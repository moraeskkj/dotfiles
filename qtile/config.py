#### akames config file ###
### PATHS ###
# mouse cfg's -> qtile/modules/mouse.py
# groups / workspaces cfg's -> qtile/modules/groups.py
# keybinds cfg's -> qtile/modules/keys.py
# layouts cfg's -> qtile/modules/layouts.py
# bar,screen, widgets -> qtile/modules/screen.py

### IMPORTS ###
from libqtile import hook
import subprocess
import os
from modules.groups import groups
from modules.keys import keys, mod, shift
from modules.layouts import layouts, floating_layout
from modules.screens import screens, main_screen_bar, widget_defaults

dgroups_key_binder = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
auto_minimize = False
wmname = "qtile"

#starting cools things 
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/scripts/autostart.sh"])
