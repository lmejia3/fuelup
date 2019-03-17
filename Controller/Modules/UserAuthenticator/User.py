
class User:
    """
    this will represent a user. user_key and user_IP is used to represent a user
    who is currently logged in.
    """
    username = "default"
    password = "default"
    type = "default"
    user_key = "default"
    user_IP = "default"

    def __init__(self, username, password, type, user_key, user_IP):
        self.username = username
        self.password = password
        self.type = type
        self.user_key = user_key
        self.user_IP = user_IP
