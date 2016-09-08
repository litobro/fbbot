from yapsy.IPlugin import IPlugin

class plugin(IPlugin):

    user_keyword_vector = {}
    admin_keyword_vector = {}

    def register_user_command(self, keyword):
        self.user_keyword_vector[keyword] = getattr(self, keyword)

    def register_admin_command(self, keyword):
        self.admin_keyword_vector[keyword] = getattr(self, keyword)

    def activate(self):
        #Should be overridden and implemented at plugin level
        pass

    def deactivate(self):
        pass
