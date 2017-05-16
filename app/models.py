#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-23 22:43:36
# @Author  : darmon (ren675523481@gmail.com)
# @Link    : github.com/KunPengRen
# @Version : $Id$abc

from app import db
import datetime
from flask_mongoengine.wtf import model_form

class Quest(db.Document):
	#Columns
	userid = db.StringField(required=True,max_length=20)
	fileid = db.StringField(required=True,max_length =20)
	random = db.ListField()
	result = db.BooleanField()

#class User(db.Document):
	