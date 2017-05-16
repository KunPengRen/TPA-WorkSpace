  #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-29 20:43:50
# @Author  : darmon (ren675523481@gmail.com)
# @Link    : github.com/KunPengRen
# @Version : $Id$

import requests
import json

from app import app


cspserver_ip='127.0.0.1:50000'
#挑战信息环节
def challenge(quest):
	r_data = get_block_num(quest)
	if r_data['result']:
		block_num = r_data['block_num']
		prove_resoult=post_challengeinfo(quest,block_num)
		return prove_resoult


	else:
		return False


#调用审计算法，生成随机文件块，并发送挑战函数请求

'''
csp返回格式
{
	"user_id":"",
	"file_id":"",
	"txt1":"",
	"txt2":"",
}

'''

def post_challengeinfo(userinfo,block_num,):
	#调用审计算法生成两个text文件
	#txt1,txt2
	prove_api= ''
	user_info = {'user_id':userinfo['user_id'],'filed_id':userinfo['file_id']}
	files = {'txt1':open('txt1.txt','rb'),'txt2':open('txt2.txt','rb')}
	adress = cspserver_ip+prove_api
	r = requests.post(adress,data = userinfo,files =files)
	r_data = json.loads(r.text)
	return r_data


#根据收到的验证信息，调用审计算法 审计文件完整性

def check_prove_info(prove_info):

	txt1_adress = prove_info['txt1']['adress']
	txt2_adress = prove_info['txt2']['adress']
	text1name = prove_info['txt1']['name']
	text2name = prove_info['txt2']['name']
	r1 = requests.get(txt1_adress)
	r2 = requests.get(txt2_adress)
	with open(text1name,"wb") as code:
		code.write(r1.content)
	with open(text2name,"wb") as code:
		code.write(r2.content)
	return verify_by_tpa(text1name,text2name)

	


#验证用户信息和身份 json格式
'''
	csp返回格式
	{"result":true
	 "block_num":"1024"
	}
'''

def get_block_num(userinfo):
	block_api=''
	adress = cspserver_ip+block_api
	r = requests.post(adress,data=userinfo)
	r_data = json.loads(r.text)
	return r_data



