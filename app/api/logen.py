#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-02 22:26:50
# @Author  : darmon (ren675523481@gmail.com)
# @Link    : github.com/KunPengRen
# @Version : $Id$

import os
import json
import time
from app import app

ISOTIMEFORMAT='%Y-%m-%d %X'

def save_user_loginfo(userinfo,block_txt,radom_txt,csptxt1,csptxt2):
	logtime = time.strftime(ISOTIMEFORMAT,time.localtime())
	
	logname = userinfo['user_id'] +'_'+ userinfo['file_id'] +'_'+logtime
	block_txt_string = writetext(block_txt)
	radom_txt_string = writetext(radom_txt)
	csptxt1_string = writetext(csptxt1)
	csptxt2_string = writetext(csptxt2)
	with open(logname,"wb") as code:
		code.write(block_txt_string+"...."+radom_txt_string+"...."+csptxt1_string+"...."+csptxt2_string)

	return True
	


def writetext(filename):
	file = open(filename)
	string = ''
	while 1:
		lines = file.readlines(100000)
		if not lines:
			break
		for line in lines:
			string += line

		return string


	
	


