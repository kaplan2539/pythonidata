#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

d=np.genfromtxt( 'plot.dat' );
        
fig=plt.figure(figsize=(11,8.5))
plt.errorbar(x=d[:,0],y=d[:,2],fmt='o',xerr=d[:,1],yerr=d[:,3])
plt.title("A plot using error bars")

plt.xlim(0,10)
plt.xticks([1.0,3.0,5.0,7.0,9.0])
plt.xlabel('y [mm]')

plt.ylim(0,20)
plt.ylabel('t [sec]')

plt.savefig('errorbar.pdf')
plt.savefig('errorbar.png')

plt.show()
