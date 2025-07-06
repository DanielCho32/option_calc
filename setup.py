# setup.py
from setuptools import setup, find_packages

setup(
    name="option_calc",
    version="0.1.0",
    description="European & American Options Pricing Calculator with Greeks",
    author="Daniel Cho",
    author_email="cho.daniel32@gmail.com",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "streamlit",
        "numpy",
        "scipy",
        "matplotlib",
    ],
)
