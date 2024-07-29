import flask as Flask
from flask import Flask, render_template, request, redirect, url_for, flash, session
import requests
import json
import os
import sys


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html', botStatus="0")

@app.route('/response', methods=['GET', 'POST'])
def response():
    user_message = request.form['user_message']
    print(user_message)
    response="Hello I am TroubleShooter Bot."
    return render_template('chatbot.html', user_message=user_message, response=response, botStatus="1")




if __name__ == '__main__':
    app.run(debug=True)