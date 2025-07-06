#IMPORTS

# Main Page
import streamlit as st
from option_calc.us_option_pricing import us_option_binomial
from option_calc.eu_option_pricing import black_scholes_price
from option_calc.greeks import delta, gamma, vega, theta, rho
from option_calc.greeks import explain_delta, explain_gamma, explain_vega, explain_theta, explain_rho

# Heatmap
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import io

# Logic
st.set_page_config(page_title="Options Pricing & Greeks Calculator", layout="wide")

st.title("Options Pricing & Greeks Calculator")
st.write("This tool calculates European (Black-Scholes) and American (Binomial Tree) option prices and Greeks.")

st.sidebar.header("Input Parameters")
model_choice = st.sidebar.selectbox("Option Model", ["European", "American"])
S = st.sidebar.number_input("Stock Price (S)", value=100.0)
K = st.sidebar.number_input("Strike Price (K)", value=100.0)

time_input_mode = st.sidebar.radio("How would you like to input time to maturity?", ["Years", "Days"])

if time_input_mode == "Years":
    T = st.sidebar.number_input("Time to Maturity (T) in Years", min_value=0.0001, value=1.0000, step=0.0001, format="%.4f")
else:
    days_to_expiry = st.sidebar.number_input("Days to Expiry", min_value=1, value=365)
    T = days_to_expiry / 365.0

# Risk-Free Rate
r_input = st.sidebar.number_input("Risk-Free Rate (r) in %", value=5.0, min_value=0.0, max_value=100.0, step=0.01)
r = r_input / 100.0  # convert percentage to decimal
st.sidebar.caption("Example: enter 5.25 for 5.25% annualized rate")

# Volatility
sigma_input = st.sidebar.number_input("Volatility (σ) in %", value=20.0, min_value=0.01, max_value=500.0, step=0.1)
sigma = sigma_input / 100.0  # convert percentage to decimal
st.sidebar.caption("Example: enter 140.5 for 140.5% implied volatility")

if model_choice == "American":
    steps = st.sidebar.slider("Binomial Steps (for American Option)", min_value=10, max_value=500, value=100)
else:
    steps = None 


st.markdown("---")

if model_choice == "European":
    st.subheader("EU Option Prices (Black-Scholes)")
    call_price = black_scholes_price(S, K, T, r, sigma, "call")
    put_price = black_scholes_price(S, K, T, r, sigma, "put")
    st.write(f"**Call Price**: ${call_price:.2f}")
    st.write(f"**Put Price**: ${put_price:.2f}")

elif model_choice == "American":
    st.subheader("US Option Prices (Binomial Tree)")
    call_price = us_option_binomial(S, K, T, r, sigma, steps, "call")
    put_price = us_option_binomial(S, K, T, r, sigma, steps, "put")
    st.write(f"**Call Price**: ${call_price:.2f}")
    st.write(f"**Put Price**: ${put_price:.2f}")

st.markdown("---")
greek_option = st.selectbox("▶Select Option Type for Greeks", ["Call", "Put"])

greek_type = greek_option.lower()
d = delta(S, K, T, r, sigma, greek_type)
g = gamma(S, K, T, r, sigma)
v = vega(S, K, T, r, sigma)
t = theta(S, K, T, r, sigma, greek_type)
rh = rho(S, K, T, r, sigma, greek_type)

st.subheader("Greeks")
st.markdown(f"**Delta**: {d:.4f}")
st.markdown(f"**Gamma**: {g:.4f}")
st.markdown(f"**Vega**: {v:.4f}")
st.markdown(f"**Theta**: {t:.4f}")
st.markdown(f"**Rho**: {rh:.4f}")

with st.expander("◆ What do these Greeks mean?"):
    st.text(explain_delta(d))
    st.text(explain_gamma(g))
    st.text(explain_vega(v))
    st.text(explain_theta(t))
    st.text(explain_rho(rh))


#HEATMAP EU

# --- Black-Scholes formula functions ---
def black_scholes_call_price(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def black_scholes_put_price(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# Prepare grid
S_vals   = np.linspace(S * 0.5, S * 1.5, 100)
sigma_vals = np.linspace(0.01, 1.0, 100)
S_grid, sigma_grid = np.meshgrid(S_vals, sigma_vals)

# Compute prices according to the master option_type
price_grid = np.zeros_like(S_grid)
for i in range(price_grid.shape[0]):
    for j in range(price_grid.shape[1]):
        spot  = S_grid[i, j]
        vol   = sigma_grid[i, j]
        if greek_option == "Call":
            price_grid[i, j] = black_scholes_call_price(spot, K, T, r, vol)
        else:
            price_grid[i, j] = black_scholes_put_price(spot, K, T, r, vol)

# Plot
fig, ax = plt.subplots(figsize=(6, 4), dpi=50)
c = ax.contourf(S_grid, sigma_grid, price_grid, levels=50, cmap="RdYlGn")
ax.set_title(f"{greek_option} Option Price Heatmap")
ax.set_xlabel("Stock Price (S)")
ax.set_ylabel("Volatility (σ)")
fig.colorbar(c, label="Option Price")

buf = io.BytesIO()
fig.savefig(buf, format="png", dpi=200)  # save at 80 dpi
buf.seek(0)
st.image(buf, width=900)

#PNL HEATMAP
