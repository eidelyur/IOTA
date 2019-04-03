#====================================================================
#
# YuE comment (03/26/19):
#
# Script realize data processing of IOTA simulation (*.h5 files). 
#
#====================================================================
#
# Import and setup IPython magics:
#
%matplotlib inline
%reload_ext autoreload
%autoreload 2
import sys, os
import numpy as np
import scipy
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import gridspec
import h5py

workDir = '/home/vagrant/jupyter/eidelyur/iota/example_run/'

fileLS = os.popen('ls').readlines()
numbFiles = len(fileLS)
# print ('numbFiles = %d, fileLS = %s' % (numbFiles,fileLS))
fileList = [' ']*numbFiles
numb_h5 = 0
numb_basic = 0
numb_particles = 0
numb_full2 = 0
k = 0
for line in fileLS:
    if line[0:-1].count('.h5') == 1:
        fileList[k] = line[0:-1]
        if fileList[k].count('basic') == 1:
            numb_basic += 1
        if fileList[k].count('particles') == 1:
            numb_particles += 1
        if fileList[k].count('full2') == 1:
            numb_full2 += 1
        k += 1
        numb_h5 += 1
print 'numb_h5 = ', numb_h5,'; "basic" = ',numb_basic,', "full2" = ', \
numb_full2,', "particles" = ',numb_particles        
# fileList[0:numb_h5]

#
# Input fileName:
#
existFileFlag = 0
print ('Files: %s' % fileList[0:numb_h5])
while existFileFlag == 0:
    crrntName = raw_input("\nSelect a name of file: ")
    print "Your file is: ", crrntName
    for name in fileList[0:numb_h5]:
#        print('name = ', name, ', check = ',crrntName)            
        if crrntName == name:
            existFileFlag = 1
            break
#    print('existFileFlag == ', existFileFlag)            
    if existFileFlag == 1:
        print ('File is found!')
    else:
        print ('File does not exist! Try again!')

# Files like 'particles_strct*_*.h5':
#
nameFile = workDir + crrntName
print ('nameFile = ',nameFile)
# nameFile = workDir + 'particles_strct0_0000.h5'
# nameFile = workDir + 'basic_strct0.h5'
# nameFile = workDir + 'full2_strct0.h5'
fp0 = h5py.File(nameFile,'r')
# print ('fp0 =', fp0)
fp0_len = len(fp0)              # = 7
namesAttr = [' ']*fp0_len
fp0_keys = fp0.keys()
# print ('fp0_keys = ',fp0_keys)
k = 0
for name in fp0_keys:
    shapeName = fp0[name].shape
    namesAttr[k] = str(name)
    stringHelp = str(shapeName)[1:len(str(shapeName))-1] 
    countCommas = stringHelp.count(',')
#    print ('For name %s shape = %s => %s; commas = %d' % (name,namesAttr[k],stringHelp,countCommas))
    k += 1
    if countCommas == 0:
        dimnsn = 0
    else:
        numbIndx = stringHelp.split(',')
        dimnsn = len(numbIndx)
        if numbIndx[dimnsn-1] == '':
            dimnsn = dimnsn-1
            numbIndx = numbIndx[0:dimnsn]
#        print ('numbIndx = ', numbIndx)
#    print ('dimnsn = ',dimnsn) 
# Results:
# For name charge shape = ()
# For name mass shape = ()
# For name particles shape = (10000, 7)
# For name pz shape = ()
# For name rep shape = ()
# For name s_n shape = ()
# For name tlen shape = ()
#
# So, data in this file are: 
# charge(1), mass(1), particles(10000,7), pz(1), rep(1), s_n(1), tlen(1)
#
charge = fp0[namesAttr[0]].value
# print ('charge = ',charge)
mass = fp0[namesAttr[1]].value
# print ('mass = ', mass)
particles = fp0[namesAttr[2]].value
# print ('particles = ',particles)
pz = fp0[namesAttr[3]].value
# print ('pz = ',pz)
rep = fp0[namesAttr[4]].value
# print ('rep = ',rep)
s_n = fp0[namesAttr[5]].value
# print ('s_n = ',s_n)
tlen = fp0[namesAttr[6]].value
# print ('tlen = ',tlen)

particlesNumber = len(particles)
print ('particlesNumber = ',particlesNumber)
x = np.zeros(particlesNumber)
px = np.zeros(particlesNumber)
y = np.zeros(particlesNumber)
py =np.zeros(particlesNumber)
z = np.zeros(particlesNumber)
pz = np.zeros(particlesNumber)
for n in range(particlesNumber):
    x[n] = particles[n,0]
    px[n] = particles[n,1]
    y[n] = particles[n,2]
    py[n] = particles[n,3]
    z[n] = particles[n,4]
    pz[n] = particles[n,5]

minX = 110.*np.min(x)
maxX = 110.*np.max(x)
minPx = 1.1e3*np.min(px)
maxPx = 1.1e3*np.max(px)

print ('minX = ',minX,', maxX = ',maxX)

#-------------------------------------
# #This is doesn't work(!):
#
# from Tkinter import Label
# widget = Label(None,'trxt='Hello, Yury')
# widget.pack()
# widget.mainloop()
#-------------------------------------

#------------------------------
# Input "games":
#
'''
existFileFlag = 0
print ('Files: %s' % fileList[0:numb_h5])
while existFileFlag == 0:
    crrntName = raw_input("\nSelect a name of file: ")
    print "Your file is: ", crrntName
    for name in fileList[0:numb_h5]:
#        print('name = ', name, ', check = ',crrntName)            
        if crrntName == name:
            existFileFlag = 1
            break
#    print('existFileFlag == ', existFileFlag)            
    if existFileFlag == 1:
        print ('File is found!')
    else:
        print ('File does not exist! Try again!')
'''


fig = plt.figure()
print ('fig = ', fig)
plt.plot(100.*x,1.e3*px,'.r')
plt.xlabel('x, cm',fontsize=12,color='m')
plt.ylabel('px, mrad',fontsize=12,color='m')
plt.xlim([minX,maxX])
plt.ylim([minPx,maxPx])
plt.title('Particle distribution at s = 0 ',fontsize=14, color='m')
plt.grid(True)
plt.show()

sys.exit()
