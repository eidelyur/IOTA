import sys, os
import numpy as np
import scipy


# pwdRes = sys.pwd()
# print ('Start of Test: pwdRes = %s' % pwdRes)
print ('Start of Test...')

def parameters(length,phase,cval,tval,slices):
    madx_elmnts = []
# Define the focal length of the insert using the phase advance and length
    f0 = length/4.0*(1.0+1.0/np.tan(np.pi*phase)**2)
    print ('f0 = {}'.format(f0))
# Define array of s-values
    start = (length/slices)*0.5
    print ('start = {}'.format(start))
    end = length - start
    print ('end = {}'.format(end))
# Set the initial beta value to help compare to lattice functions
    beta0 = length/np.sqrt(1.0-(1.0-length/2.0/f0)**2)
    print ('beta0 = {}'.format(beta0))
# Make an attribute as they could be useful for constructing the mad-x sequence
    s_vals = np.linspace(start,end,slices) 
    for n in range(len(s_vals)): 
# Set the beta functions as an attribute for comparing against other lattice functions
        bn = length*(1-s_vals[n]*(length-s_vals[n])/length/f0)/ \
             np.sqrt(1.0-(1.0-length/2.0/f0)**2)
        knn = tval*length/slices/bn**2
        cnll = cval*np.sqrt(bn)
        knll = knn*cnll**2
#        print('{}: s_vals = {}, bn = {}, knn = {}, cnll = {}, knll = {}'. \
#              format(n,s_vals[n],bn,knn,cnll,knll))
        elem = 'elem'+str(int(n))+', knll='+'{:e}'.format(knll)+ \
               ', cnll='+'{:e}'.format(cnll)
        print ('elem = {}'.format(elem))
        madx_elmnts.append(elem)	          

 
    return madx_elmnts

length = 1.8
phase = 0.3
slices = 10
cval = .03
tval = .04

line = parameters(length,phase,tval,cval,slices)
for n in range(slices):
    print ('elem = {}'.format(line[n]))

print ('End of Test...')

sys.exit()
