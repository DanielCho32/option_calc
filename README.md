# Options Pricing & Greeks Calculator

A Python-based tool to calculate European option prices and Greeks (Delta, Gamma, Vega, Theta, Rho) using the Black-Scholes model.

## Features
- Call & put option pricing
- Greeks computation
- Interactive demo in Jupyter Notebook
- Modular structure (easy to extend to binomial models or Monte Carlo)

## Languages and Libraries
- Python - Core programming language
- NumPy - Numerical operations
- SciPy - Statistical functions and option pricing models
- Jupyter Notebook - Interactive demo
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
