#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 09:54:52 2021

@author: jessicagamboa
"""

import parameters as prm
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------#
# Examples of Köhler curves
# ---------------------------------------------------------------------------#


# Definition of A to use in the Kelvin factor, Ke = A/Dwet (from Araujo eq. 3.3)
A = (4*prm.sigma(prm.T0)*prm.Mw)/(prm.R*prm.T0*prm.rhow(prm.T0))


# Saturation from (from Araujo eq. 3.20)
#s = lambda Dw : (Dw**3 - prm.Dd**3)*np.exp(A/Dw)/(Dw**3 - prm.Dd**3*(1-prm.kappa(prm.Dd)))

# Supersaturation 1 - kappa1 = 0.15 , Dd1 = 50e-9
kappa1 =  0.15
Dd1 = 50e-9
S1 = lambda Dw : ((((Dw**3 - Dd1**3)*np.exp(A/Dw))/(Dw**3 - (Dd1)**3*(1 - kappa1))) - 1)*100
                   
# Supersaturation 2 - kappa2 = 0.15 , Dd2 = 50e-9
kappa2 =  1.4
Dd2 = 50e-9
S2 = lambda Dw2 : ((((Dw2**3 - Dd2**3)*np.exp(A/Dw2))/(Dw2**3 - (Dd2)**3*(1 - kappa2))) - 1)*100
                  
# Supersaturation 3 - kappa3 = 0.15 , Dd3 = 50e-9
kappa3 =  0.15
Dd3 = 200e-9
S3 = lambda Dw3 : ((((Dw3**3 - Dd3**3)*np.exp(A/Dw3))/(Dw3**3 - (Dd3)**3*(1 - kappa3))) - 1)*100

# Supersaturation 4 - kappa4 = 0.15 , Dd4 = 50e-9
kappa4 =  1.4
Dd4 = 200e-9
S4 = lambda Dw4 : ((((Dw4**3 - Dd4**3)*np.exp(A/Dw4))/(Dw4**3 - (Dd4)**3*(1 - kappa4))) - 1)*100

# Supersaturation 5 - kappa5 = 0.15 , Dd5 = 50e-9
kappa5 =  0.15
Dd5 = 350e-9
S5 = lambda Dw5 : ((((Dw5**3 - Dd5**3)*np.exp(A/Dw5))/(Dw5**3 - (Dd5)**3*(1 - kappa5))) - 1)*100

# Supersaturation 6 - kappa6 = 0.15 , Dd6 = 50e-9
kappa6 =  1.4
Dd6 = 350e-9
S6 = lambda Dw6 : ((((Dw6**3 - Dd6**3)*np.exp(A/Dw6))/(Dw6**3 - (Dd6)**3*(1 - kappa6))) - 1)*100


Dw1 = np.linspace(50e-9,10000e-9, 2001)
Dw2 = np.linspace(50e-9,10000e-9, 2001)
Dw3 = np.linspace(300e-9,10000e-9, 2001)
Dw4 = np.linspace(300e-9,10000e-9, 2001)
Dw5 = np.linspace(350e-9,10000e-9, 2001)
Dw6 = np.linspace(350e-9,10000e-9, 2001)


plt.plot(Dw1, S1(Dw1), ls = '--', color= 'red', markersize=1) 
plt.plot(Dw2, S2(Dw2),  color= 'red', markersize=1)
plt.plot(Dw3, S3(Dw3), ls = '--', color= 'purple', markersize=1) 
plt.plot(Dw4, S4(Dw4),  color= 'purple', markersize=1)
plt.plot(Dw5, S5(Dw5), ls = '--', color= 'orange', markersize=1) 
plt.plot(Dw6, S6(Dw6),  color= 'orange', markersize=1)
plt.axhline(y = 0.4, color = 'black')  
plt.axhline(y = 0.9, color = 'black', ls = '--')
ax = plt.gca()
ax.set_xlim([0.9e-7,1e-5]) 
ax.set_ylim([-0.4,1.2])
ax.set_xscale('log') 
plt.title("Köhler Curves", fontsize = 12)
lgd = plt.legend(["Dd = 50nm  kappa = 0.15", "Dd = 50nm  kappa = 1.40", 
                  "Dd = 200nm  kappa = 0.15", "Dd = 200nm  kappa = 1.40", 
                  "Dd = 350nm  kappa = 0.15", "Dd = 350nm  kappa = 1.40",
                  "Satm = 0.4%", "Satm = 0.9%"], 
                  loc='upper right')
plt.xlabel('Dwet (m)')
plt.ylabel("$Supersaturation$ (%)")
plt.grid()
plt.show
plt.savefig('kohler curves', dpi=600, bbox_extra_artist=(lgd), bbox_inches = 'tight')


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    