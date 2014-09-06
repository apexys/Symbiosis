#!/usr/bin/env python

from sys import argv, exit
from flask import Flask, session, escape, request, make_response
from json import dumps as to_json
from util import slurp

app = Flask( __name__ )

@app.route( '/' )
def index():
    return slurp('../clients/static/index.html')

@app.route( '/login', methods = [ 'POST' ] )
def login():
    data = request.form
    if data[ 'user' ] == 'dummy' and data[ 'pass' ] == 'dummy':
        response = make_response(to_json( { 'infos': [ 'Login successful' ] } ))
        response.set_cookie('username', data['user']);
        response.set_cookie('password', data['pass']);
        return response
    else:
        return to_json( { 'errors': [ 'Login failed' ] } )

if __name__ == "__main__":
    app.run( debug = True )

