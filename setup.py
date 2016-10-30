from setuptools import setup, find_packages
from os import path

from version import __version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'docs/README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirements = [
        line
        for line in f
    ]

setup(
    name='ucuenca',
    version=__version__,
    description='Librería de Python para la API de la Universidad de Cuenca',
    long_description=long_description,
    url='https://github.com/stsewd/ucuenca.py',
    author='Santos Gallegos',
    author_email='santos_g@outlook.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='ucuenca api development',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=requirements
)
