import sys
import os.path
import logging
LOG_FILE = os.path.join(os.path.dirname(__file__), 'gitup.log')
logging.basicConfig(
    filename=LOG_FILE,
    filemode='w',
    format='%(asctime)s %(name)s(%(levelname)s): %(message)s',
    level=logging.INFO)
log = logging.getLogger('gitup')
log.addHandler(logging.StreamHandler(sys.stdout))


def main():
    usage = '''
    gitup - Git project manager
    python gitup [command]
    Commands:
        clone   - clone all projects into git project directory
        info    - fetch updates and print status and branch info for projects
    '''
    import gitup
    if not len(sys.argv) > 1:
        print usage
        sys.exit(1)
    command = sys.argv[1]
    if command == 'clone':
        log.info('Running gitup clone')
        gitup.clone_projects()
    elif command == 'info':
        log.info('Running gitup info')
        gitup.git_info()
    else:
        print usage


if __name__ == '__main__':
    main()
