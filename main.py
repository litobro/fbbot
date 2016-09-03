import fbchat, yaml
from yapsy.PluginManager import PluginManager

class fbbot(fbchat.Client):
    pluginManager = None
    keyword_vector = {}

    def __init__(self, email, password, debug=True, user_agent=None):
        fbchat.Client.__init__(self, email, password, debug, user_agent) 
        self.pluginManager = PluginManager()
        self.pluginManager.setPluginPlaces(['plugins'])
        self.pluginManager.collectPlugins()

        for plugin in self.pluginManager.getAllPlugins():
            try:
                pass #TODO: Implement actual plugin loading of keywords and recognize them below in on_message
            except Exception as ex:
                print(ex)

    def on_message(self, mid, author_id, author_name, message, metadata):
        self.markAsDelivered(author_id, mid)
        self.markAsRead(author_id)

        #Check for self author
        if str(author_id) != str(self.uid):
            #trigger word
            if message.startswith("/bot"):
                pass #TODO: Implement plugin system for commands here

with open("config.yaml", "r") as stream:
    try:
        pair = yaml.load(stream)
        fb_user = pair['fb_user']
        fb_pass = pair['fb_pass']
    except yaml.YAMLError as e:
        print(e)

client = fbbot(fb_user, fb_pass)
client.listen()
