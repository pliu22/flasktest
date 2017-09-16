# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask #引入flask
from config import DevConfig #引入配置文件
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

#--------------------------------------------
#创建一个User模型
class User(db.Model):
	__tablename__ = "user" #表名
	#定义字段
	id 		= db.Column(db.Integer(), primary_key = True)
	username= db.Column(db.String(255))
	password= db.Column(db.String(255)) 

	def __init__(self,username):
		self.username = username

	def __repr__(self):
		return "<User '{}'>".format(self.username)

tags = db.Table('post_tags',
	db.Column('post_id',db.Integer, db.ForeignKey('post.id')),
	db.Column('tag_id',db.Integer,  db.ForeignKey('tag.id'))
)

#文章表
class Post(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	title = db.Column(db.String(255))
	text = db.Column(db.Text())
	publish_date = db.Column(db.DateTime())
	comments = db.relationship(
		'Comment',
		backref='post',
		lazy='dynamic'
	)
	user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
	tags = db.relationship(
		'Tag',
		secondary=tags,
		backref=db.backref('posts', lazy='dynamic')
	)

	def __init__(self, title):
		self.title = title

	def __repr__(self):
		return "<Post '{}'>".format(self.title)

#标签表
class Tag(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	title = db.Column(db.String(255))

	def __init__(self, title):
		self.title = title

	def __repr__(self):
		return "<Tag '{}'>".format(self.title)

#--------------------------------------------

@app.route('/')
def home():
	return '<h1>hello world!</h1>'

if __name__ == '__main__':
	app.run()