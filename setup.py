from setuptools import setup, find_packages

setup(
    name="ipl-analytics",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.5.0",
        "numpy>=1.23.0",
        "scikit-learn>=1.1.0",
        "matplotlib>=3.6.0",
        "seaborn>=0.12.0",
        "plotly>=5.10.0",
        "dash>=2.6.0",
        "pytest>=7.0.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A data analytics project for Indian Premier League cricket statistics",
    keywords="ipl, cricket, analytics, data science",
    python_requires=">=3.8",
)