# main.py

from us_option_pricing import us_option_binomial

def main():
    print("US Option Pricing Calculator\n")

    #Inputs
    S = float(input("Enter stock price (S): "))
    K = float(input("Enter strike price (K): "))
    T = float(input("Enter time to maturity (T in years): "))
    r = float(input("Enter annual risk-free rate (e.g. 0.05 for 5%): "))
    sigma = float(input("Enter volatility (e.g. 0.05 for 5%): "))
    steps = int(input("Enter number of binomial steps (e.g. 100): "))
    option_type = input("Enter option type ('call' or 'put'): ").lower().strip()

    # Calculate the US option price
    price = us_option_binomial(S, K, T, r, sigma, steps, option_type)

    # Print result
    print(f"\nUS {option_type.capitalize()} Option Price: ${price:.2f}")

if __name__ == "__main__":
    main()

