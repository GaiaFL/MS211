from math import *
import numpy as np

c1 = 0.1
c2 = 0.05
d1 = 0.1
d2 = 0.05

def x1(x0, y0, h):
	return x0 + h*(c1*x0 - d1*x0*y0)

def y1(x0, y0, h):
	return y0 + h*(c2*x0*y0 - d2*y0)


def euler_explicito (h, n_it):
	x = [3.0]
	y = [1.0]
	i = 1
	while(i < n_it):
		x.append(x1(x[i-1],y[i-1],h))
		y.append(y1(x[i-1],y[i-1],h))
		i += 1
	return x, y

T = 365
t1 = T/365
t2 = T/3650

