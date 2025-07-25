from math import log, sqrt, exp
from scipy.stats import norm

def black_scholes_price(S, K, T, r, sigma, option_type='call'):
    '''
    Price a European option using the Black-Scholes model.

    Parameters:
        S (float): Stock price
        K (float): Strike price
        T (float): Time to maturity (years)
        r (float): Risk-free interest rate
        sigma (float): Volatility (standard deviation of returns)
        option_type (str): 'call' or 'put'

    Returns:
        float: Theoretical option price
    '''
    d1 = (log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)

    if option_type == 'call':
        return S * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        return K * exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")
