#!/usr/bin/env python3

import json, subprocess, time, os, sys, random

def random_sign():

    if random.randint(0,1) == 0: return -1
    else: return 1

while True:
   
    
    #vector = json.loads(data)
    x = str(random.randint(1,5)*100 * random_sign())
    y = str(random.randint(1,10)*100 * random_sign())
   # string = str(vector)
    data = ' {"x" : "'+x+'", "y": "'+y+'", "z": "0", "status" : "down", "QoS" : "bad"} '
    #string2 = '"' + string +'"'

    print(data)
    #time.sleep(0.1)


