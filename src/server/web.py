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

if __name__ == "__main__":
    app.run( debug = True )

