from time import sleep
from datetime import datetime
from sh import gphoto2 as gp

import signal, os, subprocess, sys

def killgphoto2Process():
	os.killall('gvfsd-gphoto2', signal.SIGKILL)

shot_date = datetime.now().strftime("%Y%m%d")
shot_time = datetime.now().strftime("%Y%m%d %H:%M:%S")
picID = "shot"
triggerCommand = ["--trigger-capture"]

def captureImages(images, time):
    capturedImgs = 0
    sleepTime = float(images) / time
    print(images)
    print(time)
    print(float(sleepTime))
    while (capturedImgs < images):
        gp(triggerCommand)
        sleep(sleepTime)
        capturedImgs += 1        
    
    
def main():
    #killgphoto2Process()
    if(len(sys.argv) > 0): 
        print(len(sys.argv))
        print(sys.argv[1])
        captureImages(int(sys.argv[1]), float(sys.argv[2]))
    

if __name__ == '__main__':
   main()
