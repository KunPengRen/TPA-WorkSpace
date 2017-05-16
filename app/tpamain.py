#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-29 20:52:06
# @Author  : darmon (ren675523481@gmail.com)
# @Link    : github.com/KunPengRen
# @Version : $Id$

from app import app
from flask  import request,render_template,url_for
from flask import jsonify
from models import Quest
from api import audit,logen
import os




@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login",methods=['POST','GET'])
def login():
   # demoCSS = url_for("static",filename="css/style.css")
    error = None
    if request.method == 'POST':
        name =  request.form['username']
        password =request.form['password']
        print name
        
        #if request.form['username'] != 'admin' or request.form['password'] != 'admin123':
         #   error= "sorry"
        #else:
         #   return redirect(url_for('index'))
        return render_template('auditindex.html',name=name)
    return render_template('login2.html',error=error)

@app.route('/userquest',methods=['POST','GET'])
def user_quest():
	form = request.form
	
	quest = {
		'user_id' :form['user_id'],
		'file_id' : form['file_id'],
	    'token':form['token']
    }
    #audit.challenge(quest)	
	return jsonify(quest)

@app.route('/logen',methods=['POST','GET'])
def user_logen():
    return render_template('logen.html')
@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    
    if request.method == 'POST':
       
        f = request.files['userfile']
        print request.headers

        f.save(os.path.join('./', f.filename))
        
        '''
        s = request.form['name']
        with open('./test2.txt', 'a') as f:
            f.write(s)
        '''
    return 'Done!'

def save_logs():

    pass