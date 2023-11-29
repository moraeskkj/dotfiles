from libqtile import qtile, lazy
from qtile_extras import widget
from utils.settings import colors, network_if , workspace_names

group_box_settings = {
    "active": colors[18],
    "rounded": True,
    "block_highlight_text_color": colors[18],
    "this_current_screen_border": colors[18],
    "this_screen_border": colors[18],
    "urgent_border": colors[3],
    "other_current_screen_border": colors[22],
    "other_screen_border": colors[22], 
    "highlight_color": colors[13],
    "inactive": colors[14],
    "foreground": colors[21],
    "borderwidth": 2,
    "disable_drag": True,
    "fontsize": 14,
    "highlight_method": "line",
    "padding_x": 7,
    "padding_y": 16,
}

def toggle_maximize():
    lazy.window.toggle_maximize()

def parse_window_name(text):
    """Simplifies the names of a few windows, to be displayed in the bar"""
    target_names = [
        "Mozilla Firefox",
        "Visual Studio Code",
        "Discord",
    ]
    return next(filter(lambda name: name in text, target_names), text)

def gen_groupbox():
    return (
        widget.GroupBox(  # firefox
            font="Font Awesome 6 Brands",
            visible_groups=[workspace_names[0]],
            **group_box_settings,
        ),
        widget.GroupBox(  # dev, term
            font="Font Awesome 6 Free Solid",
            visible_groups=[workspace_names[1], workspace_names[2]],
            **group_box_settings,
        ),
        widget.GroupBox(  # discord, spotify
            font="Font Awesome 6 Brands",
            visible_groups=[workspace_names[3], workspace_names[4]],
            **group_box_settings,
        ),
        widget.GroupBox(  # notes, brave
            font="Font Awesome 6 Free Solid",
            visible_groups=[workspace_names[5], workspace_names[6]],
            **group_box_settings,
        ),
        widget.GroupBox(  # virt, ferdium, gaming
            font="Font Awesome 6 Free Solid",
            visible_groups=[workspace_names[7], workspace_names[8], workspace_names[9]],
            **group_box_settings,
        ),
    )

def gen_spacer():
    return widget.Spacer()

def gen_separator(padding: int, size_percent: int):
    return widget.Sep(
        linewidth=0,
        padding=padding,
        size_percent=size_percent,
    )

w_bar_icon = widget.TextBox(
    text="󰣇 ",
    foreground=colors[18],
    font="Iosevka Nerd Font",
    fontsize=22,
)

w_window_name = widget.WindowName(
    padding=8,
    foreground=colors[18],
    empty_group_string="Desktop",
    max_chars=18,
    parse_text=parse_window_name,
    mouse_callbacks={"Button1": toggle_maximize},
)

w_systray = widget.Systray(
    padding=7,
)

#vol_icon = widget.TextBox(
#    text=" ",
#    fontsize=17,
#)
#
#w_vol = widget.PulseVolume(
#    limit_max_volume="True",
#    padding=8,
#)

cpu_icon = widget.TextBox(
    text = " ",
    fontsize=17,
)

w_cpu = widget.CPU(
    format='{load_percent:5.2f}%',
    padding=7,
)

checkupdates_icon = widget.TextBox(
    text = "⟳ ",
    fontsize= 18,
)

w_checkupdates = widget.CheckUpdates(
    distro = "Arch_checkupdates",
    update_interval = 2000,
    colour_have_updates = colors[3],
    no_update_string='No updates',
    display_format = "{updates} Updates",
    execute= 'alacritty -e sudo paru -Syu',
)

network_icon = widget.TextBox(
    text="󰍛 ",
    fontsize=18,
)

w_network = widget.Memory(
    measure_mem='G',
    format='{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}',
    padding=1,
)

clock_icon = widget.TextBox(
    text="󰥔 ",
    fontsize=17,
)

w_clock = widget.Clock(
    format="%d %b | %H:%M",
)
