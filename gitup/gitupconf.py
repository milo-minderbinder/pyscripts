import os.path

docker_projects_dir = os.path.expanduser('~/Docker-Projects')
projects = [
    {
        'name': 'baseimage',
        'url': 'git@github.com:milo-minderbinder/docker-baseimage.git',
        'dir': os.path.join(docker_projects_dir, 'baseimage'),
        'branches': ['master']
    },
    {
        'name': 'python',
        'url': 'git@github.com:milo-minderbinder/docker-python.git',
        'dir': os.path.join(docker_projects_dir, 'python'),
        'branches': ['master']
    },
    {
        'name': 'java-jdk',
        'url': 'git@github.com:milo-minderbinder/docker-java-jdk.git',
        'dir': os.path.join(docker_projects_dir, 'java-jdk'),
        'branches': ['master', 'oracle-java6', 'oracle-java7', 'oracle-java8']
    },
    {
        'name': 'tomcat7',
        'url': 'git@github.com:milo-minderbinder/docker-tomcat7.git',
        'dir': os.path.join(docker_projects_dir, 'tomcat7'),
        'branches': ['master', 'oracle-java7', 'oracle-java8']
    },
    {
        'name': 'apache2',
        'url': 'git@github.com:milo-minderbinder/docker-apache2.git',
        'dir': os.path.join(docker_projects_dir, 'apache2'),
        'branches': ['master', 'oracle-java7', 'oracle-java8']
    },
    {
        'name': 'gradle2',
        'url': 'git@github.com:milo-minderbinder/docker-gradle2.git',
        'dir': os.path.join(docker_projects_dir, 'gradle2'),
        'branches': ['master', 'oracle-java6', 'oracle-java7', 'oracle-java8']
    },
    {
        'name': 'maven',
        'url': 'git@github.com:milo-minderbinder/docker-maven.git',
        'dir': os.path.join(docker_projects_dir, 'maven'),
        'branches': ['master', 'oracle-java7', 'oracle-java8']
    },
    {
        'name': 'spring-ref',
        'url': 'git@github.com:milo-minderbinder/docker-spring-ref.git',
        'dir': os.path.join(docker_projects_dir, 'spring-ref'),
        'branches': ['master']
    },
    {
        'name': 'example-apache2',
        'url': 'git@github.com:milo-minderbinder/docker-example-apache2.git',
        'dir': os.path.join(docker_projects_dir, 'example-apache2'),
        'branches': ['master']
    },
    {
        'name': 'openam',
        'url': 'git@github.com:milo-minderbinder/docker-openam.git',
        'dir': os.path.join(docker_projects_dir, 'openam'),
        'branches': ['master']
    },
    {
        'name': 'passcheck',
        'url': 'git@github.com:milo-minderbinder/docker-passcheck.git',
        'dir': os.path.join(docker_projects_dir, 'passcheck'),
        'branches': ['master']
    }
]
