#!/usr/bin/env python
import setuptools

try:
  with open('ReadMe.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()
except (IOError, OSError):
  long_description = ''

setuptools.setup(
  name                         	= 'xontrib-linuxbrew',
  version                      	= '0.1.1',
  license                      	= 'MIT',
  author                       	= 'Evgeny',
  author_email                 	= '',
  description                  	= "Add Homebrew's shell environment to xonsh on Linux",
  long_description             	= long_description,
  long_description_content_type	= 'text/markdown',
  python_requires              	= '>=3.6',
  install_requires             	= ['xonsh'],
  packages                     	= ['xontrib'],
  package_dir                  	= {'xontrib': 'xontrib'},
  package_data                 	= {'xontrib': ['*.xsh']},
  platforms                    	= 'any',
  url                          	= 'https://github.com/eugenesvk/xontrib-linuxbrew',
  project_urls = {
    "Documentation"	: "https://github.com/eugenesvk/xontrib-linuxbrew/blob/master/ReadMe.md",
    "Code"         	: "https://github.com/eugenesvk/xontrib-linuxbrew",
    "Issue tracker"	: "https://github.com/eugenesvk/xontrib-linuxbrew/issues",
  },
  classifiers=[
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Topic :: System :: Shells",
    "Topic :: System :: System Shells",
    "Topic :: Terminals",
  ]
)
