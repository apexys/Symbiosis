#!/usr/bin/env python
from sys import argv, exit
from util import slurp, spit
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

from sqlalchemy import Column, String, Integer, ForeignKey, create_engine

Base = declarative_base()

def create_database():
    try:
        engine = create_engine( slurp( 'sql_engine.conf' ), echo = True )
    except FileNotFoundError:
        print( '[ERROR] Please create a sql_engine.conf file. You can create '
               'such a file by invoking python database.py config' )
        exit( 1 )
    Base.metadata.create_all( engine )

def id_col():
    return Column( Integer, primary_key = True )

class User( Base ):
    __tablename__ = 'user'
    id = id_col()
    name = Column( String )
    salt = Column( String )
    hashed_auth_data = Column( String )

class Message( Base ):
    __tablename__ = 'message'
    id = id_col()
    text = Column( String )
    user_id = Column( Integer, ForeignKey( User.id ) )
    context_id = Column( Integer, ForeignKey( 'context.id' ) )

    user = relationship( User, backref = backref( 'messages' ) )
    context = relationship( 'context' )

class Service( Base ):
    __tablename__ = 'service'
    id = id_col()
    name = Column( String )

class Contact( Base ):
    __tablename__ = 'contact'
    id = id_col()
    service_id = Column( Integer, ForeignKey( Service.id ) )
    handle = Column( String )
    user_id = Column( Integer, ForeignKey( User.id ) )

    user = relationship( User, backref = 'contacts' )
    service = relationship( Service )

class Context( Base ):
    __tablename__ = 'context'
    id = id_col()
    name = Column( String )

class UserInContext( Base ):
    __tablename__ = 'user_in_context'
    id = id_col()
    context_id = Column( Integer, ForeignKey( Context.id ) )
    user_id = Column( Integer, ForeignKey( User.id ) )

    #oh, the joy of many-to-many relationships
    context = relationship( Context, backref = 'users_in_context' )
    users = relationship( User, backref( 'user_in_contexts' ) )

class ChatItem( Base ):
    __tablename__ = 'chat_item'
    id = id_col()
    context_id = Column( Integer, ForeignKey( Context.id ) )
    user_id = Column( Integer, ForeignKey( User.id ) )
    message = Column( String )

    context = relationship( Context, backref = 'items' )
    author = relationship( User, backref = 'items' )


if __name__ == "__main__":
    if len( argv ) > 1:
        if argv[ 1 ] == 'create':
            create_database()
        elif argv[ 1 ] == 'config':
            spit( 'sql_engine.conf', 'sqlite:///:memory:' )
            print( '[INFO] wrote default config' )
