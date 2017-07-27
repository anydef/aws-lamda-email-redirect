#!/usr/bin/env python
from setuptools import setup

# from distutils.core import setup

setup(name='Lambda SES redirect',
      version='1.0',
      description='Redirecting message from contact form to private email',
      author='Pavlo Fedyna',
      author_email='fed.pavlo@gmail.com',
      url='https://anydef.io',
      packages=['.'],
      zip_safe=False,
      install_requires=[''],
      setup_requires=['boto3']
      )
