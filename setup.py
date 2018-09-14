from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gerrit-hooks',
    version='1.0.1',
    description='Utility for writing Gerrit Hooks in python',
    long_description=long_description,
    author='Nils Diefenbach',
    author_email='nlsdfnbch.foss@kolabnow.com',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Version Control',
        'License :: OSI Approved :: MIT License',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
)
