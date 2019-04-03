#!/usr/bin/python3

import sys, os
import numpy as np
import scipy
import time

import h5py

f = h5py.File("mytestfile.hdf5", "w")
dset = f.create_dataset("mydataset", (100,), dtype='i')
print ('dset = ' % dset)

'''

# write tkinter as Tkinter to be Python 2.x compatible
from tkinter import *

print ('Start of shortTest...')

def hello(event):
    print("Single Click, Button-l") 
def quit(event):                           
    print("Double Click, so let's stop") 

widget = Button(None, text='Mouse Clicks')
# widget.pack()
# widget.bind('<Button-1>', hello)
# widget.bind('<Double-1>', quit) 
# widget.mainloop()

Nsteps = 3
for step in range(Nsteps):
    print ('step = %d' % step)
    time.sleep(1.)
    try:
       newVal=raw_input('New value = ')
       newVal = float(newVal)
       print ('newVal = %f' % newVal)
    except ValueError:
        print('No input')

print ('End of shortTest...')
'''
sys.exit()
