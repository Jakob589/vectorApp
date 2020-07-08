from mpl_toolkits.mplot3d import Axes3D
import json
import matplotlib.pyplot as plt
import time
import random
import matplotlib.animation as animation
import subprocess 
import json, subprocess, time, os, sys
from multiprocessing import Process, Queue


def collect_data(q):
    cmd = "echo 192.168.1.60:9090 | java -jar /Users/jakob/Documents/ijs/eBottle/uhf-acc-read/build/UhfRfidReader.jar"

    p = subprocess.Popen(cmd,
                     shell=True,
                     bufsize=64,
                     stdout=subprocess.PIPE)

    for line in p.stdout:
        
        raw_data = str(line.rstrip())
        
        data = raw_data[2:(len(raw_data) -1)]
        
        if data == "1|1|2,0006&3,010005": data = '{"x": "0", "y": "0", "z": "0", "status": "down", "QoS": "bad"}'
        vector = json.loads(data)
        #print(data)
        print(vector)
        p.stdout.flush()


    while True:
        data = '{"x": "0", "y": "0", "z": "0", "status": "down", "QoS": "bad"}'
        vector = json.loads(data)
        vector["x"] = random.randint(1,5)*100
        vector["y"] = random.randint(1,10)*100
        q.put(vector)
        
def animate_data(q):

    origin = [0,0,0]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    def animate(i):
        
        vectorMain = q.get()
        #print(vectorMain)
        x = int(vectorMain["x"])/10000
        y = int(vectorMain["y"])/10000
        z = int(vectorMain["z"])/10000
   
        ax.clear()
        p0 = [x,y,z]
        p1 = [0, 0, 0]
        p2 = [0, 0, 0]
        X, Y, Z = zip(origin,origin,origin) 
        U, V, W = zip(p0,p1,p2)
        ax.quiver(X,Y,Z,U,V,W,arrow_length_ratio=0.1)

    ani = animation.FuncAnimation(fig, animate,1)
    plt.show()    


if __name__ == '__main__':
    
    q = Queue()
    p = Process(target=collect_data, args=(q,))
    pAni = Process(target=animate_data, args=(q,))
    p.start() 
    pAni.start()
    p.join()

