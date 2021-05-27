# -*- coding: utf-8 -*-
"""
Created on Wed May 26 22:34:37 2021

@author: pratik.chatterjee
"""

# what is Flask?

"""
Flask is a microservice web based framework which allows us to expose our
business logic and functions through an API

"""

from flask import Flask, request

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def add():
    a=request.args.get("a")
    b=request.args.get("b")
    c=request.args.get("c")
    
    return str(int(a)+int(b)+int(c))

if __name__=='__main__':
    app.run(port=7000) # the port varible is used to specify which port we want to run the app else default will be taken
    