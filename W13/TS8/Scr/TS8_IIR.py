#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 21:30:01 2023

@author: joaquin

"""

import numpy as np
import scipy.signal as sig
import matplotlib as mpl
import matplotlib.pyplot as plt
from pytc2.sistemas_lineales import plot_plantilla
from control import pzmap, TransferFunction


ws1 = 1 #rad/s
wp1 = 3 #rad/s
wp2 = 25 #rad/s
ws2 = 35 #rad/s

fs = 1000 #kHz
nyq_frec = fs / 2

Amin = 40 #dB
Amax = 0.4 #dB

frecs = np.array([0.0,         ws1,         wp1,     wp2,     ws2,         nyq_frec   ]) / nyq_frec
gains = np.array([-Amax, -Amax, -Amin, -Amin, -Amax, -Amax])
gains = 10**(gains/20)

wpass = [wp1/fs, wp2/fs]
wstop = [ws1/fs, ws2/fs]

sos_pb_dig = sig.iirdesign(wp= wpass, ws= wstop, gpass= Amax, gstop= Amin, analog= False, ftype= 'butter', output='SOS', fs= 1)

ww, hh = sig.sosfreqz(sos= sos_pb_dig, worN= 2000, whole= False, fs = fs)

b,a = sig.sos2tf(sos_pb_dig)

np.

plt.close(1)

pzmap(sys = TransferFunction(b, a, dt = 1/fs), plot = True, grid = True)
# plt.figure(1)

# plt.subplot(2,1,1)
# plt.title("Filtro IIR")
# plt.ylabel('Módulo [dB]')
# plt.xlabel('Frecuencia [Hz]')
# plt.grid(visible=True)
# plt.plot(ww, 20*np.log(np.abs(hh)));
# plt.axis([0, 100, -100, 5 ])

# plot_plantilla(filter_type = 'bandpass', fpass = [wp1, wp2], ripple = Amax , fstop = [ws1, ws2], attenuation= Amin, fs = 1000)

# plt.subplot(2,1,2)
# plt.title("Phase Response")
# plt.grid(visible=True)
# plt.plot(ww, np.angle(hh));
# """

# FITLRO FIR

# """
# import scipy as sci

# ws1 = 1 #rad/s
# wp1 = 3 #rad/s
# wp2 = 25 #rad/s
# ws2 = 35 #rad/s

# fs = 1000 #kHz
# nyq_frec = fs / 2

# Amin = 0.5 #dB
# Amax = 40#dB

# frecs = np.array([0.0,         ws1,         wp1,     wp2,     ws2,         nyq_frec   ]) / nyq_frec
# gains = np.array([-Amax, -Amax, -Amin, -Amin, -Amax, -Amax])
# gains = 10**(gains/20)