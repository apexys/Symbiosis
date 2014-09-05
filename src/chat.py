#!/usr/bin/env python
from sys import argv, exit
from time import time
from collections import namedtuple

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
    """
    A user
    """
    pass

Message = namedtuple( 'Message', 'contact direction message' )

if __name__ == "__main__":
    pass
