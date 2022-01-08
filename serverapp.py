# from sys import exit as exitapp
from json import load
from time import sleep

from flask import Flask
from flask import render_template
from flask import request
from keyboard import press_and_release
from keyboard import write

# from requests import get
# from webbrowser import open as openurl

app = Flask(__name__)

CONFIG_FILE = ".actionscreen/config"
VERSION = "alpha.3"

# update check
# disabled during alpha, TODO re-enable later
# site_url = "https://blobbybilb.github.io/actionscreen/"
# try:
#     update_status = get(f"{site_url}update_check/{VERSION}.html").text
#     if 'fine' not in update_status:
#         if 'update' in update_status:
#             openurl(f"{site_url}errors/update_error.html")
#             print('There is an update available!\
#                 Go to the github repository for actionscreen to update.')
#             if 'important' in update_status:
#                 openurl(f"{site_url}errors/big_update_error.html")
#                 print('THERE IS AN IMPORTANT UPDATE AVAILABLE!\
#                     You should update immediately.')
#                 exitapp()
#         else:
#             openurl(f"{site_url}errors/other_error.html")
#             print('There was an error checking for actionscreen update.')
# except:
#     openurl(f"{site_url}errors/other_error.html")
#     print('There was an error checking for actionscreen update.')

try:
    open(CONFIG_FILE, "r").close()
except FileNotFoundError:
    open(CONFIG_FILE, "w+").close()

with open(CONFIG_FILE) as config_file:
    json_data = load(config_file)
    password = json_data["password"]
    shortcuts = json_data["shortcuts"]


@app.route("/<passwd>/<platform>/<action_type>/<action>/")
def request_handler(passwd, platform, action_type, action):
    if passwd != password:
        sleep(1)
        return "incorrect password"
    try:
        if action_type == "keyboard_shortcut":
            press_and_release(shortcuts[platform][action_type][action])
        elif action_type == "sequence":
            for part in shortcuts[platform][action_type][action]:
                # if part[0] == 'keyboard_shortcut': # instead change this to a prefix for other types
                press_and_release(part[1])
        elif action_type == "write_text":
            write(shortcuts[platform][action_type][action])

    except KeyError:
        try:
            _ = shortcuts[platform][action_type]
            try:
                _ = shortcuts[platform]
            except KeyError:
                return "invalid platform"
        except KeyError:
            return "invalid action type"
        return "invalid action"
    return "success"


@app.route("/<screen>/<columns>/")
def check_page(screen, columns):
    with open(".actionscreen/screens/" + screen) as screen_file:
        screen_data = load(screen_file)
        screen_config = screen_data["screen_config"]
        screen_color = screen_data["screen_color"]
    try:
        _ = int(columns)
    except ValueError:
        return f"{columns} is not an integer"

    rows_to_display = (((len(screen_config)) // int(columns)) + 1) * "14vh "
    columns_to_display = int(columns) * "auto "
    return render_template(
        "/main.html/",
        screen_config=screen_config,
        screen_color=screen_color,
        screen_name=screen,
        rows_to_display=rows_to_display,
        columns_to_display=columns_to_display,
        server_ip=request.host.replace(":5090", ""),
    )


@app.route(
    "/saveconfig/", methods=["POST"]
)  # TODO give freindly message on non-POST request
def save_config():
    if not request.host.startswith(request.remote_addr):
        return "This must be done from host computer!"
    # TODO save config and update variable
    # json_data["password"] = request.form["password"]

    return request.form


@app.route("/config/")
def edit_config():
    if not request.host.startswith(request.remote_addr):
        return "This must be done from host computer!"
    platforms_count = len(json_data["shortcuts"])
    config_js_file = open("config.js", "r").read()
    return render_template(
        "/config.html/",
        json_data=json_data,
        platforms_count=platforms_count,
        config_js=config_js_file,
    )


@app.route("/")
def screen_chooser():
    return render_template("/screen_chooser.html/")


app.run(host="0.0.0.0", port=5090, debug=True)

# TODO screen chooser
# TODO guide
# TODO alpha notes on README (broken/expect)
# TODO rename config -> config.json, and main_screen -> main_screen.json and fix in code
# TODO remove platforms thing to simplify
