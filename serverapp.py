from sys import exit as exitapp
from json import load
from time import sleep

from flask import Flask
from keyboard import press_and_release
from requests import get
from webbrowser import open as openurl

app = Flask(__name__)

CONFIG_FILE = ".actionscreen_config"
VERSION = "alpha.1"

# update check
# update_status = get(f"https://blobbybilb.github.io/actionscreen/update_check/{VERSION}.html")
# if update_status != 'fine':
#     if update_status == 'update':
#         openurl("https://blobbybilb.github.io/actionscreen/update_error.html")  # TODO actually make this
#     else:
#         openurl("https://blobbybilb.github.io/actionscreen/other_error.html")  # TODO actually make this as well
#     exitapp()

try:
    open(CONFIG_FILE, "r").close()
except FileNotFoundError:
    open(CONFIG_FILE, "w+").close()

with open(CONFIG_FILE) as config_file:
    json_data = load(config_file)
    user_pass = json_data["user_password"]
    shortcuts = json_data["shortcuts"]


@app.route('/<passwd>/<platform>/<action_type>/<action>/')
def request_handler(passwd, platform, action_type, action):
    if passwd != user_pass:
        sleep(1)
        return 'incorrect password'
    try:
        if action_type == 'keyboard_shortcut':
            press_and_release(shortcuts[platform][action_type][action])
        elif action_type == 'keyboard_shortcut_sequence':
            for part in shortcuts[platform][action_type][action]:
                press_and_release(part)
    except KeyError:
        try:
            _ = shortcuts[platform][action_type]
            try:
                _ = shortcuts[platform]
            except KeyError:
                return 'invalid platform'
        except KeyError:
            return 'invalid action type'
        return 'invalid action'
    return 'success'


@app.route('/')
def check_page():
    return 'actionscreen'  # to verify that it's a valid server


app.run(host='0.0.0.0', port=5090, debug=True)
