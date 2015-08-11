# -*- coding: utf-8 -*-
import os
from flask import Flask, jsonify, request, redirect, url_for, render_template, session
from flask.ext.session import Session
import multiprocessing as mp
import pandas as pd
import redisinit as RDI
from classes import DirManager,TableManager

app = Flask(__name__)
#store session data in redis
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)

@app.route('/', methods=['GET'])
def index():
    if not 'DM' in session.keys():
        session['DM'] = DirManager()
    if not 'TM' in session.keys():
        session['TM'] = TableManager()
        
    return render_template('dir.html',cur_dir = session['DM'].cur_dir, dirs = session['DM'].listdir(),files=session['TM'].tables)

@app.route('/managefile', methods=['GET','POST'])
def managefile():
    if request.method == 'GET':
        session['DM'].changedir(request.args.get('cur_dir'))
        return jsonify(x = session['DM'].listdir(),y = session['DM'].cur_dir)

    if request.method == 'POST':
        #add file and paths in session    
        for i in range(len(request.json['files'])):
            session['TM'].add_table(request.json['files'][i],request.json['filepaths'][i])
        reto = {'files':session['TM'].get_name(),'filepaths':session['TM'].get_path()}
        return jsonify(reto)

#ajax deletetable
@app.route('/deletetable', methods=['POST'])
def deletetable():
    if request.method == 'POST':
        session['TM'].del_table(request.json['filepaths'])
        reto = {'files':session['TM'].get_name(),'filepaths':session['TM'].get_path()}        
        return jsonify(reto)

@app.route('/tabletype', methods=['GET'])
def tabletype():
    pass

@app.route('/main', methods=['GET'])
def main():
    if request.method == 'GET':
        return 'ok'
        #return render_template('main.html',tables = tables)

if __name__ == '__main__':
    p = mp.Process(target = RDI.Run_Redis)
    p.start()
    app.run(debug=True)


