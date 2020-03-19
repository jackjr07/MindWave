# ECE 212 Mindwave controlled wheelchair

# Basic imports
import time
import bluetooth
import serial
import textwrap
import os

# Mindwave centered imports
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader
from mindwavemobile.MindwaveDataPoints import RawDataPoint
from mindwavemobile.MindwaveDataPoints import AttentionDataPoint
from mindwavemobile.MindwaveDataPoints import BlinkDataPoint
import mindwavemobile

if __name__ == '__main__':
    # Initialize the bluetooth software serial port
    ser = serial.Serial(
        port     = "/dev/rfcomm3",
        baudrate = 38400,
        bytesize = serial.EIGHTBITS,
       parity   = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        timeout  = 1,
        xonxoff  = False,
        rtscts   = False,
        dsrdtr   = False,
        writeTimeout = 2 ) 

    # Initialize and start the Mindwave datapoint reader
mindwaveDataPointReader = MindwaveDataPointReader()
mindwaveDataPointReader.start()

    # Check if the Mindwave is connected
if(mindwaveDataPointReader.isConnected()):

    blinkState = 1
        
    while(True):

            # Read in a new set of EEG data
            dataPoint = mindwaveDataPointReader.readNextDataPoint()
            if dataPoint.__class__.__name__ == 'AttentionDataPoint':

                if(dataPoint.attentionValue >= 40):
                    
                    if blinkState == 1:
#                         print('Forward')
                        ser.write(b'f')

                    elif blinkState == -1:
#                         print('Backward')
                        ser.write(b'b')

                else:
                    ser.write(b'n')
#                     print('Blank')   
            if dataPoint.__class__.__name__ == 'EEGPowersDataPoint':

                if dataPoint.delta > 1000000:
                    if blinkState == 1:
                        blinkState = -1
                    else:
                        blinkState = 1

            if not dataPoint.__class__ is RawDataPoint:
                print(dataPoint);


            # os.system('cls' if os.name == 'nt' else 'clear')

            else:
                print((textwrap.dedent(
                """\Exiting because the program could not connect to the
                Mindwave Mobile device""").replace("\n", " ")))
