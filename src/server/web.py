#!/usr/bin/env python

from sys import argv, exit
from flask import Flask, session, escape, request, render_template
from json import dumps as to_json
from util import slurp

app = Flask( __name__ )

@app.route( '/' )
def index():
    return slurp('../clients/static/index.html')

@app.route( '/login', methods = [ 'GET' ] )
def login():
    data = request.form
    if data[ 'user' ] == 'dummy' and data[ 'pass' ] == 'dummy':
        return to_json( { 'infos': [ 'Login successful' ] } )
    else:
        return to_json( { 'errors': [ 'Login failed' ] } )

if __name__ == "__main__":
    app.run( debug = True )

