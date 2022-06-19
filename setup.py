# @copyright: AlertAvert.com (c) 2016. All rights reserved.

from setuptools import setup
import pathlib

import setuptools

try:
    here = pathlib.Path(__file__).parent.resolve()
    # Get the long description from the README file
    long_description = (here / "README.md").read_text(encoding="utf-8")
    long_description_content_type = "text/markdown"
except ImportError:
    long_description = """This python package is based from python mysql connector. It allows you to easily consume MySQL service without doing much of the code.
    """
    long_description_content_type = "text/plain"

from ezsql import __version__ as VERSION

setup(name='python-ezsql',
      description='This python package is based from python mysql connector',
      long_description_content_type=long_description_content_type,
      long_description=long_description,
      version=VERSION,
      url='https://github.com/Mackhintoshi/EzSQL',
      author='Jerick GUtierrez',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3'
      ],
      #packages=setuptools.find_packages(where="ezsql"),
      packages=[
        "ezsql",
        "ezsql/lib",
        "ezsql/tests",
        ],
      install_requires=[
          'mysql-connector-python',
      ]
      )