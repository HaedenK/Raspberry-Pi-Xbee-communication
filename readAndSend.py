
#!/usr/bin/env python
import os, sys, time, fcntl, serial
if __name__ == '__main__':
        serial = serial.Serial()
        serial.port = '/dev/ttyUSB0'
        serial.baudrate = 9600
        serial.timeout = 1
        serial.writeTimeout = 1
        serial.open()
        fcntl.fcntl(sys.stdin, fcntl.F_SETFL, os.O_NONBLOCK)
        serial.writelines("RPi 1 est ok")
        print "RPi 1 est ok"
        print "Lancement"
        try:
                while True:
                        line = serial.readline().decode('utf-8')
                        if line:
                                print line
                        try:
                                line = sys.stdin.readline()
                                serial.writelines(line)
                        except IOError:
                                time.sleep(0.1)
                                continue
        except KeyboardInterrupt:
                print("key interrupt", ERROR_TEXT)
                serial.writelines("RPI DOWN DOWN DOWN")
        finally:
                print "nice"
