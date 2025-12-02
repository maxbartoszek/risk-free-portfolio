# risk-free-portfolio
Low-Risk Portfolio Generator

A minimum-variance, stability-weighted equity portfolio engine built in Python.

This project implements a fully automated risk-free style portfolio builder, using real market data, factor scoring, and convex optimization. We delivered a portfolio with:
* 1.34% weekly volatility
* 1.6 Sharpe ratio
Extremely stable performance during choppy market conditions

What This Model Does

This pipeline generates a minimum-variance portfolio using real North American equities. It includes:

1. Data Ingestion & Cleaning
* Uses yfinance
* Minimizes portfolio variance: to pull historical prices
* Converts adjusted close prices to returns
* Handles missing values and delisted tickers
* Filters out invalid or empty data

2. Stability Factor Computation
For each ticker, the model computes:
|     Factor     |             Purpose                 |
|   Volatility   |      Measures day-to-day risk       |
|      Beta      |      Measures market sensitivity    |
|   Market Cap   |      Stability & size proxy         |

3. Custom Stability Scoring
* Low volatility → higher score
* Low beta → higher score
* Large market cap → higher score

4. Portfolio Optimization (CVXPY)
Minimizes portfolio variance:
Subject to:
w ≥ 0 (long-only)
∑𝑤 =1
This produces a true minimum-variance portfolio.

5. Performance Analysis
* Rolling returns
* Cumulative value
* Weekly volatility
* Sharpe ratio
* Equity curve visualization

6. Results Summary
The optimized portfolio delivered:
* Smooth return path
* Low sensitivity to market movements
* Minimal drawdowns
* Strong risk-adjusted performance
This aligns closely with the expected behaviour of a low-risk or risk-free equity strategy.
