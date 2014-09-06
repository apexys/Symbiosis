#!/usr/bin/env python
from sys import argv, exit
from abc import ABC

from chat import ChatSession, Message

class CommunicationPlugin( ABC ):
    def __init__( self, recv_callback, *args, **kwargs ):
        """
        Initialize a communication plugin.

        :param recv_callback: A function that takes one Message object that should be processed by the main program
        :param args: Further plugin-specific arguments
        :param kwargs: Further plugin-specific arguments
        """
        raise NotImplemented

    def login( self, credentials : dict ):
        """
        Log in with at the service with credentials

        :param credentials: Data for login
        """
        raise NotImplemented

    def logout( self ):
        """
        Log out from the service and disconnect
        """
        raise NotImplemented

    def send( self, message ):
        """
        Send a message

        :param message: Object of type Message with all the required data
        """
        raise NotImplemented

    def get_active_sessions( self ) -> [ChatSession]:
        """
        Get a list of all currently active sessions

        :return: A list of all active sessions that this plugin manages
        """
        raise NotImplemented


if __name__ == "__main__":
    pass
