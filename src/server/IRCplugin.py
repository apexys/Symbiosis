from plugins import CommunicationPlugin
from chat import Message, ChatSession
from socket import socket

class IRCPlugin (CommunicationPlugin):
    def __init__( self, recv_callback, connection_data):
        """
        Initialize a communication plugin.

        :param recv_callback: A function that takes one Message object that should be processed by the main program
        :param args: Further plugin-specific arguments
        :param kwargs: Further plugin-specific arguments
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        self._socket.connect(connection_data);
        self._socketfile = self._socket.makefile()
        self._activeSession = ChatSession('Echo Session');
        self._recv_callback = recv_callback

    def login( credentials : dict ):
        """
        Log in with at the service with credentials

        :param credentials: Data for login
        """
        self._socketfile.write('PASS ' + credentials['password'] + '\n')
        self._socketfile.write('NICK ' + credentials['username'] + '\n')
        self._socketfile.write('USER ' + credentials['username'] + ' hostname servername ' + credentials['username'] + '\n')

        self._loggedIn = True

    def logout():
        """
        Log out from the service and disconnect
        """
        self._loggedOut = True

    def send(self, message ):
        """
        Send a message

        :param message: Object of type Message with all the required data
        """
        self._recv_callback(message)

    def get_active_sessions() -> [ChatSession]:
        """
        Get a list of all currently active sessions

        :return: A list of all active sessions that self plugin manages
        """
        return self._activeSession

    def listen():
        pass

if __name__ == '__main__':
    def test_cb(message):
        print("Received Message: " + message.contact + " " + message.direction + " " + message.message)
    plugin = EchoPlugin(test_cb)
    plugin.send(Message("Testuser", "->", "Hello World!"))
