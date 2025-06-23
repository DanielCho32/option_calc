# main.py

from us_option_pricing import us_option_binomial

def main():
    # Define option parameters
    S = 100      # Current stock price
    K = 100      # Strike price
    T = 1        # Time to expiration (in years)
    r = 0.05     # Annual risk-free interest rate (5%)
    sigma = 0.2  # Volatility of the underlying (20%)
    steps = 100  # Number of steps in binomial tree

    # Choose option type: 'call' or 'put'
    option_type = 'call'

    # Calculate the US option price
    price = us_option_binomial(S, K, T, r, sigma, steps, option_type)

    # Print result
    print(f"American {option_type.capitalize()} Option Price: ${price:.2f}")

if __name__ == "__main__":
    main()
