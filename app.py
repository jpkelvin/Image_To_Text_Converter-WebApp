from flask import Flask,redirect,url_for,render_template,request
from extracter import text
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/submit',methods=['POST','GET'])
def output():
    Image=''
    if request.method=='POST':
        return Image
if __name__=='__main__':
    app.run(debug=True)
