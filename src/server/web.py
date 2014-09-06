#!/usr/bin/env python

from sys import argv, exit
from flask import Flask, session, escape, request, render_template
from json import dumps as to_json

app = Flask( __name__ )

@app.route( '/' )
def index():
    #import os
    #return os.getcwd()
    return render_template( '../clients/static/index.html' )

@app.route( '/login', methods = [ 'POST' ] )
def login():
    data = request.form
    if data[ 'user' ] == 'dummy' and data[ 'pass' ] == 'dummy':
        return to_json( { 'infos': [ 'Login successful' ] } )
    else:
        return to_json( { 'errors': [ 'Login failed' ] } )

if __name__ == "__main__":
    app.run( debug = True )

