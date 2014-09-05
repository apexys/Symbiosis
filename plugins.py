#!/usr/bin/env python
from sys import argv, exit
from abc import ABC

class CommunicationPlugin( ABC ):
    def __init__( self, recv_callback, *args, **kwargs ):
        pass

    def login( credentials ):
        pass

    def logout():
        pass

    def send( to, data ):
        pass

    def query( query_data ):
        pass

    def showQueryUI():
        pass

if __name__ == "__main__":
    pass
