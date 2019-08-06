import random as r
import os, sys, time, threading, multiprocessing

numberOfCores=multiprocessing.cpu_count()

def task(cmd):
    w=r.randint(2,5)
    time.sleep(w)
    return

# Run Multiple Thread
for i in range(16):
    cmd=str(i+1)
    msg="...Thread %s start...."%(cmd)
    print(msg)
    t = threading.Thread(target=task , args=(cmd,))
    t.start()
    while True:
        print(threading.activeCount())
        if threading.activeCount()-1 <= 6:
            break
        time.sleep(1)

# Waiting to finish the thread
while True:
  if threading.activeCount() == 1:
    break
  time.sleep(1)
  print ("Thread Left ... ",threading.activeCount() - 2)

print("\n...All Thread ends....")