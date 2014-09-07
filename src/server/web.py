#!/usr/bin/env python

from sys import argv, exit
from flask import Flask, session, escape, request, make_response
from json import dumps
from argparse import ArgumentParser
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from util import slurp
from chat import Message, Contact, Account


import database as db

app = Flask( __name__ )
app.secret_key = 'A super secret key' #TODO implement a random key generator

sql = db.Session()

def default_response():
    return { 'infos': [], 'warnings': [], 'errors': [] }

def to_json( f ):
    def result( *args, **kwargs ):
        return make_response( dumps( f( *args, **kwargs ) ) )
    result.__name__ = f.__name__ #flask assertion fails if one function shares several routes
    return result

@app.route( '/' )
def index():
    return slurp('../clients/static/index.html')

@app.route( '/register', methods = ['POST'] )
@to_json
def register():
    response = default_response()
    data = request.form
    try:
        username = data[ 'username' ]
        password = data[ 'password' ]
    except KeyError:
        response[ 'errors' ].append( 'Missing POST data' )
        return response

    db_users = sql.query( db.User ).filter( db.User.name == username ).all()
    if len( db_users ) != 0:
        if len( db_users ) > 1:
            print( '[BUG] Username ' + username + ' is duplicated in the database!' )
        response[ 'errors' ].append( 'User already exists' )
        return response

    db_user = db.User( username, password )
    sql.add( db_user )
    sql.commit()
    response[ 'infos' ].append( 'Registration successful!' )
    session[ 'user' ] = username
    return response



@app.route( '/login', methods = ['POST'] )
@to_json
def login():
    response = default_response()
    data = request.form
    try:
        username = data[ 'username' ]
        password = data[ 'password' ]
    except KeyError:
        response[ 'errors' ].append( 'Missing POST data' )
        return response

    try:
        db_user = sql.query( db.User ).filter( db.User.name == username ).one()
    except NoResultFound:
        response[ 'errors' ].append( 'Username not found' )
        return response

    if db_user.check_password( password ):
        response[ 'infos' ].append( 'Login successful' )
        session[ 'user' ] = username
    else:
        response[ 'errors' ].append( 'Login failed' )

    return response

@app.route( '/get_new_messages', methods = ['POST', 'GET'] )
@to_json
def get_new_messages():
    response = default_response()

    if session.get( 'user' ) is None:
        response[ 'errors' ].append( 'You are not logged in' )
        return response

    response[ 'messages' ] = []
    data = request.form

    #dummy
    msg = Message( 'dummy@example.com', 'example-service', '->', 'Hello World' )
    response[ 'messages' ].append( msg._asdict() )
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

    app.run( debug = args.debug, host = '0.0.0.0' )
