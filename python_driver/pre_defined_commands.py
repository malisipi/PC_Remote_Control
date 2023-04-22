import subprocess;

def shutdown():
    subprocess.getoutput("poweroff");
    return "OFF "

def lock_screen():
    subprocess.getoutput("xdg-screensaver lock");
    #subprocess.getoutput("dbus-send --type=method_call --dest=org.gnome.ScreenSaver /org/gnome/ScreenSaver org.gnome.ScreenSaver.Lock");
    return "LOCK"