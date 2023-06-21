#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 16:53:11 2023

@author: joaquin
"""

from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
import pytc2

# Librería de TC2, esta la vas a usar mucho
from pytc2.sistemas_lineales import analyze_sys
ep = (10**0.1 -1)**(1/2)

zlp, plp, klp = sig.buttap(3)

zlp = [0+3j, 0-3j]
klp = 1/9

num, den = sig.zpk2tf(zlp, plp, klp)

lp = TransferFunction( num, den )

numhp, denhp = sig.lp2hp( num, den  )


hp = TransferFunction( numhp, denhp )
zhp, php, khp = sig.tf2zpk(numhp, denhp)

plt.close('all')
analyze_sys(lp, sys_name='Prueba TS5 lp')
analyze_sys(hp, sys_name='Prueba TS5 hp')
