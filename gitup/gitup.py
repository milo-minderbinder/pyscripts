import os
import os.path
import logging
import subprocess
import gitupconf


log = logging.getLogger('gitup.gitup')
projects = gitupconf.projects
log.debug('Configured projects: \n%s' %
          ('\n'.join([project['dir'] for project in projects])))


def read_process(args):
    output = ''
    try:
        proc = subprocess.Popen(args,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                universal_newlines=True)
        proc_out, proc_err = proc.communicate()
        if proc_out:
            output += '\n%s\n' % proc_out
        if proc_err:
            output += '\n%s\n' % proc_err
    except OSError as e:
        log.error('Exception while running read_process with args: %s'
                  % str(args))
        log.error('Exception: %s' % str(e))
    return output


def clone_projects():
    log.info('Cloning projects...')
    for project in projects:
        project_dir = os.path.realpath(project['dir'])
        if not os.path.isdir(project_dir):
            log.info(read_process(
                ['git', 'clone', project['url'], project_dir]))
        else:
            log.info('Skipping %s - directory already exists: %s'
                     % (project['name'], project_dir))
    log.info('...done!')


def git_info():
    for project in projects:
        output = []
        project_dir = os.path.realpath(project['dir'])
        if os.path.isdir(project_dir):
            output.append('Git info for %s' % project['name'])
            os.chdir(project_dir)
            # Fetch changes to origin and prune deleted branches
            output.append(read_process(['git', 'fetch', '--all', '-p']))
            # Get branch information for local and remote
            output.append('Branch info:')
            output.append(read_process(['git', 'branch', '-vv', '-a']))
            # Get status for each branch
            for branch in project['branches']:
                output.append('Checking out branch: %s' % branch)
                output.append(read_process(['git', 'checkout', branch]))
                output.append('Status:')
                output.append(read_process(['git', 'status']))
        else:
            log.warn('No git project named %s found in %s'
                     % (project['name'], project_dir))
        output.append('-' * 80)
        log.info('\n'.join(output))
