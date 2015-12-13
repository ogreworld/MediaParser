#!usr/bin/python
# -*- coding: utf-8 -*-
#
# file_name: setup
# description: 
# author: libo
# Histort:
# 	first created: 2015/11/16

__author__ = 'libo'

import sys
from setuptools import setup, find_packages
from glob import glob

sys.path.insert(0, './lib/')

import MediaParser

rc_doc = glob('doc/*')

setup(name          = 'MediaParser',
      version       = MediaParser.__version__,
      package_dir   = {'' : 'lib'},
      packages      = ['MediaParser'],
      description   = 'MediaParser',
      include_package_data = True,
      data_files    = [('doc', rc_doc)],
      )