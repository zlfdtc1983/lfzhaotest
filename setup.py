#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 注意 如果要使用上传功能，需要安装twine包:
#   $ pip install twine

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command


# 神奇的操作，一个函数完事
setup(
  name = "lfzhaotest",
  version = "0.1.1",
  keywords = ("pip", "pathtool","lfzhaotest"),
  description = "lfzhao test",
  long_description = "a test for pip",
  license = "MIT Licence",
 
  url = "https://github.com/zlfdtc1983/lfzhaotest",
  author = "lfzhao",
  author_email = "lfzhao@126.com",
 
  packages = find_packages(),
  include_package_data = True,
  platforms = "any",
  install_requires = []
)
