#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 15:43:49 2021

@author: jessicagamboa

It defines the following parameters:
    
    ASD - Aerosol size distributions based on lognormal distribution
    kappa - Hygroscopicity parameter  
    W - Updraft/vertical constant velocity 
    dtD - Temporal step in dinamical equation
    wlf - Final liquid water mixing ratio
    T0 - Initial temperature
    z0 - Initial height
    p0 - Initial pressure
    rh0 - Initial relative humidity
    
    D - Dry diameter
    Sigma = Surface tension of the solution/air interface
    K = Kelvin factor

       
"""

# ---------------------------------------------------------------------------#
# Constant Parameters
# ---------------------------------------------------------------------------#

R = 8.3144 # Gases universal constant - J/(K*mol)
Rd = 287.058 # J kg-1 K-1 sp. for dry air DESCOBRIR OQ É
Mw = 18.01528e-3 # Water molar mass - kg/mol
Ma = 28.9644e-3 # Air molar mass - kg/mol
g = 9.8 # Gravity acceleration - m/sˆ2
T0 = 298.15 # Initial temperature - Kelvin (K) - Araujo on pg 56
Z0 = 1000 # Initial height - (m) - Gabriel's code
P0 = 0.9376 # Initial pressure - (atm) - Gabriel's code
Rh0 = 95e-2 # Initial relative humidity
Dtd = 0.05 # Temporal step in dinamical equation - (s) - Araujo 
Dd = 50e-9 # Dry diameter - (nm) - Araujo on Figure 3.1 in pg.56

# ---------------------------------------------------------------------------#
# Variable Parameters
# ---------------------------------------------------------------------------#

def ASD(D):
    """
    Description:
        Compute the aererosol size distributions based on lognormal 
        distribution. 
    Reference:
        Seinfeld, Pandis (pg. 371); Araujo (pg. 32)
    Arguments:
        double D : Aerosol diameter in meters (m)
    Returns:
        np.array ASD[] : concentrations, in , of each bin of diameter 
        discretization
        from 1 to p - 1
    Example:
        
    """
    
    
    return ASD

def kappa(D):
    """
    Description:
        Compute the hygroscopicity parameter
    Reference:
        Petters (pg. 5); Araujo (pg. 53)
    Arguments:

    Returns:
        
    Example:
        
    """  

    kappa = 0.15
    
    return kappa

def W():
    """
    Description: 
        Updraft/vertical constant velocity
    
    """
    W = [2]
    
    return W

def sigma(T):
    """
    Description: 
        Surface tension of the solution/air interface 
    """
    sigma = 0.0761 - (T-273)*1.55e-4 # J/mˆ2, DE ONDE VEIO A FORMULA?
    
    return sigma

def rhow(T):
    """
    Description: 
        Density of water
    
    """
    t = T - 273.15 # Temperature in Celsius
    # Coefficients from Table 3.3 Araujo pg 62
    A0 = 999.8396 # unit: kg/mˆ3
    A1 = 18.224944 # unit: kg/(mˆ3 C)
    A2 = -7.92221e-3 # unit: kg/(mˆ3 Cˆ2)
    A3 = -55.44846e-6 # unit: kg/(mˆ3 Cˆ3)
    A4 = 149.7562e-9 # unit: kg/(mˆ3 Cˆ4)
    A5 = -393.2952e-12 # unit: kg/(mˆ3 Cˆ4)
    B = 18.159725e-3 # unit: 1/C
    
    rhow = (A0 + A1*t + A2*(t**2) + A3*(t**3) + A4*(t**4) + A5*(t**5))/(1+B*t)
    
    return rhow




