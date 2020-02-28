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


if __name__ == '__main__':
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()
    if (mindwaveDataPointReader.isConnected()):
    
        
        while(True):
            dataPoint = mindwaveDataPointReader.readNextDataPoint()
            if (not dataPoint.__class__ is RawDataPoint):
                print(dataPoint)
                GPIO.output(17, True)
                time.sleep(1)
                GPIO.output(17, False)
                time.sleep(1)
    else:
        print((textwrap.dedent("""\
            Exiting because the program could not connect
            to the Mindwave Mobile device.""").replace("\n", " ")))
        GPIO.out(17, False)

