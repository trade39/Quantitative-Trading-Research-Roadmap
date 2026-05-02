ROADMAP_DATA = {
    "Stage 1": {
        "title": "Foundation",
        "duration": "Months 1–3",
        "goal": "Understand what quantitative trading is and how markets work.",
        "topics": [
            {
                "category": "Financial Markets Literacy",
                "items": [
                    "How exchanges work (order matching, market microstructure)",
                    "Asset classes: equities, futures, options, forex, crypto",
                    "Market participants: market makers, HFTs, institutional traders",
                    "Order types: market, limit, stop, MOC, IOC"
                ]
            },
            {
                "category": "Core Finance Concepts",
                "items": [
                    "Time value of money, compounding, discounting",
                    "Risk vs. return tradeoff",
                    "Portfolio theory basics (diversification, correlation)",
                    "What alpha and beta mean in practice",
                    "Key metrics: Sharpe ratio, drawdown, CAGR, win rate"
                ]
            },
            {
                "category": "Introduction to Quantitative Trading",
                "items": [
                    "Discretionary vs. systematic vs. algorithmic trading",
                    "Types of quant strategies: trend following, mean reversion, stat arb, market making",
                    "The strategy lifecycle: research → backtest → paper trade → live deploy",
                    "Understanding the research process and its pitfalls"
                ]
            }
        ],
        "resources": [
            "📖 Market Wizards — Jack Schwager",
            "📖 Quantitative Trading — Ernest Chan (first 3 chapters)",
            "🎓 CME Group free courses on futures markets"
        ]
    },
    "Stage 2": {
        "title": "Mathematics & Statistics",
        "duration": "Months 3–6",
        "goal": "Build the quantitative toolkit that underpins every strategy.",
        "topics": [
            {
                "category": "Linear Algebra",
                "items": [
                    "Vectors, matrices, dot products",
                    "Matrix decomposition (eigenvalues, PCA)",
                    "Applications: portfolio optimization, factor models"
                ]
            },
            {
                "category": "Probability & Statistics",
                "items": [
                    "Probability distributions (normal, log-normal, fat tails)",
                    "Descriptive stats: mean, variance, skewness, kurtosis",
                    "Hypothesis testing: p-values, t-tests, confidence intervals",
                    "Correlation vs. causation — critical in finance"
                ]
            },
            {
                "category": "Time Series Analysis",
                "items": [
                    "Stationarity and the ADF test",
                    "Autocorrelation (ACF/PACF)",
                    "ARIMA models",
                    "Cointegration and pairs trading foundation"
                ]
            },
            {
                "category": "Calculus & Optimization",
                "items": [
                    "Derivatives and gradients (for optimization)",
                    "Gradient descent fundamentals",
                    "Constrained optimization (Lagrangian) for portfolio construction"
                ]
            },
            {
                "category": "Financial Statistics",
                "items": [
                    "Returns vs. log-returns and why it matters",
                    "Fat tails and non-normality of financial data",
                    "Rolling statistics and regime detection"
                ]
            }
        ],
        "resources": [
            "📖 Statistics — Freedman, Pisani & Purves",
            "🎓 MIT OpenCourseWare 18.650 (Statistics for Applications)",
            "📖 Analysis of Financial Time Series — Ruey Tsay"
        ]
    },
    "Stage 3": {
        "title": "Programming & Data",
        "duration": "Months 6–9",
        "goal": "Turn mathematical ideas into working research tools.",
        "topics": [
            {
                "category": "Python Mastery for Quants",
                "items": [
                    "NumPy: numerical computation",
                    "Pandas: time series & data wrangling",
                    "Matplotlib/Plotly: visualization",
                    "SciPy: statistical functions",
                    "Statsmodels: econometrics & time series",
                    "scikit-learn: machine learning baseline"
                ]
            },
            {
                "category": "Data Engineering Skills",
                "items": [
                    "Working with OHLCV data, tick data, order book data",
                    "Handling corporate actions: splits, dividends, survivorship bias",
                    "Data cleaning: missing values, outliers, timezone alignment",
                    "Building a local research database (SQLite → PostgreSQL)",
                    "APIs: yFinance, Alpaca, Polygon.io, Quandl"
                ]
            },
            {
                "category": "Backtesting Fundamentals",
                "items": [
                    "Building a vectorized backtester from scratch",
                    "Understanding look-ahead bias (#1 beginner mistake)",
                    "Transaction costs: commissions, slippage, market impact",
                    "Vectorized vs. event-driven backtesting (Backtrader, Zipline, bt)"
                ]
            },
            {
                "category": "Version Control & Workflow",
                "items": [
                    "Git basics: branching, commits, pull requests",
                    "Jupyter Notebooks for research",
                    "Structuring a quant research project cleanly"
                ]
            }
        ],
        "milestone": "🎯 Build a simple moving average crossover strategy end-to-end: data ingestion → signal generation → backtesting → performance report",
        "resources": [
            "📖 Python for Finance — Yves Hilpisch"
        ]
    },
    "Stage 4": {
        "title": "Strategy Building",
        "duration": "Months 9–13",
        "goal": "Research, develop, and validate real trading strategies.",
        "topics": [
            {
                "category": "Signal Research & Alpha Generation",
                "items": [
                    "Momentum signals: time-series momentum, cross-sectional momentum",
                    "Mean reversion signals: RSI, Bollinger Bands, z-score pairs",
                    "Value signals: P/E, P/B, earnings yield",
                    "Quality signals: ROE, profit margins, accruals",
                    "Alternative data signals: sentiment, earnings call NLP, satellite data"
                ]
            },
            {
                "category": "Strategy Categories",
                "items": [
                    "Trend Following: Time series, position sizing",
                    "Statistical Arbitrage: Cointegration, execution speed",
                    "Factor Investing: Cross-sectional regression",
                    "Market Making: Microstructure, inventory risk",
                    "Event-Driven: NLP, fast data pipelines"
                ]
            },
            {
                "category": "Backtesting Best Practices",
                "items": [
                    "Walk-forward optimization vs. in-sample overfitting",
                    "Monte Carlo simulation for robustness",
                    "Deflated Sharpe Ratio — accounting for multiple testing",
                    "Out-of-sample testing protocols",
                    "Regime analysis: bull/bear/volatile markets"
                ]
            },
            {
                "category": "Risk & Position Sizing",
                "items": [
                    "Kelly Criterion and fractional Kelly",
                    "Volatility targeting / position scaling",
                    "Correlation-aware portfolio construction",
                    "Stop-loss design and drawdown limits"
                ]
            }
        ],
        "milestone": "🎯 Research a stat arb pairs trading strategy: find cointegrated pairs, build spread model, backtest with realistic costs, stress test across regimes",
        "resources": [
            "📖 Algorithmic Trading — Ernest Chan"
        ]
    },
    "Stage 5": {
        "title": "Advanced Quantitative Methods",
        "duration": "Months 13–19",
        "goal": "Master institutional-grade techniques used by hedge funds.",
        "topics": [
            {
                "category": "Machine Learning for Trading",
                "items": [
                    "Supervised learning: XGBoost, LightGBM",
                    "Feature engineering from financial data",
                    "Avoiding overfitting: cross-validation with purging & embargoing",
                    "Unsupervised learning: clustering for regime detection",
                    "Neural networks: LSTM, Temporal Convolutional Networks"
                ]
            },
            {
                "category": "Portfolio Construction & Optimization",
                "items": [
                    "Mean-Variance Optimization and real-world failures",
                    "Black-Litterman model",
                    "Risk parity and equal risk contribution",
                    "Hierarchical Risk Parity (HRP)",
                    "Factor neutralization and beta hedging"
                ]
            },
            {
                "category": "Derivatives & Options Quant",
                "items": [
                    "Black-Scholes model and Greeks (Δ, Γ, Θ, Vega, Rho)",
                    "Volatility surface modeling: implied vs. realized vol",
                    "Options strategies: vol trading, dispersion, gamma scalping",
                    "Stochastic calculus: Brownian motion, Itô's lemma"
                ]
            },
            {
                "category": "Execution & Market Microstructure",
                "items": [
                    "VWAP, TWAP, implementation shortfall algorithms",
                    "Adverse selection and toxic order flow (VPIN)",
                    "Bid-ask spread decomposition",
                    "Latency and its real impact on P&L"
                ]
            },
            {
                "category": "Alternative Data & NLP",
                "items": [
                    "Sentiment analysis on earnings calls and news",
                    "SEC filings parsing (10-K, 8-K)",
                    "Web scraping with ethical practices",
                    "Large language models as signal generators"
                ]
            }
        ],
        "resources": [
            "📖 Advances in Financial Machine Learning — López de Prado",
            "📖 Options, Futures & Other Derivatives — John Hull"
        ]
    },
    "Stage 6": {
        "title": "Professional Mastery",
        "duration": "Month 19+",
        "goal": "Think and operate at the level of a professional quant researcher.",
        "topics": [
            {
                "category": "Research Process Excellence",
                "items": [
                    "Formulating falsifiable hypotheses",
                    "Keeping a rigorous research journal",
                    "Building a strategy library with documented edge decay",
                    "Capacity analysis: AUM absorption limits"
                ]
            },
            {
                "category": "Risk Management at Scale",
                "items": [
                    "Value at Risk (VaR) and Conditional VaR",
                    "Stress testing: 2008 GFC, COVID crash, flash crashes",
                    "Tail risk hedging",
                    "Correlation breakdown in crisis periods"
                ]
            },
            {
                "category": "Live Trading Infrastructure",
                "items": [
                    "Paper trading → live deployment pipeline",
                    "Real-time signal generation architecture",
                    "Order management systems (OMS)",
                    "Monitoring dashboards: P&L attribution, risk metrics"
                ]
            },
            {
                "category": "Soft Skills",
                "items": [
                    "Intellectual honesty: Alpha vs. Data mining",
                    "Communication: presenting to non-technical stakeholders",
                    "Collaboration with PMs and traders",
                    "Continuous academic reading (SSRN, arXiv)"
                ]
            }
        ],
        "resources": [
            "📖 Active Portfolio Management — Grinold & Kahn",
            "🎓 Academic papers on SSRN (free)"
        ]
    }
}

TRAPS = [
    {"title": "Look-ahead bias", "description": "Using future data in your signals unknowingly."},
    {"title": "Overfitting", "description": "Optimizing parameters until the backtest looks perfect."},
    {"title": "Survivorship bias", "description": "Only testing on stocks that still exist today."},
    {"title": "Ignoring costs", "description": "A 1% annual edge disappears with realistic transaction costs."},
    {"title": "Neglecting regime changes", "description": "A strategy working 2010–2020 may be dead today."}
]

TOOLS_CHECKLIST = {
    "Stage 1-2": ["Excel/Sheets", "Basic Python", "yFinance"],
    "Stage 3-4": ["Pandas", "Zipline/Backtrader", "PostgreSQL", "Git"],
    "Stage 5": ["scikit-learn", "PyTorch/TF", "QuantLib", "Interactive Brokers API"],
    "Stage 6": ["Custom execution infra", "Bloomberg/Refinitiv", "AWS/GCP"]
}
