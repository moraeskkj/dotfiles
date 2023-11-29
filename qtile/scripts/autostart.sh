#!/bin/bash

export TERM=xterm-256color

#resize screen
xrandr --output Virtual1 --mode 1360x768

#load a aleatory wallpaper if you want
wall=$(find ~/pics/wallpapers -type f -name "*.jpg" -o -name "*.jpg" | shuf -n 1)
feh --bg-scale $wall

#set colors scheme

wal -c
wal -i $wall

#autostart apps

picom -b &
#discord &

# don't touch it
#notify-send -t 8000 -u normal --icon=/home/flame/.config/qtile/assets/waifu_coffe.png "uuuuh?" "welcome back sir! how are u?"
