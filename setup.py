# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "hello_flask_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="My First Swagger file",
    author_email="",
    url="",
    keywords=["Swagger", "My First Swagger file"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['hello_flask_server=hello_flask_server.__main__:main']},
    long_description="""\
    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
    """
)

