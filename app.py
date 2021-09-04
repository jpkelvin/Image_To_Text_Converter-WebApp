from flask import Flask, config,redirect,url_for,render_template,request
from extracter import extract
from werkzeug.utils import secure_filename
import os
app=Flask(__name__)
app.config['UPLOAD_FOLDER']='static/images/'
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/submit',methods=['POST','GET'])
def output():
    if request.method=='POST':
        Img= request.files['img']
        file_name=secure_filename(Img.filename)
        Img.save(os.path.join(app.config['UPLOAD_FOLDER'],file_name))
        text=extract(file_name)
        return render_template('results.html',img=file_name, extracted_text=text)
if __name__=='__main__':
    app.run(debug=True)
