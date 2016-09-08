from plugin import plugin

class Echo(plugin):

    def activate(self):
        self.register_user_command('echo')

    def echo(self, words):
        return " ".join(words[2:])
