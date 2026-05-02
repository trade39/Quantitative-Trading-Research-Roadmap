# content.py
ROADMAP_DATA = {
    "Stage 1": {
        "title": "Foundation",
        "duration": "Months 1–3",
        "goal": "Build a deep intuition for market mechanics and the quant research cycle.",
        "overview": "Before writing a single line of code, you must understand the 'physics' of the markets. This stage is about moving from a retail mindset (guessing direction) to a quantitative mindset (analyzing probabilities and market structure).",
        "topics": [
            {
                "category": "Market Microstructure (The 'Why')",
                "items": [
                    "**The Limit Order Book (LOB):** How price actually moves. Understand the interaction between aggressive (market) and passive (limit) orders.",
                    "**Liquidity & Slippage:** Why a strategy that looks good on paper might fail when executed with size.",
                    "**Market Participants:** Identifying the footprint of Market Makers vs. Institutional Flow vs. Arbitrageurs.",
                    "**Asset Classes:** Comparing Equities, Futures (leverage/basis), and Options (volatility) mechanics."
                ]
            },
            {
                "category": "The Quantitative Mindset",
                "items": [
                    "**Alpha vs. Beta:** Distinguishing between general market movement and your unique 'edge'.",
                    "**Expected Value (EV):** Thinking in terms of Win Rate × Avg Win - Loss Rate × Avg Loss.",
                    "**The 4 Pillars of a Quant Lab:** Data → Research → Backtest → Execution."
                ]
            }
        ],
        "guide": [
            "1. **Study the Tape:** Open a platform like TradingView or ThinkOrSwim and watch the Level 2 (Depth of Market) for 30 minutes. Notice how big orders 'absorb' price.",
            "2. **Read 'Market Wizards':** Understand the psychological transition from 'gambling' to 'process-oriented' trading.",
            "3. **Learn the Lingo:** Define every term in the LOB: Bid-Ask Spread, Mid-price, Depth, and Imbalance."
        ],
        "exercise": "**The Spread Analysis:** Download 1 day of 1-minute OHLCV data for SPY. In Excel, calculate the average candle size. Research what the typical bid-ask spread is for SPY. Calculate what percentage of your 'candle' is eaten by the spread.",
        "milestone": "🎯 Complete the 'Financial Markets 101' certification and explain the LOB to someone who doesn't trade.",
        "resources": [
            "📖 Market Wizards — Jack Schwager",
            "📖 Quantitative Trading — Ernest Chan (Chapters 1-2)",
            "🎓 CME Group: Introduction to Futures"
        ]
    },
    "Stage 2": {
        "title": "Mathematics & Statistics",
        "duration": "Months 3–6",
        "goal": "Equip yourself with the statistical tools to separate signal from noise.",
        "overview": "Finance is 'noisy'. Most patterns you see are just random chance. This stage teaches you the 'Bullshit Detector'—the mathematical rigorousness required to prove an edge exists.",
        "topics": [
            {
                "category": "Probability & Distributions",
                "items": [
                    "**The Normal Distribution Myth:** Understanding why 'Fat Tails' (Kurtosis) cause most models to blow up during crashes.",
                    "**Log-Returns:** Why we use log-returns for modeling instead of simple price changes (additivity and symmetry).",
                    "**Conditional Probability:** Bayes' Theorem and its application in updating market bias."
                ]
            },
            {
                "category": "Time Series & Econometrics",
                "items": [
                    "**Stationarity:** Why you can't build a model on raw prices (they wander) and must use stationary data (returns).",
                    "**Cointegration:** The secret to Pairs Trading. Finding two assets that 'walk together' even if they drift apart.",
                    "**Hypothesis Testing:** Using P-values and T-stats to see if your backtest result is just 'luck'."
                ]
            }
        ],
        "guide": [
            "1. **Master the Histogram:** Plot the returns of Bitcoin vs. S&P 500. Observe the 'kurtosis' in Bitcoin—the extreme outliers.",
            "2. **Linear Algebra Basics:** Understand how matrices represent portfolios (Weights × Returns).",
            "3. **Statistical Significance:** Learn why a Sharpe Ratio of 1.0 requires at least 3 years of data to be statistically valid."
        ],
        "exercise": "**The Cointegration Search:** Pick two related stocks (e.g., KO and PEP). Use a simple spreadsheet or Python to plot their price ratio over 1 year. Identify 'mean-reverting' periods where the ratio stretched too far.",
        "milestone": "🎯 Pass the 'Statistics for Finance' module and build a spreadsheet that calculates Z-Scores for any price series.",
        "resources": [
            "📖 Statistics — Freedman, Pisani & Purves",
            "🎓 MIT 18.650: Statistics for Applications",
            "📖 Analysis of Financial Time Series — Ruey Tsay"
        ]
    },
    "Stage 3": {
        "title": "Programming & Data",
        "duration": "Months 6–9",
        "goal": "Build a professional-grade research environment using Python.",
        "overview": "A quant is only as good as their data and their ability to manipulate it. This stage transitions you from manual analysis to automated, vectorized research.",
        "topics": [
            {
                "category": "The Python Quant Stack",
                "items": [
                    "**Pandas Mastery:** Vectorization is king. If you use a 'for' loop in Pandas, you're doing it wrong. Learn `.apply()`, `.shift()`, and `.rolling()`.",
                    "**NumPy:** Fast numerical arrays for high-performance calculations.",
                    "**Visualization:** Using Plotly for interactive charts that allow you to zoom into specific trades."
                ]
            },
            {
                "category": "Data Engineering & Integrity",
                "items": [
                    "**ETL Pipelines:** Extract, Transform, Load. How to pull data from APIs (Alpaca, Polygon) and store it locally.",
                    "**Survivorship Bias:** Building a 'Point-in-Time' database so you don't test on stocks that only survived to today.",
                    "**Data Cleaning:** Handling 'fat-finger' errors and missing ticks in high-frequency data."
                ]
            }
        ],
        "guide": [
            "1. **Set up VS Code:** Move away from Jupyter for production code. Use a professional IDE with Git integration.",
            "2. **Build a Data Loader:** Write a script that downloads 5 years of daily data for the NASDAQ 100 and saves it to a Parquet file.",
            "3. **Learn Git:** Commit your code daily. Use branches for new strategy ideas."
        ],
        "exercise": "**The Vectorized Backtester:** Build a 10-line Python script using Pandas that calculates the performance of a 'Moving Average Crossover' strategy. No 'if' statements—use only vectorized logic.",
        "milestone": "🎯 Successfully build a local database that auto-updates every night with closing prices for 500 tickers.",
        "resources": [
            "📖 Python for Finance — Yves Hilpisch",
            "💻 'QuantConnect' Bootcamps (Free tutorials)",
            "📖 Python for Data Analysis — Wes McKinney"
        ]
    },
    "Stage 4": {
        "title": "Strategy Building",
        "duration": "Months 9–13",
        "goal": "Research and validate your first institutional-grade trading strategies.",
        "overview": "This is where the magic happens. You will combine market intuition, math, and code to find 'Alpha'—market inefficiencies that you can exploit for profit.",
        "topics": [
            {
                "category": "Alpha Generation",
                "items": [
                    "**Cross-Sectional Momentum:** Buying the 'winners' and selling the 'losers' across an index.",
                    "**Mean Reversion:** Trading 'stretched' rubber bands using RSI, Bollinger, or Z-Scores.",
                    "**Factor Models:** Decomposing returns into Size, Value, Quality, and Low Volatility components."
                ]
            },
            {
                "category": "The Backtesting Protocol",
                "items": [
                    "**Transaction Cost Modeling:** Implementing realistic slippage (0.01% - 0.05%) and commissions.",
                    "**Overfitting (p-hacking):** Understanding why testing 1,000 parameter combinations will always find a 'perfect' (but fake) backtest.",
                    "**Walk-Forward Optimization:** Testing on 'Unseen' data to ensure the strategy generalizes."
                ]
            }
        ],
        "guide": [
            "1. **Pick a Niche:** Don't try to trade everything. Choose one asset (e.g., FX) and one style (e.g., Trend).",
            "2. **Write a Strategy Thesis:** Before coding, write 1 paragraph explaining *why* this strategy should make money (e.g., 'It exploits the slow reaction of retail to news').",
            "3. **Analyze Drawdowns:** Look at the 'worst-case' periods. Could you have survived them mentally?"
        ],
        "exercise": "**The Alpha Hunt:** Research 'The Turn of the Month Effect' or 'The Monday Effect'. Use your Python tools to see if these seasonalities still exist in the S&P 500 today.",
        "milestone": "🎯 Create a 10-page 'Strategy Tear Sheet' including Sharpe, Max Drawdown, Win Rate, and Return Distribution.",
        "resources": [
            "📖 Algorithmic Trading — Ernest Chan",
            "📖 Expected Returns — Antti Ilmanen",
            "🎓 'WorldQuant University' free modules"
        ]
    },
    "Stage 5": {
        "title": "Advanced Quantitative Methods",
        "duration": "Months 13–19",
        "goal": "Master the machine learning and portfolio optimization techniques of top hedge funds.",
        "overview": "At this level, you move beyond simple rules to 'dynamic' models. You will learn how to use ML not for price prediction, but for risk management and signal combination.",
        "topics": [
            {
                "category": "Financial Machine Learning",
                "items": [
                    "**Labeling:** Moving beyond 'price-up/price-down' to the 'Triple Barrier Method'.",
                    "**Feature Engineering:** Building features from Order Flow, Sentiment, and Volatility surfaces.",
                    "**Purging & Embargoing:** Special cross-validation techniques to prevent data leakage in time series."
                ]
            },
            {
                "category": "Portfolio Construction",
                "items": [
                    "**Risk Parity:** Allocating based on 'Risk Contribution' rather than dollar amounts.",
                    "**Hierarchical Risk Parity (HRP):** Using graph theory to diversify portfolios more robustly.",
                    "**Black-Litterman:** Combining market equilibrium with your private views."
                ]
            }
        ],
        "guide": [
            "1. **Learn Scikit-Learn:** Master Random Forests and Gradient Boosting for classification tasks.",
            "2. **Study Volatility:** Understand 'GARCH' models to forecast when markets will become dangerous.",
            "3. **Factor Neutralization:** Learn how to hedge out 'Market Risk' so you only profit from your specific alpha."
        ],
        "exercise": "**The Regime Detector:** Build a K-Means clustering model in Python that categorizes the market into 3 states: 'Low Vol/Bull', 'High Vol/Bear', and 'Sideways/Chop'.",
        "milestone": "🎯 Implement a machine learning model that achieves a 'Precision' of >55% on out-of-sample directional signals.",
        "resources": [
            "📖 Advances in Financial Machine Learning — López de Prado",
            "📖 Options, Futures & Other Derivatives — John Hull",
            "💻 'QuantAcademy' Deep Learning courses"
        ]
    },
    "Stage 6": {
        "title": "Professional Mastery",
        "duration": "Month 19+",
        "goal": "Operate as a full-stack Quant Researcher capable of running institutional capital.",
        "overview": "The final stage is about infrastructure, scale, and longevity. You transition from a 'researcher' to a 'portfolio manager' who manages risk as much as they seek returns.",
        "topics": [
            {
                "category": "Institutional Execution",
                "items": [
                    "**Execution Algorithms:** VWAP, TWAP, and Implementation Shortfall. Minimizing your own market impact.",
                    "**OMS/EMS Design:** Building the 'Plumbing' that connects your research to the exchange securely.",
                    "**Real-time Monitoring:** Tracking 'Tracking Error' and 'Alpha Decay' in live trading."
                ]
            },
            {
                "category": "Advanced Risk & Psychology",
                "items": [
                    "**Tail Risk Hedging:** Using out-of-the-money options to protect against 'Black Swan' events.",
                    "**Capacity Analysis:** Determining at what AUM (Assets Under Management) your strategy stops working.",
                    "**The Professional Journal:** Documenting every model failure and iteration with academic rigor."
                ]
            }
        ],
        "guide": [
            "1. **Build a Production Pipeline:** Use Docker and AWS/GCP to run your research scripts on a schedule.",
            "2. **Network:** Start contributing to open-source quant libraries or publishing research on SSRN/arXiv.",
            "3. **Capital Allocation:** Learn the business of quant: how to pitch a strategy to a PM or Seed Fund."
        ],
        "exercise": "**The 'Flash Crash' Test:** Simulate how your current 'best' strategy would have performed during the 2010 Flash Crash or the 2020 COVID crash. Did it blow up?",
        "milestone": "🎯 Deploy a live 'Paper Trading' portfolio of 3+ diversified strategies and maintain a Sharpe > 1.5 for 6 months.",
        "resources": [
            "📖 Active Portfolio Management — Grinold & Kahn",
            "🎓 'Pioneers in Quantitative Finance' (Documentary/Series)",
            "📖 The Man Who Solved the Market — Gregory Zuckerman"
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
