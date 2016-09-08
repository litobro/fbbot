from plugin import plugin

class Ping(plugin):

    def activate(self):
        self.register_user_command('ping')

    def ping(self, words):
        return "pong"
