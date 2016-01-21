#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

fitfunc = lambda p,x : p[0] + p[1]*x
errfunc = lambda p,x,y,xerr,yerr : (y-fitfunc(p,x))/xerr/yerr

d=np.genfromtxt( 'plot.dat' );

x=d[:,0]
xerr=d[:,1]
y=d[:,2]
yerr=d[:,3]

inital_p = [1.0,1.0]
r = optimize.leastsq(errfunc,inital_p,args=(x,y,xerr,yerr),full_output=1)
(result_p, cov) = (r[0],r[1])

fig=plt.figure(figsize=(11,8.5))
plt.plot(np.array([0.0, 10.0]),fitfunc(result_p,np.array([0.0,10.0])))
plt.errorbar(x=x,y=y,fmt='o',xerr=xerr,yerr=yerr)

plt.title("A weighted fit using errors")

plt.xlim(0,10)
plt.xticks([1.0,3.0,5.0,7.0,9.0])
plt.xlabel('y [mm]')

plt.ylim(0,20)
plt.ylabel('t [sec]')

plt.savefig('fit.pdf')
plt.savefig('fit.png')

plt.show()
