import sys, os
import numpy as np
import create_madx_nl_elements_sequence

mu0 = .3
l0 = 1.8
cval = .03
tval = .4
f0 = l0/4.0*(1.01+1.0/np.tan(np.pi*mu0)**2)
betae = l0/np.sqrt(1.0-(1.0-l0/2.0/f0)**2)
betas = l0*(1.0-l0/4.0/f0)/np.sqrt(1.0-(1.0-l0/2.0/f0)**2)
# print ('Focal length is {} m'.format(f0))
# print ('Beta values at entrance are {} m'.format(betae))
# print ('Beta value at center is  {} m'.format(betas))
print ('Focal length is %e m' % f0)
print ('Beta values at entrance are %e m' % betae)
print ('Beta value at center is  %e m' % betas)


testNLI = create_madx_nl_elements_sequence.NonlinearInsert(l0, mu0, cval, tval)
num_slicesNLI = testNLI.num_slices
print ('num_slicesNLI = %d' % num_slicesNLI)

testNLI1 = create_madx_nl_elements_sequence.NonlinearInsert.generate_sequence(testNLI)
# num_slicesNLI1 = testNLI1.num_slices
# print ('num_slicesNLI1 = %d' % num_slicesNLI1)

testNLI2 = create_madx_nl_elements_sequence.NonlinearInsert.create_madx(testNLI)
len_testNLI2 = len(testNLI2)
num_slicesNLI2 = testNLI.num_slices
print ('len_testNLI2 = %d; num_slicesNLI2 = %d' % (len_testNLI2,num_slicesNLI2))

strNLI1 = testNLI1[0]
print ('strNLI1[0] = %s' % strNLI1)

strNLI2 = testNLI2[0]
print ('strNLI2[0] = %s' % strNLI2)

for n in range(num_slicesNLI2-1):
    print ('str[%d]' % n)
#    str = testNLI2[n]
#    print ('str[%d] = %s' % (n,str))

    
    
sys.exit()

