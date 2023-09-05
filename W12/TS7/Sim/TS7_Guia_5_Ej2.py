# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 13:18:53 2023

@author: Joaquin
"""

import scipy.signal as sig
from pytc2.sistemas_lineales import analyze_sys
import matplotlib.pyplot as plt

plt.close(1)
plt.close(3)
plt.close(5)

fc = 6 # En kHz
fs = 100 #En kHz 

Ww = fs

zz, pp, kk = sig.buttap(2)

zz, pp, kk = sig.lp2hp_zpk(zz, pp, kk, wo = fc/Ww)



num, den = sig.zpk2tf(zz, pp, kk)
TF = sig.TransferFunction(num, den)


z, p, k = sig.bilinear_zpk(zz, pp, kk, fs/Ww)

numz , denz = sig.zpk2tf(z, p, k)

TFZ = sig.TransferFunction(numz, denz)

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