#!/usr/bin/env python
from distutils.core import setup

setup(name='wordpress-installer',
      version='0.0.1',
      description='A command-line tool for installing a WordPress project',
      long_description="A command-line tool for installing a WordPress project",
      author='Ryan Bagwell',
      author_email='ryan@ryanbagwell.com',
      url='https://github.com/ryanbagwell',
      py_modules=['wpinstaller'],
      scripts=['wpinstaller/wpinstall'],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Programming Language :: PHP',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
      ],
      install_requires=[
        'wordpress-package-manager==0.9.2'
      ]
    )