#!/usr/bin/env python

"""ALPRBD: Automated license plate recognition system for Bangladesh.

ALPRBD provides a api to work with license plate numbers of vehicles 
in Bangladesh. The system is divided into four stages: Detection, 
Extraction, Segmentation, and Recognition.

Detection: locates all possible regions of interest.
Extraction: extracts region of interest and clean them up.
Segmentation: segments characters from license plate.
Recognition: recognizes each segments with a probability.

Finally all modules put together to display the final results
of recognized plate numbers with their accuracy in percentage.
"""
from setuptools import setup

DOCLINES = (__doc__ or '').split("\n")

"""
setup(
    name='alprbd',
    version='0.0.1',

    description='Automated License Plate Recognition for Bangladesh',
    long_description=DOCLINES,

    # The project's main homepage.
    url='http://github.com/dipu-bd/alprbd',

    author='Sudipto Chandra',
    author_email='dipu.sudipta@gmail.com',
    license='MIT',
    packages=[
        'alprbd',
        'numpy',
        'opencv-python',
        'tensorflow',
    ],
    zip_safe=False
)"""

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='alprbd',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.1',

    description='Automated License Plate Recognition system for Bangladesh',
    long_description=long_description,

    # The project's main homepage.
    url='http://github.com/dipu-bd/alprbd',

    # Author details
    author='Sudipto Chandra',
    author_email='dipu.sudipta@gmail.com',

    # Choose your license
    #license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 2 - Pre-Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: End Users/Desktop',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        "Operating System :: MacOS",

        'Environment :: Console',
        'Natural Language :: English',

    ],

    # What does your project relate to?
    keywords='alpr anpr bangladesh vechile',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    #packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    packages=[
        'alprbd'
    ],

    package_dir={
        'alprbd': 'src/alprbd'
    },

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'alprbd': ['trained/*.npz']
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[('my_data', ['data/data_file'])],


    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'numpy',
        'opencv-python',
        'tensorflow'
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'alprbd=alprbd:main',
        ],
    },
)
