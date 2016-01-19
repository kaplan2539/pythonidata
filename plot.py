#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

d=np.genfromtxt( 'plot.dat' );
        
fig=plt.figure(figsize=(11,8.5))
plt.plot(d[:,0],d[:,1],'-')
plt.title("A simple x-y plot")

plt.xlim(0,10)
plt.xticks([1.0,3.0,5.0,7.0,9.0])
plt.xlabel('y [mm]')

plt.ylabel('t [sec]')

plt.savefig('plot.pdf')
plt.savefig('plot.png')

plt.show()
