from sys import exit as exitapp
from json import load
from time import sleep

from flask import Flask
from flask import render_template
from keyboard import press_and_release
from requests import get
from webbrowser import open as openurl

app = Flask(__name__)

CONFIG_FILE = ".actionscreen_config"
VERSION = "alpha.1"

# update check
site_url = "https://blobbybilb.github.io/actionscreen/"
update_status = get(f"{site_url}update_check/{VERSION}.html")
if update_status != 'fine':
    if update_status == 'update':
        openurl(f"{site_url}errors/update_error.html")
    else:
        openurl(f"{site_url}errors/other_error.html")
    exitapp()

try:
    open(CONFIG_FILE, "r").close()
except FileNotFoundError:
    open(CONFIG_FILE, "w+").close()

with open(CONFIG_FILE) as config_file:
    json_data = load(config_file)
    password = json_data["password"]
    shortcuts = json_data["shortcuts"]


@app.route('/<passwd>/<platform>/<action_type>/<action>/')
def request_handler(passwd, platform, action_type, action):
    if passwd != password:
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


@app.route('/<screen>/<columns>/')
def check_page(screen, columns):
    with open('.actionscreen_screens') as screen_file:
        screen_data = load(screen_file)
        screen_config = screen_data[screen]["screen_config"]
        screen_color = screen_data[screen]["screen_color"]
    try:
        _ = int(columns)
    except ValueError:
        return f'{columns} is not an integer'
    rows_to_display = (((len(screen_config)) // int(columns)) + 1) * '14vh '
    columns_to_display = int(columns) * 'auto '
    return render_template('/main.html/', screen_config=screen_config, screen_color=screen_color, screen_name=screen,
                           rows_to_display=rows_to_display, columns_to_display=columns_to_display)


app.run(host='0.0.0.0', port=5090, debug=True)
