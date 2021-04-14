import flask
from flask import render_template , make_response, request, session,redirect,url_for
import os, shutil, glob
from dirsync import sync


app = flask.Flask(__name__)
app.config["DEBUG"]=True

app.secret_key= os.urandom(16)

@app.route('/')
def page_1():

    dir1='C:/Users/yahio/Desktop/'
    dir2='C:/Users/yahio/Desktop/'
    
    if not os.path.exists(dir1):
        os.mkdir(dir2)
        
    if not os.path.exists(dir2):
        os.mkdir(dir2)

    return render_template("accueil.html",dir1=dir1,dir2=dir2)


@app.route('/synchro', methods=['GET', 'POST'])
def synchro():


    dir1rawdata = request.form.getlist('dir1[]')
    dir1=dir1rawdata[0]

    dir2rawdata = request.form.getlist('dir2[]')
    dir2=dir2rawdata[0]


    if not os.path.exists(dir1):
        os.mkdir(dir1)
        
    if not os.path.exists(dir2):
        os.mkdir(dir2)

    ext = request.form.getlist('ext[]')


    if not os.path.exists(dir1):
        dir1+='       DIR 1 PAS LA'
    
    if not os.path.exists(dir2):
        dir2+='       DIR 2 PAS LA'
    

    source_path = dir1
    target_path = dir2
    
    for i in ext:
        sync(source_path, target_path, 'sync', verbose=True, only=(r'^.*\.'+i+'$',))
        sync(target_path, source_path, 'sync', verbose=True, only=(r'^.*\.'+i+'$',))
    
    return render_template("synchro.html",data1=dir1rawdata[0],data2=dir2rawdata[0], data3=ext)

    '''if not os.path.exists('C:/Users/Amird/OneDrive/Desktop/travail/formation/dossier1'):
        os.mkdir('C:/Users/Amird/OneDrive/Desktop/travail/formation/dossier1')
        
    if not os.path.exists('C:/Users/Amird/OneDrive/Desktop/travail/formation/dossier2'):
        os.mkdir('C:/Users/Amird/OneDrive/Desktop/travail/formation/dossier2')
'''


if __name__=="__main__":
    app.run()
