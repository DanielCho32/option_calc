# tests/conftest.py
import sys, os

# Add the 'src' folder to sys.path so Python can find option_calc
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)
