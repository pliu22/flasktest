# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Config(object):
	pass

class ProdConfig(Config):
	pass

class DevConfig(Config):
	DEBUG = True