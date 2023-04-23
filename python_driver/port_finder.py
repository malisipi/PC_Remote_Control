import serial.tools.list_ports;

def find_port(platform_os):
    if(platform_os=="Windows"):
        ports = list(serial.tools.list_ports.comports());
        for port in ports:
            if("CH340" in port[1]):
                return port[0];
    else:
        return "/dev/ttyUSB0";