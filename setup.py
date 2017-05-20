# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import shutil
import os
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
if not os.path.exists('scripts'):
    os.makedirs('scripts')
shutil.copyfile('src/unox/unox.py', 'scripts/unison-fsmonitor')

setup(
    name='unox',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.2.0',

    description='Unox',
    long_description='',

    # The project's main homepage.
    url='https://github.com/wistia/unox',

    # Author details
    author='Hannes Landeholm ',
    author_email='hannes.landeholm@gmail.com',

    # Choose your license
    license='MPLv2',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Filesystems',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries',
        'Operating System :: MacOS :: MacOS X',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='unison macfsvents',

    # You can just speciunify the packages manually here if your project is
    # simple. Or you can use find_packages().
    package_dir={'': './src'},
    packages=find_packages('./src'),
    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    py_modules=["unox"],

    # we need to install pathtools since watchdog depends on it but did not define the dep
    install_requires=['macfsevents'],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #     'console_scripts': [
    #         'unison-fsmonitor=unox.unox:main',
    #     ],
    # },
    scripts=['scripts/unison-fsmonitor']
)
