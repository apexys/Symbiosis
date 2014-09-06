#!/usr/bin/env python

from sys import argv, exit
from flask import Flask, session, escape, request, render_template
from json import dumps as to_json
from util import slurp

app = Flask( __name__ )

@app.route( '/' )
def index():
    return slurp('../clients/static/index.html')

if __name__ == "__main__":
    app.run( debug = True )

