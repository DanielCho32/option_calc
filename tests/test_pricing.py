import pytest
from option_calc.eu_option_pricing import black_scholes_price
from option_calc.us_option_pricing import us_option_binomial
from option_calc.greeks import delta, gamma, vega, theta, rho

# ---------------------------------------------------
# Black-Scholes & Binomial Pricing Tests
# ---------------------------------------------------

@pytest.mark.parametrize("opt, expected", [
    ("call", 10.4506),
])
def test_black_scholes_call(opt, expected):
    price = black_scholes_price(100, 100, 1, 0.05, 0.2, option_type=opt)
    assert pytest.approx(expected, rel=1e-4) == price

def test_black_scholes_put():
    # Basic sanity for BS put
    price = black_scholes_price(100, 100, 1, 0.05, 0.2, option_type="put")
    assert pytest.approx(5.5735, rel=1e-4) == price

@pytest.mark.parametrize("opt", ["call"])
def test_binomial_call_convergence(opt):
    bs = black_scholes_price(100, 100, 1, 0.05, 0.2, option_type=opt)
    binom = us_option_binomial(100, 100, 1, 0.05, 0.2, steps=300, option_type=opt)
    assert pytest.approx(bs, rel=1e-2) == binom

def test_binomial_put_premium():
    bs_put = black_scholes_price(100, 100, 1, 0.05, 0.2, option_type="put")
    bin_put = us_option_binomial(100, 100, 1, 0.05, 0.2, steps=300, option_type="put")
    # American put should be ≥ European put
    assert bin_put >= bs_put

# ---------------------------------------------------
# Greeks Tests
# ---------------------------------------------------

def test_delta_call_minus_put_parity():
    d_call = delta(100, 100, 1, 0.05, 0.2, "call")
    d_put  = delta(100, 100, 1, 0.05, 0.2, "put")
    # For q=0, Δ_call - Δ_put ≈ 1
    assert pytest.approx(1.0, abs=1e-6) == d_call - d_put

def test_gamma_nonnegative():
    assert gamma(100, 100, 1, 0.05, 0.2) >= 0

def test_vega_positive():
    assert vega(100, 100, 1, 0.05, 0.2) > 0

@pytest.mark.parametrize("opt", ["call", "put"])
def test_theta_negative(opt):
    # Theta usually < 0 for long positions
    assert theta(100, 100, 1, 0.05, 0.2, opt) < 0

@pytest.mark.parametrize("opt", ["call", "put"])
def test_rho_sign(opt):
    r = rho(100, 100, 1, 0.05, 0.2, opt)
    # Call rho > 0, Put rho < 0
    if opt == "call":
        assert r > 0
    else:
        assert r < 0
