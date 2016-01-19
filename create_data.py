#!/usr/bin/env python

import numpy as np

def f(x,m=2,b=0.5,sigma=1.0):
    return m*x + b + np.random.normal(scale=sigma)

with open('plot.dat','w') as out:
    for x in range(1,9):
        out.write('%f %f\n' % (x,f(x)))

