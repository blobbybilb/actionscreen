_Note: This is currently in alpha, and lacking many of the features I hope to implement. But it works._

# actionscreen
a cross-platform dashboard to quickly run actions on your computer from a tablet or other device
___


### Installation (?)
The simplest way to use actionscreen (in its current alpha form) is by downloading this repository, adding things into your config file, and running the python file. This requires you to have Python 3.6+ installed. See steps below.

### How to use

Simply follow these steps.

1. If you haven't already, install Python 3. Go to the Python website (python.org) and get the latest version of Python 3 for your platform, and install it. Leaving the default options should be fine. Instructions for installing Python are available on the internet if you look it up!

2. Open up a terminal/command prompt.
  - On macOS, open Terminal.
  - On Windows, open Command Prompt, Windows Terminal, or PowerShell.
  - On GNU/Linux, you should know how to open a terminal by now ;).


3. Install dependencies. Copy and paste this command into your terminal, and press enter.
  - `python3 -m pip install keyboard flask`
  - If that doesn't work: `python -m pip install keyboard flask`


4. Clone this repository or download the zip file by pressing the green "Code 🔻" button.
  - `git clone https://github.com/blobbybilb/actionscreen`


5. Unzip the folder if needed, then run the `serverapp.py` file inside:
  - `cd actionscreen` to switch to the app folder.
  - On Windows, `python3 serverapp.py` or `python serverapp.py`
  - Others, `sudo python3 serverapp.py`
  - Note that you may not need to run it with sudo, but on macOS you will need to give the terminal accessibility permissions in order to use keyboard shortcuts.


6. Open the web app on your tablet/device which you want to trigger actions with by going to the URL displayed in the terminal. You should be ready to go!


### Docs?
uhh... coming soon... hopefully

### Features
* run keyboard shortcuts
* open apps (coming very soon)
* terminal commands
* run sequences
* **lightweight** on both client and server
* **secure**
  * rate limited (unlike many similar tools)
    * on incorrect password requests only, so it doesn't affect performance
  * password protected
  * configuration can only be changed from host
* client runs in browser
  * mobile devices
  * anything that has a non-ancient browser (tested on safari, chrome, firefox)
* server is cross-platform, run it anywhere python runs
  * windows (32-bit/i386 and 64-bit/ARM64)
  * macOS (Intel and Apple Silicon)
  * linux
  * and more!
* add your own (by editing json)
* free and open source
* easy to set up
* simple, clean, very customisable UI
  * change button colors
  * add images
  * change background color

#### To-do
* [ ] GUI for configuring actions
* [ ] open apps
* [ ] images for actions
* [ ] multiple screens
  * [ ] screen chooser screen
* [ ] switch column amount
* [ ] get IP by itself?
* [ ] logging
* [ ] mouse clicks
* [ ] blacklist/whitelist IPs
* [ ] wait in sequences
