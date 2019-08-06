# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:48:17 2019

@author: Dawar
"""
import random as r
import os, sys, time, threading, multiprocessing

numberOfCores=6
fc=open('final.csv','w')

def task(cmd):
    # File Processing Task
    fr=open('C:\\Users\\God\\Desktop\\python wrkshop\\numpy_and_threading\\input\\'+cmd)
    fw=open('C:\\Users\\God\\Desktop\\python wrkshop\\numpy_and_threading\\output\\'+cmd,'w')
    for line in fr:
        fw.write(line.upper())
    fr.close()
    fw.close()

# Run Multiple Thread
start_time = time.time()
files=os.listdir("C:\\Users\\God\\Desktop\\python wrkshop\\numpy_and_threading\\input")
for f in files:
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
  if threading.activeCount() == 6:
    break
  time.sleep(1)
  print ("Thread Left ... ",threading.activeCount())

print("\n...All Thread ends....")
print("--- %s seconds ---" % (time.time() - start_time))
fc.write(str(time.time() - start_time))
fc.close()

