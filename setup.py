# python 2.7
from __future__ import absolute_import, unicode_literals
from io import open

# builtins
from setuptools import setup, find_packages     # Always prefer setuptools over distutils

__author__ = 'chad nelson'
__project__ = 'vue_flask'
__version__ = '0.0.2'

# Get readme.rst from sphinx docs (if available).
try:
    with open('readme.rst', encoding='utf-8') as f:
        long_description = f.read()
except (IOError, ImportError):
    # default description
    long_description = 'Demonstration of how to integrate many different frontend and backend technologies, and ' + \
                       'rapidly deploy the app serverlessly via Zappa.'

setup(
    name='vue_flask',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=__version__,

    description='VueJS, Flask, Zappa serverless deployment demo.',
    long_description=long_description,

    # The project's main homepage.
    url='',
    download_url='https://github.com/nueverest/vue_flask/',

    # Author details
    author=__author__,
    author_email='nu.everest@gmail.com',

    # License
    license='MIT',

    # Classifier Reference: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',                  # 3 - Alpha, 4 - Beta, 5 - Production/Stable
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Operating System :: OS Independent',

        # Topics
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Software Development',

        # License
        'License :: OSI Approved :: MIT License',

        # Python version support.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    # What does your project relate to?
    keywords=(
        'vue_flask vuejs flask zappa scss firebase foundation6 tutorial example blowdrycss'
    ),

    # Packages - reference: https://pythonhosted.org/setuptools/setuptools.html#using-find-packages
    #package_dir={'': 'vue_flask'},
    #packages=find_packages('vue_flask', exclude=['*.settings', '*.settings.*', 'settings.*', 'settings']),
    #packages=find_packages(exclude=['*.settings']),   # THIS ONE WORKED BUT IS NO LONGER NEEDED
    packages=find_packages(),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['Flask>=0.12', 'Flask-S3==0.3.3', 'future>=0.16.0'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install vue_flask -e .[testing, development]
    extras_require={
        'testing': ['tox>=2.6.0', 'tox-travis>=0.8', 'coverage>=4.3.4', 'selenium>=3.0.2', ],
        'development': [
            'tox>=2.6.0', 'tox-travis>=0.8', 'coverage>=4.3.4', 'selenium>=3.0.2', 'blowdrycss>=1.0.2', 'zappa>=0.37.1',
        ],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={
    #     'vue_flask': ['package_data.dat'],
    # },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    # },

    # unit_tests
    test_suite="vue_flask.unit_tests",
    #tests_require=['tox', 'coverage', ],
)