import subprocess;
import platform;

platform_os = platform.system();
if(platform_os=="Windows"):
    import ctypes;


def shutdown():
    if(platform_os=="Windows"):
        subprocess.getoutput("shutdown /s /t 2");
    else:
        subprocess.getoutput("poweroff");
    
    return "OFF ";

def lock_screen():
    if(platform_os=="Windows"):
        ctypes.windll.user32.LockWorkStation();
    else:
        subprocess.getoutput("xdg-screensaver lock");
        #subprocess.getoutput("dbus-send --type=method_call --dest=org.gnome.ScreenSaver /org/gnome/ScreenSaver org.gnome.ScreenSaver.Lock");
    
    return "LOCK";