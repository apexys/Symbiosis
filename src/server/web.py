#!/usr/bin/env python

from sys import argv, exit
from flask import Flask, session, escape, request, make_response
from json import dumps
from util import slurp
from argparse import ArgumentParser
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

import database as db

app = Flask( __name__ )
sql = db.Session()

def default_response():
    return { 'infos': [], 'warnings': [], 'errors': [] }

def to_json( f ):
    def result( *args, **kwargs ):
        return make_response( dumps( f( *args, **kwargs ) ) )
    return result

@app.route( '/' )
def index():
    return slurp('../clients/static/index.html')

@app.route( '/login', methods = ['POST'] )
@to_json
def login():
    response = default_response()
    data = request.form
    try:
        db_user = sql.query( db.User ).filter( db.User.name == data[ 'username' ] ).one()
    except NoResultFound:
        response[ 'errors' ].append( 'Username not found' )
        return response

    #TODO implement user password check
    response[ 'infos' ].append( 'Login successful' )

    return response

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument( '-d', '--debug', action = 'store_true',
                         help = 'enable flask debug mode' )
    parser.add_argument( '-c', '--create_database', action = 'store_true',
                         help = 'create the database' )

    args = parser.parse_args()
    if args.create_database:
        print( 'Trying to create database' )
        db.create_database()
        print( 'If everything worked, you can now start again without -c' )
        exit( 0 ) #you probably don't want to pass -c again for each restart

    app.run( debug = args.debug )
