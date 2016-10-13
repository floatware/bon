from flask import render_template, session, redirect, url_for, request, flash, g, jsonify, abort

from lms import app

@app.route('/')
def index():
    return 'hello'

@app.route('/login', methods=['GET', 'POST'])
def login():
  form_data = []
  if request.method == 'POST':
    email = request.form["email"]
    password = request.form["password"]
  else:
    return render_template('login.html')

@app.route('/bon')
def request():
  return render_template('request-access.html')



