import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from mpl_toolkits.mplot3d import Axes3D  # registers the 3D projection
from source_greeks import greek_delta, greek_gamma, greek_theta, greek_rho, greek_vega

def get_greek_func(greek_name):
    greek_name = greek_name.lower()
    if greek_name == "delta": return greek_delta
    if greek_name == "gamma": return greek_gamma
    if greek_name == "vega":  return greek_vega
    if greek_name == "theta": return greek_theta
    if greek_name == "rho":   return greek_rho
    raise ValueError("greek_name must be one of: delta, gamma, vega, theta, rho")

def delta_3d_surf(delt, S_grid, T_grid, greek_l, opt_type="call"):
    
    # Create 3D figure

    if greek_l == "delta":
        gr_l = r"$\Delta$"
    elif greek_l == "theta":
        gr_l = r"$\Theta$"
    elif greek_l == "gamma":
        gr_l = r"$\Gamma$"
    elif greek_l == "vega":
        gr_l = "$\\nu$"
    elif greek_l == "rho":
        gr_l = "$\\rho"
    else:
        raise ValueError(f"Unknown greek_l: {greek_l}")
    
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot surface
    surf = ax.plot_surface(S_grid, T_grid, delt,
                           cmap='viridis', edgecolor='none', alpha=0.9)
    
    # Labels
    ax.set_xlabel('Stock Price S')
    ax.set_ylabel('Time to Maturity T (years)')
    ax.set_zlabel(f"{gr_l}")
    # Add color bar
    fig.colorbar(surf, shrink=0.5, aspect=10, label= f"{gr_l} Value")
    
    plt.title(f"{gr_l} Surface of " + f"{opt_type} option")       
    plt.show()


def plot_greek_vs_S(greek_l, K, r, sigm,fixed_time, 
                    st_points, opt_type="call"):
    """
    Plot Greek(S) for several fixed maturities T in years.
    S is shown as a multiple of K .
    """

    if greek_l == "delta":
        gr_l = r"$\Delta$"
    elif greek_l == "theta":
        gr_l = r"$\Theta$"
    elif greek_l == "gamma":
        gr_l = r"$\Gamma$"
    elif greek_l == "vega":
        gr_l = "$\\nu$"
    elif greek_l == "rho":
        gr_l = r"$\rho$"
    else:
        raise ValueError(f"Unknown greek_l: {greek_l}")

    greek_func = get_greek_func(greek_l)
        
    for i in range(len(fixed_time)):
        delt_points = greek_func(K, st_points, r, sigm, fixed_time[i], opt_type)
        plt.plot(st_points, delt_points, label=f"T={round(fixed_time[i],2) }, years")

    plt.axvline(x=K, color='red', linestyle='--', linewidth=1.5, label='Strike Price')
    plt.xlabel("Stock Price $S$")
    plt.ylabel(fr"{gr_l} ({opt_type})")
    plt.title(fr"{opt_type.capitalize()} {gr_l} vs. Stock Price for Fixed $T$")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_greek_vs_T(greek_l, K, r, sigm,time_points, 
                    fixed_ST, opt_type="call"):
    """
    Plot Greek(T) for several fixed S.
    """

    if greek_l == "delta":
        gr_l = r"$\Delta$"
    elif greek_l == "theta":
        gr_l = r"$\Theta$"
    elif greek_l == "gamma":
        gr_l = r"$\Gamma$"
    elif greek_l == "vega":
        gr_l = "$\\nu$"
    elif greek_l == "rho":
        gr_l = "$\\rho"
    else:
        raise ValueError(f"Unknown greek_l: {greek_l}")

    greek_func = get_greek_func(greek_l)
        
    for i in range(len(fixed_ST)):
        delt_points = greek_func(K, fixed_ST[i], r, sigm, time_points, opt_type)
        plt.plot(time_points, delt_points, label=f"S={round(fixed_ST[i],1) }$")

    
    plt.xlabel("Time to maturiry(years)")
    plt.ylabel(fr"{gr_l} ({opt_type})")
    plt.title(fr"{opt_type.capitalize()} {gr_l} vs. Time to Maturity T (years) for Fixed S")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()