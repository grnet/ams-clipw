from setuptools import setup

NAME = "cloud-info-provider-wrapper-scripts"

setup(
    name=NAME,
    version="1",
    author='GRNET',
    description='Cloud info provider wrapper',
    long_description='A wrapper for cloud info provider',
    url='https://github.com/grnet/ams-clipw',
    entry_points = {
        'console_scripts' : ['ams-clipw=ams.publish:main'],
    },
    package_dir={'ams': './ams/'},
    packages=['ams'],
    install_requires=['argo-ams-library', 'requests']
    )
