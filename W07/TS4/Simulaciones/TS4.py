#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 12:17:13 2023

@author: joaquin
"""

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig


# Librería de TC2, esta la vas a usar mucho
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

plt.figure(1)
plt.close(1)

amax = 1
amin = 30

fp = 40000
fs = 10000

norma_w = 2*np.pi*fp
wp = 2*np.pi*fp/norma_w
ws = 2*np.pi*fs/norma_w

##Transformamos al filtro pasabajos prototipo
norma_W = 1/norma_w
Wp = 1/wp
Ws = 1/ws

ee = 10**(amax/10)-1
n = 0
for i in  range (1, 5):
       at = 10*np.log10(1+ee* Ws**(2*i))
       print("Si n =", i, "Atenuación en Ws =", at)
       if (at > amin and n == 0):
           n = i
print ("El orden del filtro elegido es n =", n)

norma_W = norma_W * ee**(1/(2*n)) ## Normalizamos para tener una omega de butter

Q = 1/(2*np.cos(np.pi/3))

z, p, k = sig.buttap(3)

Nlp, Dlp = sig.zpk2tf(z, p, k)
tflp = TransferFunction( Nlp, Dlp )

bodePlot(tflp, fig_id=1, filter_description = 'Q={:3.3f}'.format(Q) )
pzmap(tflp, fig_id=2, filter_description = 'Q={:3.3f}'.format(Q)) #S plane pole/zero plot
GroupDelay(tflp, fig_id=3, filter_description = 'Q={:3.3f}'.format(Q))

Nhp, Dhp = sig.lp2hp(Nlp , Dlp)

tfhp = TransferFunction(Nhp, Dhp)

bodePlot(tfhp, fig_id=1, filter_description = 'Q={:3.3f}'.format(Q) )
pzmap(tfhp, fig_id=2, filter_description = 'Q={:3.3f}'.format(Q)) #S plane pole/zero plot
GroupDelay(tfhp, fig_id=3, filter_description = 'Q={:3.3f}'.format(Q))
                                                                           