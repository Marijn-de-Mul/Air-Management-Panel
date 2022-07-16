from flask import Flask, render_template, redirect, request, url_for
from __main__ import app

@app.route('/', methods=['POST', 'GET'])
def index(): 
    return render_template('login.html')  