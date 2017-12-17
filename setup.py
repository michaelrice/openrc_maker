import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as fn:
        return fn.read()

setup(
    name='openrc_maker',
    version='0.0.1',
    packages=['openrcgen'],
    install_requires=required,
    url='https://github.com/michaelrice/openrc_maker',
    license='Apache 2.0',
    author='Michael Rice',
    author_email='michael@michaelrice.org',
    # NOTE: pypi prefers the use of RST to render docs
    long_description=read('README.rst'),
    description='Cheesy tool to make openrc files for OpenStack when '
                'SAML2 is needed to get the initial token.',
    entry_points='''
        [console_scripts]
        os_openrcgen=openrcgen.cli:make_openrc
    ''',
)
