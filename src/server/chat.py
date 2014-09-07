#!/usr/bin/env python
from sys import argv, exit
from time import time
from collections import namedtuple
from enum import Enum, unique

class ChatSession:
    """
    A conversation that has at least 2 users (or in the extreme case two times
    the same user).
    """
    def __init__( self, label = '' ):
        self.label = label
        self.last_event = time()
        self.active_contacts = []


class User:
    """A user that is registered in the web-messager.

    A user is a meta-object that is associated with several accounts
    """
    def __init__( self, username, password ):
        #authenticate
        self.accounts = {} #self-chosen name -> Account object
        raise NotImplemented

    def load_accounts( self ):
        """
        Populate self.accounts from the database
        """
        raise NotImplemented

    def add_account( self, Account ):
        """
        Add account to the database and load it
        """
        raise NotImplemented

    def connect( self, *account_names ):
        """
        Connect to services.

        :param account_names: Connect the named accounts to their services. If no account_names are given, connect all accounts to their services
        """
        raise NotImplemented





Message = namedtuple( 'Message', 'contact service direction message' )
Contact = namedtuple( 'Contact', 'plugin handle nick' )
Account = namedtuple( 'Account', 'db_id state' ) #db_id references an ID in the database
AccountState = Enum( 'AccountState', 'not_registered offline connecting connected' )


if __name__ == "__main__":
    pass
