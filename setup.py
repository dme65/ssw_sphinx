from setuptools import setup, find_packages
long_description = open('notes.md').read()

setup(
    name='ssw_sphinx',
    version='0.1.0',
    packages=['ssw_sphinx'],
    long_description=long_description,
    classifiers=['Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 ]
)
