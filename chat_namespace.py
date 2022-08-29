from flask_socketio import Namespace, emit, join_room, leave_room

ALL_USERS_CHAT = "all_users_chat"
ROOM_CHAT = "room_chat"
PRIVATE_CHAT = "private_chat"


class ChatNamespace(Namespace):
    def on_connect(self):
        print("Successfully connected!")
        pass

    def on_disconnect(self):
        print("Successfully disconnected!")
        pass

    def on_all_users_chat(self, data):
        emit(ALL_USERS_CHAT, data, broadcast=True)

    def on_join_room(self, data):
        username = data["username"]
        room = data["room"]
        join_room(room)
        admin_message = {
            "username": "admin",
            "message": username + " has entered the room."
        }
        emit(ROOM_CHAT, admin_message, to=room)

    def on_leave_room(self, data):
        username = data["username"]
        room = data["room"]
        leave_room(room)
        admin_message = {
            "username": "admin",
            "message": username + " has left the room."
        }
        emit(ROOM_CHAT, admin_message, to=room)

    def on_room_chat(self, data):
        room = data["room"]
        emit(ROOM_CHAT, data, to=room)

    def on_join_private_chat(self, data):
        user1 = data["user1"]
        user2 = data["user2"]
        room = user1 + user2
        join_room(room)
        admin_message = {
            "username": "admin",
            "message": "Start chatting with " + user2
        }
        emit(PRIVATE_CHAT, admin_message, to=room)

    def on_private_chat(self, data):
        user1 = data["user1"]
        user2 = data["user2"]
        room = user1 + user2
        emit(PRIVATE_CHAT, data, to=room)
