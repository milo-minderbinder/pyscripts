from setuptools import setup, find_packages

setup(
    name='mailer',
    version='0.1.0',
    description='A simple emailing utility',
    url='https://github.com/milo-minderbinder/pyscripts',
    author='Milo Minderbinder',
    author_email='minderbinder.enterprises@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience "" Developers',
        'Topic :: Software Development :: Tools',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4'
    ],
    keywords='email sms mms messaging',
    packages=find_packages(exclude=['tests*']),
    entry_points={
        'console_scripts': [
            'mailer = mailer.__main__:main'
        ]
    }
)
