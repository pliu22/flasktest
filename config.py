# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Config(object):
	pass

class ProdConfig(Config):
	pass

class DevConfig(Config):
	DEBUG = True
	host  = "0.0.0.0"
	SQLALCHEMY_DATABASE_URI  = "sqlite:///flasktest.db"
	SQLALCHEMY_ECHO = True