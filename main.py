# main.py

# Imports
from us_option_pricing import us_option_binomial
from eu_pricing import black_scholes_price
from greeks import delta, gamma, vega, theta, rho
from greeks import explain_delta, explain_gamma, explain_vega, explain_theta, explain_rho

def main():
    print("Option Pricing Calculator\n")

    # Inputs
    model_choice = input("Choose option ('american' or 'european'): ").strip().lower()
    if model_choice not in ['american', 'european']:
        print("Invalid model type. Please type 'american' or 'european'.")
        return
        
    S = float(input("Enter stock price (S): "))
    K = float(input("Enter strike price (K): "))
    T = float(input("Enter time to maturity (T in years): "))
    r = float(input("Enter annual risk-free rate (e.g. 0.05 for 5%): "))
    sigma = float(input("Enter volatility (e.g. 0.05 for 5%): "))
    option_type = input("Enter option type ('call' or 'put'): ").lower().strip()
    if option_type not in ['call', 'put']:
        print("Invalid option type. Please type 'call' or 'put'.")
        return

    # Model Choice
    if model_choice == 'american':
        steps = int(input("Enter number of binomial steps (e.g. 100): "))
        price = us_option_binomial(S, K, T, r, sigma, steps, option_type)
        print(f"\n Estimated US {option_type.capitalize()} Option Price: ${price:.2f}")
    else:
        price = black_scholes_price(S, K, T, r, sigma, option_type)
        print(f"\n Estimated EU {option_type.capitalize()} Option Price (Black-Scholes): ${price:.2f}")

    # Greeks
    d = delta(S, K, T, r, sigma, option_type)
    g = gamma(S, K, T, r, sigma)
    v = vega(S, K, T, r, sigma)
    t = theta(S, K, T, r, sigma, option_type)
    rh = rho(S, K, T, r, sigma, option_type)  

    # Greeks Explanation
    print("\n Option Greeks Explanation:")
    print(explain_delta(d))
    print(explain_gamma(g))
    print(explain_vega(v))
    print(explain_theta(t))
    print(explain_rho(rh))

if __name__ == "__main__":
    main()

