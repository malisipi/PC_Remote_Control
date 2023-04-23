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
import user_defined_commands as cm;
import port_finder as pf;
import platform;

debug_mode = False;
platform_os = platform.system();

if(platform_os=="Windows"):
    from ctypes import WinDLL;
    user32 = WinDLL("user32");

def arduino_write(text):
    global arduino;
    if(debug_mode): print("DEBUG: arduino_write: " + text)
    arduino.write(text.encode("utf-8"));

def arduino_read():
    global arduino;
    readed_value = arduino.read_until();
    if(debug_mode): print("DEBUG: arduino_read: " + readed_value);
    return readed_value;

def send_key(key_code):
    if(platform_os=="Windows"):
        user32.keybd_event(key_code, 0, 0, 0);
        user32.keybd_event(key_code, 0, 2, 0);
    else:
        pass;

def get_volume():
    if(platform_os=="Windows"):
        return "--";
    else:
        return subprocess.getoutput("pactl get-sink-volume @DEFAULT_SINK@ | awk '{print $5}' | grep %").replace("%","");

def change_volume(sign, volume):
    if(platform_os=="Windows"):
        if(sign=="+"):
            key_code = 0xAF;
        else:
            key_code = 0xAE;

        for _ in range(0, int(volume/2)):
            send_key(key_code);
    else:
        subprocess.getoutput(f"pactl set-sink-volume @DEFAULT_SINK@ {sign}{volume}%");

def player_play_pause():
    if(platform_os=="Windows"):
        send_key(0xB3);
    else:
        subprocess.getoutput("playerctl play-pause");

def player_next():
    if(platform_os=="Windows"):
        send_key(0xB0);
    else:
        subprocess.getoutput("playerctl next");

def player_prev():
    if(platform_os=="Windows"):
        send_key(0xB1);
    else:
        subprocess.getoutput("playerctl previous");

latest_time="----";

arduino = serial.Serial(port=pf.find_port(platform_os), baudrate=9600, timeout=0.05);
time.sleep(2);

while(True):
    new_time = datetime.now().strftime("%H%M");
    if(new_time != latest_time):
        latest_time = new_time;
        arduino_write(latest_time);
    match(arduino_read().decode("utf-8").replace("\r\n","")):
        case "#VUP":
            change_volume("+", 10);
            arduino_write(f"V{get_volume()}");
        case "#VDN":
            change_volume("-", 10);
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
