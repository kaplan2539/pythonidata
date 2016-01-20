#!/usr/bin/env python

import numpy as np
import math

def f(x,m=2,b=0.5,sigma=None):
    if sigma==None:
        sigma=abs(math.sin(x)) #*x/10.0
    return m*x + b + np.random.normal(scale=sigma)

with open('plot.dat','w') as out:
    for j in range(1,9):
        x_mean = 0.0
        x_rms  = 0.0
        y_mean = 0.0
        y_rms  = 0.0
        n=10
        for i in range(0,n):
            x=j+np.random.normal(scale=j/10.0)
            y=f(x)
            x_mean+=x
            x_rms +=x*x
            y_mean+=y
            y_rms +=y*y
        x_mean/=n
        x_rms/=n
        y_mean/=n
        y_rms/=n
        x_rms=math.sqrt(x_rms - (x_mean*x_mean))
        y_rms=math.sqrt(y_rms - (y_mean*y_mean))
        out.write('%f %f %f %f\n' % (x_mean,x_rms,y_mean,y_rms))

