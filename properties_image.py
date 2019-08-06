# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:33:11 2019

@author: Dawar
"""

import cv2
import numpy as np

from os import listdir
from os.path import isfile, join
mypath='C:/Users/God/Desktop/python wrkshop/google_images/downloads/Car'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for i in onlyfiles:
    path = 'C:/Users/God/Desktop/python wrkshop/google_images/downloads/Car/' + i

    # read image into matrix.
    m =  cv2.imread(path)
    
    # get image properties.
    h,w,bpp = np.shape(m)
    
    # print image properties.
    print(f'Properties of image {i}: ')
    print ("width: " + str(w))
    print ("height: " + str(h))
    print ("bpp: " + str(bpp))