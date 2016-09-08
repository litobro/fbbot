import fbchat, yaml
from yapsy.PluginManager import PluginManager

class fbbot(fbchat.Client):
    pluginManager = None
    user_keyword_vector = {}
    admin_keyword_vector = {}

    def __init__(self, email, password, debug=True, user_agent=None):
        fbchat.Client.__init__(self, email, password, debug, user_agent) 
        self.pluginManager = PluginManager()
        self.pluginManager.setPluginPlaces(['plugins'])
        self.pluginManager.collectPlugins()

        #Register all the keywords and the name of their respective plugin
        for plugin in self.pluginManager.getAllPlugins():
            try:
                self.pluginManager.activatePluginByName(plugin.name)
                for key in plugin.plugin_object.user_keyword_vector.keys():
                    self.user_keyword_vector[key] = plugin.name
                for key in plugin.plugin_object.admin_keyword_vector.keys():
                    self.admin_keyword_vector[key] = plugin.name
            except Exception as ex:
                print(ex)

    def on_message(self, mid, author_id, author_name, message, metadata):
        self.markAsDelivered(author_id, mid)
        self.markAsRead(author_id)

        #Check for self author
        if str(author_id) != str(self.uid):
            #trigger word
            if message.startswith("/bot"):
                words = message.split()
                if words[1] in self.user_keyword_vector.keys():
                    plugin = self.pluginManager.getPluginByName(self.user_keyword_vector[words[1]])
                    response = plugin.plugin_object.user_keyword_vector[words[1]](words)
                else:
                    response = "Unrecognized Command"

                #Send the response
                sent = self.send(author_id, response)
                if sent:
                     print("Sent", response, "to", author_id)
                else:
                     print("Failed", response, "to", author_id)
 
with open("config.yaml", "r") as stream:
    try:
        pair = yaml.load(stream)
        fb_user = pair['fb_user']
        fb_pass = pair['fb_pass']
    except yaml.YAMLError as e:
        print(e)

client = fbbot(fb_user, fb_pass)
client.listen()
