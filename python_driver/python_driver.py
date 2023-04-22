#!/bin/python3

(((( ((((      ((((
(  ( (         (
(((( )    )))) )
)    )    )    )
)    )))) )    )))); # by malisipi

import serial;
import time;
from datetime import datetime;
import subprocess;
import user_defined_commands as cm

debug_mode = False;

def arduino_write(text):
    global arduino;
    if(debug_mode): print("DEBUG: arduino_write: " + text)
    arduino.write(text.encode("utf-8"));

def arduino_read():
    global arduino;
    readed_value = arduino.read_until();
    if(debug_mode): print("DEBUG: arduino_read: " + readed_value);
    return readed_value;

def get_volume():
    return subprocess.getoutput("pactl get-sink-volume @DEFAULT_SINK@ | awk '{print $5}' | grep %").replace("%","");

def change_volume(volume):
    subprocess.getoutput(f"pactl set-sink-volume @DEFAULT_SINK@ {volume}%");

def player_play_pause():
    subprocess.getoutput("playerctl play-pause");

def player_next():
    subprocess.getoutput("playerctl next");

def player_prev():
    subprocess.getoutput("playerctl previous");

latest_time="----";

arduino = serial.Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=0.05);
time.sleep(2);

while(True):
    new_time = datetime.now().strftime("%H%M");
    if(new_time != latest_time):
        latest_time = new_time;
        arduino_write(latest_time);
    match(arduino_read().decode("utf-8").replace("\r\n","")):
        case "#VUP":
            change_volume("+10");
            arduino_write(f"V{get_volume()}");
        case "#VDN":
            change_volume("-10");
            arduino_write(f"V{get_volume()}");
        case "#PLY":
            player_play_pause();
            arduino_write("PLAY");
        case "#NXT":
            player_next();
            arduino_write("NEXT");
        case "#PRV":
            player_prev();
            arduino_write("PREV");
        case "#C01":
            arduino_write(cm.command_01());
        case "#C02":
            arduino_write(cm.command_02());
        case "#C03":
            arduino_write(cm.command_03());
        case "#C04":
            arduino_write(cm.command_04());
        case "#C05":
            arduino_write(cm.command_05());
        case "#C06":
            arduino_write(cm.command_06());
        case "#C07":
            arduino_write(cm.command_07());
        case "#C08":
            arduino_write(cm.command_08());
        case "#C09":
            arduino_write(cm.command_09());
        case "#C10":
            arduino_write(cm.command_10());
        case "#C11":
            arduino_write(cm.command_11());
        case "#C12":
            arduino_write(cm.command_12());