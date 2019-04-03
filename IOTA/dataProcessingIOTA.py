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
#
# Synergia specific imports:
#
import rssynergia 
from rssynergia.base_diagnostics import read_bunch
from rssynergia.base_diagnostics import workflow
from rssynergia.base_diagnostics import lfplot
from rssynergia.base_diagnostics import plotbeam
from rssynergia.base_diagnostics import latticework
from rssynergia.base_diagnostics import basic_calcs
from rssynergia.base_diagnostics import pltbunch
from rssynergia.base_diagnostics import elliptic_sp
from rssynergia.base_diagnostics import options
from rssynergia.base_diagnostics import diagplot
from rssynergia.elliptic import elliptic_beam6d
import synergia
import synergia_workflow

workDir = '/home/vagrant/jupyter/eidelyur/iota/example_run/'

fileLS = os.popen('ls').readlines()
numbFiles = len(fileLS)
fileList = [' ']*numbFiles
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
        numb_h5 = k
print 'numb_h5 = ', numb_h5,'; "basic" = ',numb_basic,', "full2" = ', \
numb_full2,', "particles" = ',numb_particles        
fileList[0:numb_h5]


# Files like 'basic_strct*.h5':
#
nameFile = workDir + 'basic_strct0.h5'
fb0 = h5py.File(nameFile,'r')
fb0_len = len(fb0)              # = 12
fb0_keys = fb0.keys()
for name in fb0_keys:
    shapeName = fb0[name].shape
    print ('For name %s shape = %s' % (name,shapeName))
# For name charge shape = ()
# For name mass shape = ()
# For name max shape = (3, 14642)
# For name mean shape = (6, 14642)
# For name min shape = (3, 14642)
# For name num_particles shape = (14642,)
# For name pz shape = (14642,)
# For name real_num_particles shape = (14642,)
# For name repetition shape = (14642,)
# For name s shape = (14642,)
# For name s_n shape = (14642,)
# For name std shape = (6, 14642)
#
# So, data in this file are: 
# charge(1), mass(1), max(3,14642), mean(6,14642), min(3,14642), num_particles(14642), pz(14642),
# real_num_particles(14642), repetition(14642), s(14642), s_n(14642), std(6,14642)
#
charge = fb0[fb0_keys[0]].value
mass = fb0[fb0_keys[1]].value
max = fb0[fb0_keys[2]].value
mean = fb0[fb0_keys[3]].value
min = fb0[fb0_keys[4]].value
num_particles = fb0[fb0_keys[5]].value
pz = fb0[fb0_keys[6]].value
real_num_particles = fb0[fb0_keys[7]].value
crepetition = fb0[fb0_keys[8]].value
s = fb0[fb0_keys[9]].value
s_n = fb0[fb0_keys[10]].value
std = fb0[fb0_keys[11]].value

fb0.close()

# Files like 'particles_strct*_*.h5':
#
nameFile = workDir + 'particles_strct0_0000.h5'
# nameFile = workDir + 'basic_strct0.h5'
# nameFile = workDir + 'full2_strct0.h5'
fp0 = h5py.File(nameFile,'r')
fp0_len = len(fp0)              # = 7
fp0_keys = fp0.keys()
for name in fp0_keys:
    shapeName = fp0[name].shape
    stringHelp = str(shapeName)[1:len(str(shapeName))-1] 
    countCommas = stringHelp.count(',')
    print ('For name %s shape = %s => %s; commas = %d' % (name,shapeName,stringHelp,countCommas))
    if countCommas == 0:
        dimnsn = 0
    else:
        numbIndx = stringHelp.split(',')
        dimnsn = len(numbIndx)
        if numbIndx[dimnsn-1] == '':
            dimnsn = dimnsn-1
            numbIndx = numbIndx[0:dimnsn]
        print 'numbIndx = ', numbIndx
    print 'dimnsn = ',dimnsn          
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
charge = fp0[fp0_keys[0]].value
mass = fp0[fp0_keys[1]].value
particles = fp0[fp0_keys[2]].value
pz = fp0[fp0_keys[3]].value
rep = fp0[fp0_keys[4]].value
s_n = fp0[fp0_keys[5]].value
tlen = fp0[fp0_keys[6]].value

fp0.close()

particlesNumber = len(particles)
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

fig = plt.figure()
plt.plot(100.*x,1.e3*px,'.r')
plt.xlabel('x, cm',fontsize=12,color='m')
plt.ylabel('px, mrad',fontsize=12,color='m')
plt.xlim([minX,maxX])
plt.ylim([minPx,maxPx])
plt.title('Particle distribution at s = 0 ',fontsize=14, color='m')
plt.grid(True)
plt.show()
    
sys.exit()

# Files like 'full2_strct*.h5':
#
nameFile = workDir + 'full2_strct0.h5'
ff0 = h5py.File(nameFile,'r')
ff0_len = len(ff0)              # = 19
ff0_keys = ff0.keys()
for name in ff0_keys:
    shapeName = ff0[name].shape
    print ('For name - %s shape = %s' % (name,shapeName))
# For name charge shape = ()
# For name corr shape = (6, 6, 22)
# For name emitx shape = (22,)
# For name emitxy shape = (22,)
# For name emitxyz shape = (22,)
# For name emity shape = (22,)
# For name emitz shape = (22,)
# For name mass shape = ()
# For name max shape = (3, 22)
# For name mean shape = (6, 22)
# For name min shape = (3, 22)
# For name mom2 shape = (6, 6, 22)
# For name num_particles shape = (22,)
# For name pz shape = (22,)
# For name real_num_particles shape = (22,)
# For name repetition shape = (22,)
# For name s shape = (22,)
# For name s_n shape = (22,)
# For name std shape = (6, 22)
#
# So, data in this file are: 
# charge(1), corr(6, 6, 22), emitx(22), emitxy(22), emitxyz(22), emity(22),
# emitz(22), mass(1), max(3, 22), mean(6, 22), min(3, 22), mom2(6, 6, 22),
# num_particles(22), pz(22),real_num_particles(22), repetition(22), s(22), 
# s_n(22), std(6, 22)
#
charge = ff0[ff0_keys[0]].value
corr = ff0[ff0_keys[1]].value
emitx = ff0[ff0_keys[2]].value
emitxy = ff0[ff0_keys[3]].value
emitxyz = ff0[ff0_keys[4]].value
emity = ff0[ff0_keys[5]].value
emitz = ff0[ff0_keys[6]].value
mass = ff0[ff0_keys[7]].value
max = ff0[ff0_keys[8]].value
mean = ff0[fb0_keys[f]].value
min = ff0[ff0_keys[10]].value
mom2 = ff0[ff0_keys[11]].value
num_particles = ff0[ff0_keys[12]].value
real_num_particles = ff0[ff0_keys[13]].value
repetition = ff0[ff0_keys[14]].value
s = ff0[ff0_keys[16]].value
s_n = ff0[ff0_keys[17]].value
std = ff0[ff0_keys[18]].value


ff0.close()
