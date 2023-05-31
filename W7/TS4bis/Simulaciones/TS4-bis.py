# -*- coding: utf-8 -*-
"""
Created on Sat May 27 21:01:29 2023

@author: Joaquin
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

amax = 3
amin = 20

fpi = 1600
fsi = 1250

fps = 2500  
fss = 3200

fo = np.sqrt(fpi*fps)
print("f0 =", fo)

norma_w = 2*np.pi*fo

w0 = 2*np.pi*fo/norma_w
wpi = 2*np.pi*fpi/norma_w
wsi = 2*np.pi*fsi/norma_w

wps = 2*np.pi*fps/norma_w
wss = 2*np.pi*fss/norma_w

BW = fps-fpi
Q = fo/BW
##Transformamos al filtro pasabajos prototipo
Wp = Q*(w0**2-wpi**2)/wpi/w0
Ws = Q*(w0**2-wsi**2)/wsi/w0

print("Wp =", Wp, "Ws =", Ws)

ee = 10**(amax/10)-1

print("epsilon^2 =", ee)

n = 0
for i in  range (1, 5):
       at = 10*np.log10(1+ee* Ws**(2*i))
       print("Si n =", i, "Atenuación en Ws =", at)
       if (at > amin and n == 0):
           n = i
print ("El orden del filtro elegido es n =", n)

z, p, k = sig.buttap(n)

Nlp, Dlp = sig.zpk2tf(z, p, k)
tflp = TransferFunction( 3.16*Nlp, Dlp )

bodePlot(tflp, fig_id=1, filter_description = 'Q={:3.3f}'.format(Q) )
pzmap(tflp, fig_id=2, filter_description = 'Q={:3.3f}'.format(Q)) #S plane pole/zero plot
GroupDelay(tflp, fig_id=3, filter_description = 'Q={:3.3f}'.format(Q))

Nbp, Dbp = sig.lp2bp(3.16*Nlp , Dlp, w0, BW/fo)

zbp, pbp, lbp = sig.tf2zpk(Dbp, Nbp)

tfbp = TransferFunction(Nbp, Dbp)

bodePlot(tfbp, fig_id=1, filter_description = 'Q={:3.3f}'.format(Q) )
pzmap(tfbp, fig_id=2, filter_description = 'Q={:3.3f}'.format(Q)) #S plane pole/zero plot
GroupDelay(tfbp, fig_id=3, filter_description = 'Q={:3.3f}'.format(Q))
                                                                           