# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os, sys, time, fcntl, serial
if __name__ == '__main__':
        temp = 0.0
        lum = 0.0
        serial = serial.Serial()
        serial.port = '/dev/ttyUSB0'
        serial.baudrate = 9600
        serial.timeout = 1
        serial.writeTimeout = 1
        serial.open()
        fcntl.fcntl(sys.stdin, fcntl.F_SETFL, os.O_NONBLOCK)
        serial.writelines("[INFOS] Raspberry est ok")
        print "[INFOS] Raspberry is up and running"
        print "research xbee module, please wait..."

        def processData(Input):
                dataIn = Input.split('_')
                global temp
                temp = float(dataIn[0])
                global lum
                lum = float(dataIn[1])
        try:
                while True:
                        line = serial.readline().decode('utf-8')
                        if line:
                                print "[input] Arduino -> " + line
                                processData(line)
                                print "[INFOS] The temperature of the room is : " + temp + "C"
                                print "[INFOS] The brightness of the room is : " + lum + "%"
                                linin = sys.stdin.readline()
                                serial.writelines(linin)
                                if linin:
                                        print("[output] data Send -> " +linin)
                                        linin = false;
        except IOError:
                time.sleep(0.1)
        except KeyboardInterrupt:
                print("key interrupt", ERROR_TEXT)
                serial.writelines("[ERROR] RPI script down.")
        finally:
                print "script down, please reboot."
