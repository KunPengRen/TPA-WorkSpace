#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-30 01:00:54
# @Author  : darmon (ren675523481@gmail.com)
# @Link    : github.com/KunPengRen
# @Version : $Id$

import os
import requests

def tappost():
	user_info = {'user_id':'darmon','file_id':'text1'}

	r = requests.post("http://127.0.0.1:5000/userquest",data=user_info)

	print r.text

def updatefile():
	files = {'userfile': open('text2.txt', 'rb')}  
	user_info = {'name': 'letian'}  
	#localhost="http://10.3.37.104/file/save_file.php"
	localhost="http://127.0.0.1:5000/upload"
	r = requests.post(localhost, data=user_info, files=files)
	print r.text

if __name__ == '__main__':
	#tappost()
	updatefile()