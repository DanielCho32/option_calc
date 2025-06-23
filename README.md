# Options Pricing & Greeks Calculator

A Python-based tool to calculate European and American option prices using the Black-Scholes and CRR binomial models respectively, as well as Greeks (Delta, Gamma, Vega, Theta, Rho).

## Features
- EU Call & Put option pricing
- US Call & Put option pricing
- Greeks computation
- Calculator UI & Volatility-Underlying Price heatmap in Streamlib
- #Interactive demo in Jupyter Notebook
- Modular structure

## Languages and Libraries
- Python - Core programming language
- NumPy - Numerical operations
- SciPy - Statistical functions and option pricing models
- Streamlib - Interactive UI
- Matplotlib - For plots

## What Are Options Greeks?

| Greek | Measures | Meaning |
|-------|----------|---------|
| **Delta (Δ)** | Sensitivity to stock price | Change in option price for a $1 change in stock price |
| **Gamma (Γ)** | Sensitivity of Delta | Change in Delta for a $1 change in stock price |
| **Theta (Θ)** | Time decay | How much value the option loses each day |
| **Vega (V)** | Sensitivity to volatility | Change in option price for a 1% change in volatility |
| **Rho (ρ)** | Sensitivity to interest rates | Change in option price for a 1% change in interest rate |

## Usage
```bash
pip install -r requirements.txt
python main.py
