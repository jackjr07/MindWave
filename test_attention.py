import time
import bluetooth
from mindwavemobile.MindwaveDataPoints import RawDataPoint
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader
import textwrap
import RPi.GPIO as GPIO
from mindwavemobile.MindwaveDataPoints import AttentionDataPoint

#led_section
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

if __name__ == '__main__':
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()
    if (mindwaveDataPointReader.isConnected()):
    
        
        while(True):
            dataPoint = mindwaveDataPointReader.readNextDataPoint()
            if dataPoint.__class__.__name__ == 'AttentionDataPoint':
               print(dataPoint)
               GPIO.output(17, True)
            elif dataPoint.__class__.__name__ == 'MeditationDataPoint':
                print(dataPoint)
                GPIO.output(27, True)
            
            #  if AttentionDataPoint.attentionValue == '0': 
                   # GPIO.output(17, False)    
                   # print('OFF')
               # else:
                #    GPIO.output(17, True)
                 #   print('ON')

    else:
        print((textwrap.dedent("""\
                Exiting because the program could not connect
                to the Mindwave Mobile device.""").replace("\n", " ")))
