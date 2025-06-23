#greeks.py

#
# File to give some more detail on what the Greeks actually mean in the context of a given option
#

from math import log, sqrt, exp
from scipy.stats import norm

# Helper Functions
def _d1(S, K, T, r, sigma):
    return (log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))

def _d2(S, K, T, r, sigma):
    return _d1(S, K, T, r, sigma) - sigma * sqrt(T)

# Greek Calculations
def delta(S, K, T, r, sigma, option_type='call'):
    d1 = _d1(S, K, T, r, sigma)
    if option_type == 'call':
        return norm.cdf(d1)
    elif option_type == 'put':
        return norm.cdf(d1) - 1

def gamma(S, K, T, r, sigma):
    d1 = _d1(S, K, T, r, sigma)
    return norm.pdf(d1) / (S * sigma * sqrt(T))

def vega(S, K, T, r, sigma):
    d1 = _d1(S, K, T, r, sigma)
    return S * norm.pdf(d1) * sqrt(T) / 100  # per 1% change in vol

def theta(S, K, T, r, sigma, option_type='call'):
    d1 = _d1(S, K, T, r, sigma)
    d2 = _d2(S, K, T, r, sigma)
    if option_type == 'call':
        return (-S * norm.pdf(d1) * sigma / (2 * sqrt(T)) - r * K * exp(-r * T) * norm.cdf(d2)) / 365
    elif option_type == 'put':
        return (-S * norm.pdf(d1) * sigma / (2 * sqrt(T)) + r * K * exp(-r * T) * norm.cdf(-d2)) / 365

def rho(S, K, T, r, sigma, option_type='call'):
    d2 = _d2(S, K, T, r, sigma)
    if option_type == 'call':
        return K * T * exp(-r * T) * norm.cdf(d2) / 100  # per 1% change in rate
    elif option_type == 'put':
        return -K * T * exp(-r * T) * norm.cdf(-d2) / 100

# Greeks Explanation

def explain_delta(delta_val):
    direction = "increase" if delta_val >= 0 else "decrease"
    return f"Delta: A $1 change in stock price will {direction} the option price by approximately ${abs(delta_val):.2f}."

def explain_gamma(gamma_val):
    return f"Gamma: For every $1 change in stock price, Delta changes by approximately {gamma_val:.4f}."

def explain_vega(vega_val):
    return f"Vega: A 1% increase in volatility will change the option price by approximately ${vega_val:.2f}."

def explain_theta(theta_val):
    return f"Theta: The option will lose approximately ${-theta_val:.2f} per day due to time decay."

def explain_rho(rho_val):
    direction = "increase" if rho_val >= 0 else "decrease"
    return f"Rho: A 1% rise in interest rate will {direction} the option price by approximately ${abs(rho_val):.2f}."
