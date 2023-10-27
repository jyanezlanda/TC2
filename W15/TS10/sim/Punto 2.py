#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 17:42:22 2023

@author: joaquin
"""

from pytc2.sintesis_dipolo import remover_polo_dc, remover_polo_infinito, remover_valor_en_dc, remover_valor_en_infinito
from pytc2.remociones import remover_polo_sigma
import sympy as sp

s = sp.symbols('s', complex=True)

ZZ = 1*(s**2 + s + 1)/((s**2 + 2*s + 5)*(s+1))

YY = 1/ZZ


Y1, K1oo = remover_polo_infinito(YY)

Y2, K2 = remover_valor_en_infinito(Y1)

Z2 = 1/Y2

Z3, K3oo = remover_polo_infinito(Z2)

Z4, K4 = remover_valor_en_infinito(Z3)

Y4 = 1/Z4

Y5, k5oo = remover_polo_infinito(Y4)


ZZ = ((s + 4)*(s + 2))/((s + 3)*(s + 1))
Za, K1 = remover_valor_en_infinito(ZZ, sigma_zero = 6)
Ya = 1/Za

Yb, K2, R, C = remover_polo_sigma(imm= Ya, sigma = 6, isImpedance = False, isRC=True, sigma_zero= None)