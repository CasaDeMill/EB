# -*- coding: utf-8 -*-
"""
Created on Mon May 22 15:52:42 2017

@author: artin
"""

from scipy import *
from pylab import *
import sympy
import sys

E=sympy.Symbol('E')
d=0.3
g=(2*pi)/d
h=6.582119514e-16
m=6520462880.796167
k=0
U=3
x=[]
y1=[]
y2=[]



for i in range(11):
    x.append(i)
    M=sympy.Matrix([[((h**2*k**2)/2*m)-E, U],[U, ((h**2*(k-g)**2)/(2*m))-E]])
    N=M.det().as_poly().coeffs()
    z=sympy.Poly.from_list(N,gens=E)
    p=sympy.solve(z,E)
    if len(p)==2:
        y1.append(p[0])
        y2.append(p[1])
    else:
        y1.append(p[0])
    



#for i in range(11):
#    x.append(i)
#    E1=(1/4*m**2)*(h**2*m*(g**2-2*g*k+2*k**2)+sqrt(g**2*h**4*m**2*(g-2*k)**2+16*m**4*U**2))
#    E2=(1/4*m**2)*(h**2*m*(g**2-2*g*k+2*k**2)-sqrt(g**2*h**4*m**2*(g-2*k)**2+16*m**4*U**2))
#    y1.append(E1)
#    y2.append(E2)


plot(x,y1)
if len(p)==2:    
    plot(x,y2)    
xlabel('k(1/nm)')
ylabel('E(k)(eV)')
show()