_Note: This is currently in alpha, and lacking many of the features I hope to implement. But it works._

# actionscreen
a cross-platform dashboard to quickly run actions on your computer from a tablet or other device
___


### Installation (?)
The simplest way to use actionscreen (in its current alpha form) is by downloading this repository,
adding things into your config file, and running the python file. This requires you to have
Python 3.6+ installed.

### How to use
1. Run the serverapp.py file on your computer where you want to run the actions.
(make sure to give accessibility permission on macOS if not running with sudo)
2. Open the web app on your tablet/device which you want to trigger actions with.

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
