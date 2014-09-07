#!/usr/bin/env python
from sys import argv, exit
from util import slurp, spit
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship, sessionmaker

from sqlalchemy import Column, String, Integer, ForeignKey, create_engine, \
                       UniqueConstraint, Table

Base = declarative_base()
db_conf_file = 'sql_engine.conf' 

try:
    engine = create_engine( slurp( db_conf_file ), echo = True )
except FileNotFoundError:
    spit( db_conf_file, 'sqlite:////tmp/symbiosis.sqlite3' )
    print( '[INFO] wrote default database config' )
    engine = create_engine( slurp( db_conf_file ), echo = True )

Session = sessionmaker( bind = engine )

def create_database():
    Base.metadata.create_all( engine )

def id_col():
    return Column( Integer, primary_key = True )

class User( Base ):
    __tablename__ = 'user'
    id = id_col()
    name = Column( String )
    UniqueConstraint( 'name' )
    salt = Column( String )
    hashed_auth_data = Column( String )

    contexts = relationship( 'Context', secondary = 'user_in_context' )

    def __init__( self, name, password ):
        self.name = name
        self.salt = 'REPLACEMEWITHSOMETHINGRANDOM' #TODO randomize
        self.hashed_auth_data = password #TODO hash it

    def check_password( self, password ):
        return password == self.hashed_auth_data #TODO make it secure


class Message( Base ):
    __tablename__ = 'message'
    id = id_col()
    text = Column( String )
    user_id = Column( Integer, ForeignKey( User.id ) )
    context_id = Column( Integer, ForeignKey( 'context.id' ) )

    user = relationship( User, backref = backref( 'messages' ) )
    context = relationship( 'Context' )

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
    service = relationship( Service, uselist = False ) #one to one

class Context( Base ):
    __tablename__ = 'context'
    id = id_col()
    name = Column( String )

    users = relationship( User, secondary = 'user_in_context' )

user_in_context = Table( 'user_in_context', Base.metadata,
    Column( 'context_id', Integer, ForeignKey( Context.id ) ),
    Column( 'user_id', Integer, ForeignKey( User.id ) ) )

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
