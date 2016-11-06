import time
import serial

ser = serial.Serial('COM3', 9600, timeout=0.1)
c = 0

buffer = ""
while True:
    print "Reading ..."
    line = ser.readline()
    print "Read done"
    if len(line) > 0:
    #     pos = buffer.find("\n")
        print line
    #     for c in line:
    #         print "{:02x}".format(ord(c))
    #     if pos >= 0:
    #         buffer += line[:pos]
    #         print buffer
    #         if "exit" in line:
    #             break
    #         buffer = line[pos+1:]
    #         c += 1
    #         if c > 10:
    #             break
    time.sleep(0.1)
    print "Sleeping ..."
print "Finished"
