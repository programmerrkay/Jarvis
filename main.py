import serial

ser = serial.Serial("COM14", 9600, timeout=1)

def retrieveData():
    ser.write(b'113')
    ser.write(b'253')
    data = ser.readline().decode('ascii')
    return data

while (True):
    uInput = input ("Retrieve data? ")
    if uInput == "113":
        print (retrieveData())
    if uInput == "253":
        print(retrieveData())
    else:
        ser.write(b'253')
