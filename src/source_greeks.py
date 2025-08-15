import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from mpl_toolkits.mplot3d import Axes3D  # registers the 3D projection

N = norm.cdf

#  d1, d2 computation according to Black-Scholes framework

def d1(K, S0, r, sigm, T):
    return (np.log(S0/K) + (r + (sigm**2) / 2)*T) / (sigm*np.sqrt(T))

def d2(K, S0, r, sigm, T):
    return d1(K, S0, r, sigm, T) - sigm*np.sqrt(T)

def greek_delta(K, S0, r, sigm, T, opt_type):
    if opt_type == "call":
        delt = N(d1(K, S0, r, sigm, T))
    elif opt_type == "put":
        delt = N(d1(K, S0, r, sigm, T)) - 1
    
    return delt

def greek_theta(K, S0, r, sigm, T, opt_type):
    
    first_term = -0.5 * S0 * sigm * np.exp( -0.5 *  (d1(K, S0, r, sigm, T)) **2 ) / ( np.sqrt(2*np.pi*T) ) 

    if opt_type == "call":
        sec_term = - r * K *np.exp(-r*T)*N(d2(K, S0, r, sigm, T))
    elif opt_type == "put":
        sec_term = r * K *np.exp(-r*T)*N(-d2(K, S0, r, sigm, T))
    else: 
        sec_term = 0
        
    return first_term + sec_term


def greek_gamma(K, S0, r, sigm, T, opt_type):
    return np.exp( -0.5 *  (d1(K, S0, r, sigm, T)) **2 ) / (S0 * sigm * np.sqrt(2*np.pi*T) ) 

def greek_vega(K, S0, r, sigm, T, opt_type):
    return S0 * np.sqrt(T) * np.exp( - 0.5 *  (d1(K, S0, r, sigm, T)) **2 ) / ( np.sqrt(2*np.pi))


def greek_rho(K, S0, r, sigm, T, opt_type):
    first_mult = K * T * np.exp(-r *T) 

    if opt_type == "call":
        sec_mult = N(d2(K, S0, r, sigm, T))
    elif opt_type == "put":
        sec_mult = -N(-d2(K, S0, r, sigm, T))
    else:
        sec_mult = 0
    return first_mult * sec_mult