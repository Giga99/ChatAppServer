from flask import Flask
from flask_socketio import SocketIO

from chat_namespace import ChatNamespace
from configuration import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
socketio = SocketIO(app, logger=True, engineio_logger=True)


def start_chat():
    socketio.on_namespace(ChatNamespace('/chat'))


if __name__ == '__main__':
    start_chat()
    socketio.run(app, debug=True)
