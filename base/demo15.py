# -*- coding: utf-8 -*-

# 模块
from __future__ import division
from math import log
from logging import log as logger   # as 起别名

print log(10)
logger(10, 'import from logger')

# python中动态导入模块
try:
    import json
except ImportError:
    import simplejson as json

print json.dumps({'python':2.7})

# python之使用__future__
# Python的新版本会引入新的功能，但是，实际上这些功能在上一个老版本中就已经存在了。要“试用”某一新的特性，就可以通过导入__future__模块的某些功能来实现。

print 10 / 3
