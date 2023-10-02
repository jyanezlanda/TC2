# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 13:18:53 2023

@author: Joaquin
"""
import numpy as np
import scipy.signal as sig
from pytc2.sistemas_lineales import analyze_sys
import matplotlib.pyplot as plt

plt.close(1)
plt.close(2)
plt.close(3)
plt.close(4)
plt.close(5)

fc = 1 # En kHz
fs = 10 #En kHz 


fs_n = fs
fc_n = fc

zz, pp, kk = sig.buttap(2)

zz, pp, kk = sig.lp2lp_zpk(zz, pp, kk, wo = 2*np.pi* fc_n)



num, den = sig.zpk2tf(zz, pp, kk)
TF = sig.TransferFunction(num, den)


z, p, k = sig.bilinear_zpk(zz, pp, kk, fs) # Tener en cuenta 

numz , denz = sig.zpk2tf(z, p, k)

TFZ = sig.TransferFunction(numz, denz, dt = 1/fs)
### Con funciones de bajo nivel

wrad, hh = sig.freqz_zpk(z, p, k, worN = 1000)

ww = wrad/np.pi

plt.figure(3)

plt.subplot(2,1,1)
plt.grid(visible = True)
plt.plot(ww, 20*np.log10(abs(hh)))

plt.subplot(2,1,2)
plt.grid(visible = True)
plt.plot(ww, np.angle(hh))

###Alto Nivel
analyze_sys(TFZ, sys_name = "Fs = 100 kHz", digital = True)

"""
fs = 10
Ww = fs

zz, pp, kk = sig.buttap(2)
zz, pp, kk = sig.lp2lp_zpk(zz, pp, kk, wo = fc/Ww)

num, den = sig.zpk2tf(zz, pp, kk)
TF = sig.TransferFunction(num, den)

z, p, k = sig.bilinear_zpk(zz, pp, kk, fs)

numz , denz = sig.zpk2tf(z, p, k)
TFZ = sig.TransferFunction(numz, denz)
analyze_sys(TFZ, sys_name = "Fs = 10 kHz",  digital = True)
"""