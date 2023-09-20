
# http://www.apache.org/licenses/LICENSE-2.0

from setuptools import setup

LONG_DESCRIPTION = ""

SHORT_DESCRIPTION = """program for controlling lab instruments with pyvisa and serial. mainly for SCPI.""".strip()

DEPENDENCIES = ['pyvisa','termcolor','serial']

TEST_DEPENDENCIES = []

VERSION = '0.0.1'
URL = 'https://github.com/google/python-fire'

setup(name='pyinstro',version=VERSION,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url=URL,
    author='Vijay Panchal',
    license='Apache Software License',
    classifiers=[
        'Development Status :: Beta',
        'Intended Audience :: Scientists',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        
        'Operating System :: Windows',
    ],
    keywords='controlling lab instruments with python package, support SCPI',
    packages=['pyinstro'],
    install_requires=DEPENDENCIES,
    tests_require=TEST_DEPENDENCIES,)
