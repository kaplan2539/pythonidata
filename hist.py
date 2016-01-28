#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

d=np.genfromtxt( 'bb.dat' )

fig=plt.figure(figsize=(11,8.5))
n,bins,patches=plt.hist(d,40)
plt.title("A simple histogram plot")

plt.savefig('hist.pdf')
plt.savefig('hist.png')

plt.show()
