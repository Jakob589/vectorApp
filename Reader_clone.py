import json, subprocess, time, os, sys, random

while True:
   
    data = '{"x": "0", "y": "0", "z": "0", "status": "down", "QoS": "bad"}'
    vector = json.loads(data)
    vector["x"] = random.randint(1,5)*100
    vector["y"] = random.randint(1,10)*100
    print(vector)
    time.sleep(0.1)

