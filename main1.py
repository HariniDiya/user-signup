from flask import Flask, request, redirect,render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('form.html')

#@app.route("/hello",methods=['POST'])
#def validate_name():
 #   first_name = request.form['first_name']
  #  if first_name.length()==0:
   #     print("Enter valid username")



@app.route("/hello", methods=['POST'])
def hello():
   first_name = request.form['first_name']
   return render_template('greeting.html',name=first_name)
app.run()