# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os, sys, time, fcntl, serial

def printLog(logType, logMsg, logOnline):
        logData = "[" + logType + "]: " + logMsg
        print(logData)
        if logOnline:
                serial.writelines(logData)
                pass
        pass

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
        printLog("INFOS", "Raspberry is up and running", True)
        printLog("INFOS", "research xbee module, please wait...", False)

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
                                printLog("INPUT", "Arduino -> " + line, False)
                                processData(line)
                                printLog("INFOS", "The temperature of the room is : " + temp + "C", False)
                                printLog("INFOS", "The luminosity of the room is : " + lum + "%", False)
                        linin = sys.stdin.readline()
                        serial.writelines(linin)
                        if linin:
                                print("[output] data Send -> " +linin)
                                linin = false;
        except IOError:
                time.sleep(0.1)
        except KeyboardInterrupt:
                print("key interrupt")
                serial.writelines("[ERROR] RPI script down.")
        finally:
                print("script down, please reboot.")
