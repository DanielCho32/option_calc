# us_option_pricing.py

def us_option_binomial(S, K, T, r, sigma, steps, option_type):
    """
    Price a US option using the binomial tree model

    Parameters:
        S (float): Current stock price
        K (float): Strike price
        T (float): Time to expiration (in years)
        r (float): Annual risk-free interest rate
        sigma (float): Volatility (standard deviation of returns)
        steps (int): Number of steps in the binomial tree
        option_type (str): 'call' or 'put'

    Returns:
        float: Estimated price of the US option
    """
  
    from math import exp, sqrt

    dt = T / steps                       # Time per step
    u = exp(sigma * sqrt(dt))            # Up factor
    d = 1 / u                            # Down factor
    p = (exp(r * dt) - d) / (u - d)      # Risk-neutral probability

    # Final asset prices at maturity
    asset_prices = [S * (u ** j) * (d ** (steps - j)) for j in range(steps + 1)]

    # Option payoffs at maturity
    if option_type == 'call':
        option_values = [max(price - K, 0) for price in asset_prices]
    elif option_type == 'put':
        option_values = [max(K - price, 0) for price in asset_prices]
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    # Backward induction to calculate option price
    for i in range(steps - 1, -1, -1):
        for j in range(i + 1):
            asset_price = S * (u ** j) * (d ** (i - j))
            continuation_value = exp(-r * dt) * (p * option_values[j + 1] + (1 - p) * option_values[j])

            if option_type == 'call':
                option_values[j] = max(asset_price - K, continuation_value)
            else:
                option_values[j] = max(K - asset_price, continuation_value)

    return option_values[0]
