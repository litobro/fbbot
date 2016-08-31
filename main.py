import fbchat
import yaml

with open("config.yaml", "r") as stream:
    try:
        pair = yaml.load(stream)
        fb_user = pair['fb_user']
        fb_pass = pair['fb_pass']
    except yaml.YAMLError as e:
        print(e)

client = fbchat.Client(fb_user, fb_pass)
