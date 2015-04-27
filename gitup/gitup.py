import os
import os.path
import sys
import subprocess
import gitupconf


projects = gitupconf.projects


def clone_projects():
    print 'Cloning projects...'
    for project in projects:
        project_dir = os.path.realpath(project['dir'])
        if not os.path.isdir(project_dir):
            print subprocess.check_output(
                ['git', 'clone', project['url'], project_dir])
        else:
            print 'Skipping %s - directory already exists: %s' \
                % (project['name'], project_dir)
    print 'done!'


def git_info():
    for project in projects:
        print '\nGit info for %s' % project['name']
        project_dir = os.path.realpath(project['dir'])
        os.chdir(project_dir)
        # Fetch changes to origin and prune deleted branches
        print subprocess.check_output(['git', 'fetch', '--all', '-p'])
        # Print branch information for local and remote
        print 'Branch info:'
        print subprocess.check_output(['git', 'branch', '-vv', '-a'])
        # Get status for each branch
        for branch in project['branches']:
            print '\nChecking out branch: %s' % branch
            print subprocess.check_output(['git', 'checkout', branch])
            print 'Status:'
            print subprocess.check_output(['git', 'status'])
        print '-' * 80


def main():
    usage = '''
    gitup.py - Git project manager
    python gitup.py [command]
    Commands:
        clone   - clone all projects into git project directory
        info    - fetch updates and print status and branch info for projects
    '''

    if not len(sys.argv) > 1:
        print usage
        sys.exit(1)
    command = sys.argv[1]
    if command == 'clone':
        clone_projects()
    elif command == 'info':
        git_info()
    else:
        print usage


if __name__ == '__main__':
    main()
