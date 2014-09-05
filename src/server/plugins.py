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
        pass

    def login( credentials : dict ):
        """
        Log in with at the service with credentials

        :param credentials: Data for login
        """
        pass

    def logout():
        """
        Log out from the service and disconnect
        """
        pass

    def send( message ):
        """
        Send a message

        :param message: Object of type Message with all the required data
        """
        pass

    def get_active_sessions() -> [ChatSession]:
        """
        Get a list of all currently active sessions

        :return: A list of all active sessions that this plugin manages
        """
        pass


if __name__ == "__main__":
    pass
