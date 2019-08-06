import random as r
import os, sys, time, threading, multiprocessing
from PIL import Image
import glob
from io import BytesIO

numberOfCores=multiprocessing.cpu_count()

def task(cmd):
    img = Image.open('C:\\Users\\God\\Desktop\\downloads\\Dog\\'+cmd)
    basewidth = img.width/2
    baseheight = img.height/2
    img = img.resize((int(basewidth), int(baseheight)), Image.ANTIALIAS)
    img = img.convert('RGB')
    img.save('C:\\Users\\God\\Desktop\\downloads1\\Dog\\'+cmd+'.jpg')
    return

# Run Multiple Thread
start_time = time.time()
root_dir=os.listdir("C:\\Users\\God\\Desktop\\downloads\\Dog")
for f in root_dir:
    cmd=f
    msg="...Thread %s start...."%(cmd)
    print(msg)
    t = threading.Thread(target=task , args=(cmd,))
    t.start()
    while True:
        if threading.activeCount()-1 <= numberOfCores:
            break
        time.sleep(1)

# Waiting to finish the thread
while True:
  if threading.activeCount() == 2:
    break
  time.sleep(1)
  print ("Thread Left ... ",threading.activeCount() - 2)

print("\n...All Thread ends....")
