# Options Greeks & Delta-Hedging Simulator

This repository contains two self-contained Jupyter notebooks that illustrate key concepts in **derivatives risk management** using the Black–Scholes framework and Monte Carlo simulation.

---

## 📘 Notebooks

### 1. `greeks_visualization.ipynb`
- Implements Black–Scholes pricing formulas for European calls and puts.
- Derives and visualizes the main option Greeks:
  - Delta (Δ), Gamma (Γ), Vega (ν), Theta (Θ), Rho (ρ).
- Produces **3D surfaces** and **2D cross-sections** showing how Greeks depend on:
  - Stock price relative to strike.
  - Time to maturity.
- Includes put–call parity checks and interpretations of Greek behavior (e.g. Gamma peaks near ATM, Vega grows with √T).

### 2. `delta_hedging.ipynb`
- Simulates stock price paths under **Geometric Brownian Motion (GBM)**.
- Implements a **discrete delta-hedging strategy**:
  - Start long 1 option, short Δ shares.
  - Rebalance stock position each step as Δ changes.
  - Track a self-financing cash account.
- At maturity:
  - Close the hedge.
  - Compare hedge performance vs option payoff.

