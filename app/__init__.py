#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-23 22:43:10
# @Author  : darmon (ren675523481@gmail.com)
# @Link    : github.com/KunPengRen
# @Version : $Id$

from flask import Flask
from flask_mongoengine import MongoEngine
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config.from_object("config")
bootstrap = Bootstrap(app)
db = MongoEngine(app)

from app import models,api,tpamain
