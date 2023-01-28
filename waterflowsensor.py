#!/usr/bin/python
import RPi.GPIO as GPIO
import time , sys
#import paho.mqtt.publish as publish

FLOW_SENSOR_GPIO = 13
#MQTT_SERVER = "192.168.1.220"

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR_GPIO, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global count
count = 0

def countPulse(channel):
   global count
   if start_counter == 1:
      count = count+1

GPIO.add_event_detect(FLOW_SENSOR_GPIO, GPIO.FALLING, callback=countPulse)
k=0
kk=[]
person=1
while True:
    try:
        start_counter = 1
        time.sleep(1)
        start_counter = 0
        flow = ((count * 1000) / 450)

        # Pulse frequency (Hz) = 7.5Q, Q is flow rate in L/min.
        print("The flow is rate : %.2f "% (flow))
        if flow > 0.00:
            i = int(start_counter)
            j = int(count)
            n = int(i+j)
            k += float(flow / n)
            #print("The water consumed by the person is : %.2f ml" % (k))
            #print("FLow Only",flow)
            print("Person",person," Drinking oer second",k)

        else:
            #print("The water consumed by the person is : %.2f" % (flow))
            print("Person",person,"Stopped the Tap and he drank water :",k)
            kk.append(k)
            k=0

            person+=1
        #publish.single("/Garden.Pi/WaterFlow", flow, hostname=MQTT_SERVER)
        count = 0
        time.sleep(1)
    except KeyboardInterrupt:
        print('\nprocess killed..!!')
        GPIO.cleanup()
        sys.exit()
