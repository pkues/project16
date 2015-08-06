import os
from flask import Flask, jsonify, request, redirect, url_for, render_template, session
from dir import Dirmanager

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/', methods=['GET'])
def index():
    if not 'cur_dir' in session.keys():
        session['cur_dir'] = os.getcwd()
    if not 'tables' in session.keys():    
        session['tables'] = []
        session['tablepaths'] = []       
    files = [{'name':session['tables'][i],'path':session['tablepaths'][i]} for i in range(len(session['tables']))]
    return render_template('dir.html',cur_dir = session['cur_dir'], dirs = Dirmanager.listdir(session['cur_dir']),files=files)

@app.route('/managefile', methods=['GET','POST'])
def managefile():
    if request.method == 'GET':
        session['cur_dir'] = Dirmanager.changedir(session['cur_dir'],request.args.get('cur_dir'))
        return jsonify(x = Dirmanager.listdir(session['cur_dir']),y = session['cur_dir'])
    if request.method == 'POST':
        #add file and paths in session
        for i in range(len(request.json['files'])):
            if not request.json['filepaths'][i] in session['tablepaths']:
                session['tablepaths'].append(request.json['filepaths'][i])
                session['tables'].append(request.json['files'][i])
        reto = {'files':session['tables'],'filepaths':session['tablepaths']}
        return jsonify(reto)

@app.route('/deletetable', methods=['POST'])
def deletetable():
    if request.method == 'POST':
        for i in range(len(session['tablepaths'])):
            if request.json['filepaths'] == session['tablepaths'][i]:
                del session['tablepaths'][i]
                del session['tables'][i]
                break
        reto = {'files':session['tables'],'filepaths':session['tablepaths']}        
        return jsonify(reto)
    
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True)


