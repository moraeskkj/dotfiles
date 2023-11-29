from libqtile import bar 
from libqtile.config import Screen 
from qtile_extras import widget 
from modules.widgets import * 
from utils.settings import colors 

### WIDGETS // BAR ###
# ~/.config/qtile/modules/screens.py

color_alert = '#ee9900'
color_frame = '#808080'

widget_defaults = dict(
    font="FiraCode Nerd Font",    
    fontsize=14,
    padding=2,
)

extension_defaults = widget_defaults.copy()

def create_bar(extra_bar = False):
    """Create top bar, defined as function to allow duplication in other monitors"""
    return bar.Bar(
        [
            gen_separator(25,50), ##error here
            w_bar_icon,
            w_window_name,
            gen_spacer(),
            *gen_groupbox(),
            gen_spacer(),
            *((w_systray,) if not extra_bar else ()),
            gen_separator(15,50),
            vol_icon, w_vol,
            gen_separator(5,50),
            network_icon, w_network,
            gen_separator(11,50),
            clock_icon, w_clock,
            gen_separator(25,50),
        ],
        36,
        margin=[0, 0, 4, 0],
        background="#000000", opacity=0.8,
    )

main_screen_bar = create_bar()

screens = [
    Screen(
        top=main_screen_bar,
        bottom=bar.Gap(4),
        left=bar.Gap(4),
        right=bar.Gap(4),
    ),
]

