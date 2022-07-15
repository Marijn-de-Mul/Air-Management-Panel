from flask import Flask, render_template, redirect, request, url_for
from __main__ import app, db, Todo

@app.route('/login/', methods=['POST', 'GET'])
def login(): 
    return render_template('login.html')  