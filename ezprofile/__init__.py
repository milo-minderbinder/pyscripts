import os
import os.path
import tempfile
import cProfile
import pstats


def profile(entrypoint, ep_globals=None, ep_locals=None):
    if not ep_globals:
        ep_globals = globals()
    if not ep_locals:
        ep_locals = locals()
    profile_dir = tempfile.mkdtemp(prefix='profile-', dir=os.getcwd())
    print 'Profiling [[%s]] - writing data and results to: %s' \
        % (entrypoint, profile_dir)
    profile_data = os.path.join(profile_dir, 'profile.dat')
    cProfile.runctx(entrypoint,
                    ep_globals,
                    ep_locals,
                    profile_data)
    write_results(profile_data)


def write_results(profile_data, *sort_keys):
    if len(sort_keys) == 0:
        sort_keys = ('cumtime', 'ncalls')
    profile_dir = os.path.dirname(profile_data)
    results_file = os.path.join(profile_dir, 'profile_results.txt')
    with open(results_file, 'w') as ofile:
        stats = pstats.Stats(profile_data, stream=ofile)
        stats.sort_stats(*sort_keys)
        stats.print_stats()
    print 'Wrote profile results to: %s' % results_file
