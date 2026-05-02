# content.py

ROADMAP_DATA = {
    "Stage 1": {
        "title": "Market Microstructure & Order Flow",
        "duration": "Months 1–2",
        "difficulty": "Beginner",
        "reading_time": "20h",
        "prereqs": "None",
        "goal": "Understand the mechanics of how orders are matched and how liquidity moves price.",
        "overview": "Every trade on a modern exchange happens within the Limit Order Book (LOB). This stage strips away indicators to show you the raw physics of the market: how bids and asks interact to create the price action we see on charts.",
        "category": "Foundations",
        "guide": [
            "1. <b>Study the Tape:</b> Open a platform like TradingView or ThinkOrSwim and watch the Level 2 (Depth of Market) for 30 minutes. Notice how big orders 'absorb' price.",
            "2. <b>Read 'Market Wizards':</b> Understand the psychological transition from 'gambling' to 'process-oriented' trading.",
            "3. <b>Learn the Lingo:</b> Define every term in the LOB: Bid-Ask Spread, Mid-price, Depth, and Imbalance."
        ],
        "exercise": {
            "title": "The Spread Analysis",
            "description": "Download 1 day of 1-minute OHLCV data for SPY. Calculate the average candle size and determine what percentage of your 'candle' is eaten by a standard 1-cent bid-ask spread.",
            "scaffold": "import pandas as pd\n\n# Sample data generation\ndata = {'close': [150.00, 150.05, 150.02, 150.08, 150.10], 'high': [150.07, 150.08, 150.10, 150.15, 150.12], 'low': [149.95, 150.00, 149.98, 150.05, 150.08]}\ndf = pd.DataFrame(data)\n\n# Calculate candle size (High - Low)\ndf['candle_size'] = df['high'] - df['low']\navg_candle = df['candle_size'].mean()\n\n# Assume spread of $0.01\nspread = 0.01\nimpact = (spread / avg_candle) * 100\n\nprint(f'Average Candle Size: ${avg_candle:.4f}')\nprint(f'Spread Impact: {impact:.2f}%')\n"
        },
        "milestone": "🎯 Complete the 'Financial Markets 101' certification and explain the LOB to someone who doesn't trade.",
        "common_mistakes": [
            "Confusing price action with market direction: Seeing a candle go up does not mean the market is bullish — check the volume and LOB depth behind it.",
            "Treating all markets identically: The mechanics of a futures contract are fundamentally different from equities. Don't apply equity intuition to FX or commodities without research.",
            "Skipping the microstructure layer: Most retail traders jump straight to indicators. Without understanding who's on the other side of your trade, you are trading blind.",
            "Underestimating transaction costs: A 0.05% per-trade cost sounds tiny but can erase an entire year of alpha in a high-frequency strategy."
        ],
        "quiz_bank": [
            {
                "question": "Which participant type typically provides liquidity by placing limit orders at both the bid and the ask?",
                "options": ["High-Frequency Takers", "Market Makers", "Retail Speculators", "Institutional Buyers"],
                "answer": 1,
                "explanation": "Market Makers profit from the bid-ask spread and provide liquidity by sitting on both sides of the Limit Order Book (LOB)."
            },
            {
                "question": "If you buy 1,000 shares but only 500 are available at your price, and the next 500 are 2 cents higher, what have you experienced?",
                "options": ["Arbitrage", "Alpha", "Slippage", "Basis Risk"],
                "answer": 2,
                "explanation": "Slippage is the difference between your intended price and the actual execution price, usually caused by lack of depth in the LOB."
            },
            {
                "question": "What is the 'mid-price' in the context of the Limit Order Book?",
                "options": ["The price of the last trade", "The average of the best bid and best ask", "The price with the highest volume", "The opening price of the day"],
                "answer": 1,
                "explanation": "The mid-price is the mathematical center between the best available buy order (bid) and the best available sell order (ask)."
            },
            {
                "question": "In a 'Flash Crash', why does price typically gap down vertically?",
                "options": ["Market makers double their quotes", "Market makers pull their quotes to avoid toxic flow", "Retail traders buy the dip too early", "Exchanges increase the spread"],
                "answer": 1,
                "explanation": "During extreme volatility, market makers often withdraw liquidity to protect themselves, leaving a vacuum that causes price to gap down."
            },
            {
                "question": "Which of these is a 'non-linear' bet on volatility?",
                "options": ["Equities", "Futures", "Options", "Spot FX"],
                "answer": 2,
                "explanation": "Options have non-linear payoffs (convexity) and their value changes based on volatility (Vega), unlike linear instruments like stocks or futures."
            }
        ],
        "resources": [
            {"icon": "📖", "name": "Market Wizards — Jack Schwager", "url": "https://www.amazon.com/Market-Wizards-Interviews-Top-Traders/dp/1592803377"},
            {"icon": "📖", "name": "Quantitative Trading — Ernest Chan (Ch. 1-2)", "url": "https://www.amazon.com/Quantitative-Trading-Build-Algorithmic-Business/dp/1119800064"},
            {"icon": "🎓", "name": "CME Group: Introduction to Futures", "url": "https://www.cmegroup.com/education/courses/introduction-to-futures.html"},
            {"icon": "🎓", "name": "Yale: Financial Markets (Shiller) — Coursera", "url": "https://www.coursera.org/learn/financial-markets-global"},
            {"icon": "🌐", "name": "Investopedia: Limit Order Book Explained", "url": "https://www.investopedia.com/terms/l/limitorderbook.asp"},
            {"icon": "💻", "name": "Jigsaw Trading: Order Flow & DOM Training", "url": "https://www.jigsawtrading.com/"}
        ],
        "glossary": [
            {"term": "Limit Order Book (LOB)", "definition": "A record of all outstanding limit orders for a financial instrument, showing depth at each price level."},
            {"term": "Liquidity", "definition": "The ability to trade an asset quickly without causing a significant price change."},
            {"term": "Mid-Price", "definition": "The average of the best bid and best ask prices in the order book."}
        ]
    },
    "Stage 2": {
        "title": "Statistics & Probability in Finance",
        "duration": "Months 2–4",
        "difficulty": "Intermediate",
        "reading_time": "35h",
        "prereqs": "Basic Algebra",
        "goal": "Master the mathematical tools used to quantify edge and detect noise.",
        "overview": "Finance is the study of uncertainty. To be a quant, you must speak the language of probability. This stage covers the distribution of returns, the reality of fat-tails (Kurtosis), and why standard statistics often fail in financial markets.",
        "category": "Foundations",
        "guide": [
            "1. <b>Master the Histogram:</b> Plot the returns of Bitcoin vs. S&P 500. Observe the 'kurtosis' in Bitcoin—the extreme outliers.",
            "2. <b>Linear Algebra Basics:</b> Understand how matrices represent portfolios (Weights × Returns).",
            "3. <b>Statistical Significance:</b> Learn why a Sharpe Ratio of 1.0 requires at least 3 years of data to be statistically valid."
        ],
        "exercise": {
            "title": "The Statistical Bullshit Detector",
            "description": "Calculate the Log-Returns of a price series and check for 'Fat Tails' by comparing the distribution to a Normal curve.",
            "scaffold": "import numpy as np\nimport pandas as pd\nfrom scipy.stats import kurtosis, norm\n\n# Generate price data\nprices = 100 * np.exp(np.cumsum(np.random.normal(0, 0.01, 1000)))\n\n# Calculate Log-Returns\nlog_returns = np.log(prices[1:] / prices[:-1])\n\n# Measure Kurtosis (Normal distribution = 0)\nkurt = kurtosis(log_returns)\n\nprint(f'Kurtosis: {kurt:.2f}')\nif kurt > 0:\n    print('Market exhibits Fat Tails (Leptokurtic)')\nelse:\n    print('Market exhibits Thin Tails')\n"
        },
        "milestone": "🎯 Pass the 'Statistics for Finance' module and build a spreadsheet that calculates Z-Scores for any price series.",
        "common_mistakes": [
            "Assuming normality everywhere: Using a z-score alert system that assumes normal returns will catastrophically misfire during fat-tail events like crashes or squeezes.",
            "P-hacking without knowing it: Running 30 different correlation tests on the same dataset will inevitably surface a 'significant' result by pure chance.",
            "Regressing non-stationary series: Running OLS on raw prices (not returns) produces spurious $R^2$ values that evaporate in live trading.",
            "Ignoring the Multiple Testing Problem: In finance, statistical significance thresholds must be adjusted (Bonferroni, BHY) when testing many strategies simultaneously."
        ],
        "quiz_bank": [
            {
                "question": "Why do quants use Log-Returns instead of simple percentage returns for time-series modeling?",
                "options": ["They are more accurate", "They are time-additive", "They prevent losses", "They are easier to calculate"],
                "answer": 1,
                "explanation": "Log-returns ($ln(P_t/P_{t-1})$) are additive over time, meaning the return of two days is simply the sum of their individual log-returns."
            },
            {
                "question": "If two non-stationary price series have a linear combination that is stationary, they are said to be:",
                "options": ["Correlated", "Vectorized", "Cointegrated", "Normally Distributed"],
                "answer": 2,
                "explanation": "Cointegration is a statistical property where two 'drifting' variables never stay too far apart, forming the basis of pairs trading."
            },
            {
                "question": "What does a high positive Kurtosis (Fat Tails) imply for a trading strategy?",
                "options": ["Profits are guaranteed", "Extreme outliers (crashes/moons) happen more often than a normal curve predicts", "The market is perfectly efficient", "Price follows a linear trend"],
                "answer": 1,
                "explanation": "High kurtosis means 'rare' events happen much more frequently than standard models suggest, which can lead to 'Black Swan' losses if not managed."
            },
            {
                "question": "In Bayesian updating, what is the 'Posterior' probability?",
                "options": ["The probability before seeing new data", "The probability after updating beliefs with new evidence", "The probability of a coin toss", "The probability of a market open"],
                "answer": 1,
                "explanation": "The Posterior is the revised probability of an event happening, given the 'Prior' belief and the new 'Evidence' (Bayes Theorem)."
            }
        ],
        "resources": [
            {"icon": "📖", "name": "Statistics — Freedman, Pisani & Purves", "url": "https://www.amazon.com/Statistics-4th-David-Freedman/dp/0393929728"},
            {"icon": "🎓", "name": "MIT 18.650: Statistics for Applications", "url": "https://ocw.mit.edu/courses/18-650-statistics-for-applications-fall-2016/"},
            {"icon": "📖", "name": "Analysis of Financial Time Series — Ruey Tsay", "url": "https://www.amazon.com/Analysis-Financial-Time-Series-Tsay/dp/0470414359"},
            {"icon": "🎓", "name": "Khan Academy: Statistics & Probability", "url": "https://www.khanacademy.org/math/statistics-probability"},
            {"icon": "🌐", "name": "QuantLib: Open Source Quant Library", "url": "https://www.quantlib.org/"}
        ],
        "glossary": [
            {"term": "Stationarity", "definition": "A property of a time series where statistical properties like mean and variance remain constant over time."},
            {"term": "Kurtosis", "definition": "A measure of the 'tailedness' of a probability distribution; high kurtosis indicates frequent outliers."},
            {"term": "P-Value", "definition": "The probability of obtaining results at least as extreme as the observed results, assuming the null hypothesis is true."}
        ]
    },
    "Stage 3": {
        "title": "Data Engineering & Python for Quants",
        "duration": "Months 3–5",
        "difficulty": "Intermediate",
        "reading_time": "40h",
        "prereqs": "Stage 1, Stage 2",
        "goal": "Build a professional research environment and master vectorized data processing.",
        "overview": "Alpha is hidden in data. If you can't process millions of rows efficiently, you can't find it. This stage transitions you from a 'coder' to a 'data engineer,' focusing on high-performance Python (NumPy/Pandas) and robust data pipelines.",
        "category": "Foundations",
        "guide": [
            "1. <b>Set up VS Code:</b> Move away from Jupyter for production code. Use a professional IDE with Git integration.",
            "2. <b>Build a Data Loader:</b> Write a script that downloads 5 years of daily data for the NASDAQ 100 and saves it to a Parquet file.",
            "3. <b>Learn Git:</b> Commit your code daily. Use branches for new strategy ideas."
        ],
        "exercise": {
            "title": "The Vectorized Backtester",
            "description": "Calculate the performance of a 'Moving Average Crossover' strategy using vectorized Pandas logic (no loops).",
            "scaffold": "import pandas as pd\nimport numpy as np\n\n# Generate dummy data\ndates = pd.date_range('2023-01-01', periods=100)\nprices = 100 + np.cumsum(np.random.randn(100))\ndf = pd.DataFrame({'price': prices}, index=dates)\n\n# Calculate Moving Averages\ndf['SMA_20'] = df['price'].rolling(20).mean()\ndf['SMA_50'] = df['price'].rolling(50).mean()\n\n# Vectorized signal: 1 if SMA_20 > SMA_50, else 0\ndf['signal'] = np.where(df['SMA_20'] > df['SMA_50'], 1, 0)\n\n# Calculate returns\ndf['returns'] = df['price'].pct_change()\ndf['strategy_returns'] = df['signal'].shift(1) * df['returns']\n\ncum_returns = (1 + df['strategy_returns'].fillna(0)).cumprod()\nprint(f'Total Return: {(cum_returns.iloc[-1] - 1)*100:.2f}%')\n"
        },
        "milestone": "🎯 Successfully build a local database that auto-updates every night with closing prices for 500 tickers.",
        "common_mistakes": [
            "Living in Jupyter Notebooks forever: Notebooks are great for exploration but terrible for production. Structure your code as `.py` modules with tests from day one.",
            "Ignoring corporate actions: Failing to adjust prices for splits and dividends will cause your backtest to 'see' fake crashes and phantom rallies.",
            "Downloading data on every run: Not persisting data locally causes slow research loops and breaks reproducibility if a data vendor changes their API.",
            "Using `.iterrows()` in Pandas: This is a loop in disguise and 100–1000x slower than vectorized operations. If you write `.iterrows()`, stop and rethink."
        ],
        "quiz_bank": [
            {
                "question": "What is the primary performance benefit of Vectorization in NumPy/Pandas?",
                "options": ["Easier code", "Avoids memory leaks", "Replaces slow Python loops with C", "Prevents Overfitting"],
                "answer": 2,
                "explanation": "Vectorization performs operations on entire arrays at once using optimized C/C++ backends, bypassing Python's slow global interpreter lock (GIL) and loops."
            },
            {
                "question": "What is 'Survivorship Bias' in financial data?",
                "options": ["Testing only on surviving traders", "Testing only on stocks that are currently in an index", "Testing only on profitable strategies", "Ignoring data from weekends"],
                "answer": 1,
                "explanation": "Survivorship Bias occurs when you only test on companies that haven't gone bankrupt or been delisted, leading to artificially high backtest results."
            },
            {
                "question": "Which file format is preferred for storing large-scale tick data due to its performance and compression?",
                "options": ["CSV", "JSON", "Parquet", "Excel"],
                "answer": 2,
                "explanation": "Parquet is a columnar storage format that is highly optimized for analytical queries and much faster than row-based formats like CSV."
            }
        ],
        "resources": [
            {"icon": "📖", "name": "Python for Data Analysis — Wes McKinney", "url": "https://www.amazon.com/Python-Data-Analysis-Wes-McKinney/dp/109810403X"},
            {"icon": "🌐", "name": "Pandas Official Documentation", "url": "https://pandas.pydata.org/docs/"},
            {"icon": "🌐", "name": "Alpaca Markets: Free Market Data API", "url": "https://alpaca.markets/data"}
        ],
        "glossary": [
            {"term": "Vectorization", "definition": "A method of computer programming where operations are applied to whole arrays rather than individual elements."},
            {"term": "ETL", "definition": "Extract, Transform, Load; the process of moving data from source systems to a destination database."},
            {"term": "Survivorship Bias", "definition": "The logical error of concentrating on the people or things that made it past some selection process and overlooking those that did not."}
        ]
    },
    "Stage 4": {
        "title": "Strategy Research & Backtesting Alpha",
        "duration": "Months 5–8",
        "difficulty": "Intermediate",
        "reading_time": "50h",
        "prereqs": "Stage 3",
        "goal": "Design, test, and validate quantitative trading signals without curve-fitting.",
        "overview": "A backtest is a simulation of the past. If done poorly, it's a hallucination of the future. This stage teaches the rigorous methodology of signal research, from hypothesis generation to out-of-sample validation and cost analysis.",
        "category": "Advanced Research",
        "guide": [
            "1. <b>Pick a Niche:</b> Don't try to trade everything. Choose one asset (e.g., FX) and one style (e.g., Trend).",
            "2. <b>Write a Strategy Thesis:</b> Before coding, write 1 paragraph explaining *why* this strategy should make money (e.g., 'It exploits the slow reaction of retail to news').",
            "3. <b>Analyze Drawdowns:</b> Look at the 'worst-case' periods. Could you have survived them mentally?"
        ],
        "exercise": {
            "title": "The Alpha Hunt",
            "description": "Research 'The Monday Effect' — calculate the average returns for each day of the week to find statistical anomalies.",
            "scaffold": "import pandas as pd\nimport numpy as np\n\n# Dummy data for 1 year\ndates = pd.date_range('2023-01-01', periods=252, freq='B')\nreturns = np.random.normal(0.0005, 0.01, 252)\ndf = pd.DataFrame({'returns': returns}, index=dates)\n\n# Group by day of week (0=Monday, 4=Friday)\ndf['day'] = df.index.dayofweek\navg_returns = df.groupby('day')['returns'].mean()\n\ndays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']\nfor i, d in enumerate(days):\n    print(f'{d}: {avg_returns[i]*100:.4f}%')\n"
        },
        "milestone": "🎯 Create a 10-page 'Strategy Tear Sheet' including Sharpe, Max Drawdown, Win Rate, and Return Distribution.",
        "common_mistakes": [
            "Having no economic thesis: 'This pattern worked in the backtest' is not a thesis. If you cannot explain *why* an edge exists, it almost certainly won't survive live trading.",
            "Optimizing parameters on the full dataset: Fitting your RSI period or lookback window on all available data and then calling it a 'backtest' is just curve-fitting with extra steps.",
            "Ignoring drawdown duration: A 15% drawdown that lasts 3 years is psychologically far harder to survive than a 25% drawdown that recovers in 3 months.",
            "Treating Sharpe Ratio as infallible: A Sharpe of 2.0 calculated on 6 months of data is statistically meaningless. You need at least 3 years of out-of-sample returns for a reliable signal."
        ],
        "quiz_bank": [
            {
                "question": "A strategy that returns 20% but experiences a 40% drawdown is often considered 'uninvestable'. Which metric best captures this relationship?",
                "options": ["Log-Return", "Sharpe Ratio", "Information Ratio", "Skewness"],
                "answer": 1,
                "explanation": "The Sharpe Ratio measures excess return per unit of volatility, helping quants determine if the returns justify the risk/drawdown."
            },
            {
                "question": "What is 'Walk-Forward Optimization' designed to prevent?",
                "options": ["Slippage", "Curve-fitting (Overfitting)", "Exchange outages", "Broker commissions"],
                "answer": 1,
                "explanation": "WFO involves optimizing on a training set and testing on an 'unseen' out-of-sample set to ensure parameters are robust, not just fit to historical noise."
            }
        ],
        "resources": [
            {"icon": "📖", "name": "Algorithmic Trading — Ernest Chan", "url": "https://www.amazon.com/Algorithmic-Trading-Winning-Strategies-Rationale/dp/1118460146"},
            {"icon": "📖", "name": "Expected Returns — Antti Ilmanen", "url": "https://www.amazon.com/Expected-Returns-Investors-Harvesting-Rewards/dp/1119990726"},
            {"icon": "🎓", "name": "WorldQuant University: Free MSc Modules", "url": "https://www.wqu.edu/"},
            {"icon": "🌐", "name": "SSRN: Factor Investing Research Papers", "url": "https://www.ssrn.com/index.cfm/en/"},
            {"icon": "💻", "name": "Backtrader: Python Backtesting Framework", "url": "https://www.backtrader.com/"}
        ],
        "glossary": [
            {"term": "Alpha", "definition": "The excess return of an investment relative to the return of a benchmark index."},
            {"term": "Sharpe Ratio", "definition": "A measure for calculating risk-adjusted return, defined as the average return earned in excess of the risk-free rate per unit of volatility."},
            {"term": "Drawdown", "definition": "The peak-to-trough decline during a specific period for an investment, trading account, or fund."}
        ]
    },
    "Stage 5": {
        "title": "Machine Learning & Portfolio Optimization",
        "duration": "Months 8–12",
        "difficulty": "Advanced",
        "reading_time": "60h",
        "prereqs": "Stage 4",
        "goal": "Apply modern ML models to financial data and optimize capital allocation.",
        "overview": "The market is a non-stationary machine. Simple rules often break. This stage introduces Machine Learning (Random Forests, XGBoost, Transformers) and the mathematical science of Portfolio Optimization (Markowitz, Black-Litterman).",
        "category": "Advanced Research",
        "guide": [
            "1. <b>Master mlfinlab:</b> Explore the 'Hudson & Thames' library for institutional ML implementation.",
            "2. <b>Build a Factor Neutral Portfolio:</b> Use Python to hedge out 'Market Beta' and 'Sector Risk'.",
            "3. <b>Regularize Everything:</b> Learn Lasso and Ridge regression to prevent over-reliance on noisy features."
        ],
        "exercise": {
            "title": "The Regime Detector",
            "description": "Build a K-Means clustering model to categorize the market into 3 states: 'Low Vol/Bull', 'High Vol/Bear', and 'Sideways/Chop'.",
            "scaffold": "import numpy as np\nimport pandas as pd\nfrom sklearn.cluster import KMeans\n\n# Generate dummy features (Returns & Volatility)\nnp.random.seed(42)\nreturns = np.random.normal(0, 0.01, 100)\nvolatility = np.random.uniform(0.01, 0.05, 100)\nX = np.column_stack((returns, volatility))\n\n# Fit KMeans\nkmeans = KMeans(n_clusters=3, random_state=0).fit(X)\n\nprint(f'Detected {len(np.unique(kmeans.labels_))} regimes.')\n# Print cluster centers\nfor i, center in enumerate(kmeans.cluster_centers_):\n    print(f'Regime {i}: Return={center[0]:.4f}, Vol={center[1]:.4f}')\n"
        },
        "milestone": "🎯 Implement a machine learning model that achieves a 'Precision' of >55% on out-of-sample directional signals.",
        "common_mistakes": [
            "Using standard K-Fold CV on time series: Shuffling time-series data before splitting leaks future information into the training set, making results completely unreliable.",
            "Feeding raw price as an ML feature: Price levels are non-stationary and provide no generalizable signal. Always engineer stationary, normalized features (returns, z-scores, ratios).",
            "Maximizing Accuracy instead of Precision: In imbalanced financial datasets, 90% accuracy means nothing if you are predicting 'hold' for every bar. Focus on Precision and Recall of your signal.",
            "Ignoring feature correlation: Highly correlated features don't add information — they add noise and can destabilize tree-based models. Use SHAP/MDA to prune redundant inputs."
        ],
        "quiz_bank": [
            {
                "question": "What is the purpose of 'Meta-Labeling' in a financial machine learning pipeline?",
                "options": ["To predict price", "To filter false positive signals from a primary model", "To replace OLS regression", "To speed up training"],
                "answer": 1,
                "explanation": "Meta-labeling (López de Prado) uses a secondary model to decide *whether* to take a trade suggested by a primary model, improving overall signal precision."
            },
            {
                "question": "Why is standard K-Fold Cross-Validation problematic for financial time series?",
                "options": ["It is too slow", "It leaks future data into the training set", "It only works for images", "It ignores volume"],
                "answer": 1,
                "explanation": "Time series data is sequential. Shuffling and picking random folds (as in K-Fold) allows the model to 'see' future data when predicting the past, leading to over-optimistic results."
            }
        ],
        "resources": [
            {"icon": "📖", "name": "Advances in Financial Machine Learning — López de Prado", "url": "https://www.amazon.com/Advances-Financial-Machine-Learning-Marcos/dp/1119482089"},
            {"icon": "📖", "name": "Options, Futures & Other Derivatives — John Hull", "url": "https://www.amazon.com/Options-Futures-Other-Derivatives-10th/dp/013447208X"},
            {"icon": "🌐", "name": "mlfinlab: Financial ML Python Library", "url": "https://github.com/hudson-and-thames/mlfinlab"},
            {"icon": "🎓", "name": "Coursera: Machine Learning Specialization", "url": "https://www.coursera.org/specializations/machine-learning-introduction"},
            {"icon": "🌐", "name": "PyPortfolioOpt: Portfolio Optimization", "url": "https://pyportfolioopt.readthedocs.io/en/latest/"}
        ],
        "glossary": [
            {"term": "Transformer", "definition": "A deep learning architecture that uses attention mechanisms to weigh the influence of different parts of input data."},
            {"term": "Reinforcement Learning", "definition": "A type of machine learning where an agent learns to make decisions by performing actions and receiving rewards."},
            {"term": "Meta-Labeling", "definition": "The process of using a second model to decide whether to follow the predictions of a primary model."}
        ]
    },
    "Stage 6": {
        "title": "Institutional Infrastructure & Scaling",
        "duration": "Months 12–18",
        "difficulty": "Advanced",
        "reading_time": "45h",
        "prereqs": "Stage 5",
        "goal": "Transition from research to production and understand institutional-grade execution.",
        "overview": "Professional quants don't trade on laptops. They use distributed systems, low-latency connectivity, and robust monitoring. This stage covers the 'plumbing' of a quant fund: from cloud deployment to risk oversight.",
        "category": "Advanced Research",
        "guide": [
            "1. <b>Build a Production Pipeline:</b> Use Docker and AWS/GCP to run your research scripts on a schedule.",
            "2. <b>Network:</b> Start contributing to open-source quant libraries or publishing research on SSRN/arXiv.",
            "3. <b>Capital Allocation:</b> Learn the business of quant: how to pitch a strategy to a PM or Seed Fund."
        ],
        "exercise": {
            "title": "The 'Flash Crash' Test",
            "description": "Simulate how a strategy performs during a hypothetical 'Flash Crash' by injecting a 10% price drop over 1 minute into your test data.",
            "scaffold": "import pandas as pd\nimport numpy as np\n\n# Normal data\nprices = [100.0] * 10\n# The crash\nprices += [95.0, 92.0, 90.0, 89.0, 91.0, 94.0]\n# Recovery\nprices += [98.0] * 10\n\ndf = pd.DataFrame({'price': prices})\n\n# Simple stop loss at 5%\nstop_level = 100.0 * 0.95\nliquidated = df['price'] < stop_level\n\nif liquidated.any():\n    first_exit = liquidated.idxmax()\n    print(f'Liquidated at index {first_exit} for ${df.iloc[first_exit].price}')\n"
        },
        "milestone": "🎯 Deploy a live 'Paper Trading' portfolio of 3+ diversified strategies and maintain a Sharpe > 1.5 for 6 months.",
        "common_mistakes": [
            "Underestimating market impact at scale: A strategy with 20% annual returns may have a capacity of only $5M. Beyond that, your own orders move the market against you.",
            "Treating paper trading as validation: Paper trading does not simulate slippage, partial fills, or the emotional weight of real capital at risk. Use it for mechanics, not for performance proof.",
            "Not monitoring for alpha decay: An edge that existed in 2018 may be fully arbitraged away by 2025. You must continuously monitor live performance vs. the historical backtest benchmark.",
            "Skipping the research journal: Not documenting failed experiments means you will re-invent them. A research log is not optional — it is institutional best practice."
        ],
        "quiz_bank": [
            {
                "question": "What does a VWAP (Volume Weighted Average Price) execution algorithm aim to achieve?",
                "options": ["The highest possible profit", "Execution that matches the day's volume profile to minimize market impact", "Instant order filling", "Arbitrage between exchanges"],
                "answer": 1,
                "explanation": "VWAP algorithms slice large orders into smaller ones throughout the day to hide institutional footprints and minimize price distortion."
            }
        ],
        "resources": [
            {"icon": "📖", "name": "Advances in Financial Machine Learning — Marcos Lopez de Prado", "url": "https://www.amazon.com/Advances-Financial-Machine-Learning-Marcos/dp/1119482089"},
            {"icon": "🎓", "name": "Machine Learning for Trading — Georgia Tech (Udacity)", "url": "https://www.udacity.com/course/machine-learning-for-trading--ud501"},
            {"icon": "💻", "name": "Kaggle: Jane Street Market Prediction Competition", "url": "https://www.kaggle.com/c/jane-street-market-prediction"}
        ],
        "glossary": [
            {"term": "Feature Engineering", "definition": "The process of using domain knowledge to extract features from raw data that make machine learning algorithms work."},
            {"term": "Overfitting", "definition": "A modeling error that occurs when a function is too closely fit to a limited set of data points, failing to generalize to new data."},
            {"term": "Cross-Validation", "definition": "A technique for assessing how the results of a statistical analysis will generalize to an independent data set."}
        ]
    },
    "Stage 7": {
        "title": "Macroeconomics for Financial Markets & Trading",
        "duration": "Advanced Elective",
        "difficulty": "Intermediate",
        "reading_time": "30h",
        "prereqs": "Stage 2",
        "goal": "Integrate top-down macro regimes into systematic trading models.",
        "overview": "Markets don't exist in a vacuum. Central bank policy, inflation cycles, and geopolitical events drive the 'regime' in which your strategies operate. This stage teaches you to quantify macro data to improve strategy selection.",
        "category": "Advanced Research",
        "guide": [
            "1. <b>Follow the Fed:</b> Read the FOMC statements and listen to the Chair's press conference. Note the market reaction in the 2-Year Yield.",
            "2. <b>Build a Macro Dashboard:</b> Track the DXY, 10Y Yield, Brent Oil, and S&P 500 on one screen to see the correlations.",
            "3. <b>Study Economic Releases:</b> Use an economic calendar to track NFP and CPI releases. Observe how the 'surprise' (actual vs forecast) drives volatility."
        ],
        "exercise": {
            "title": "The Yield Curve Playbook",
            "description": "Plot the 2s10s yield spread and identify periods of 'Inversion' (when the 2-year yield is higher than the 10-year).",
            "scaffold": "import pandas as pd\nimport matplotlib.pyplot as plt\n\n# Dummy Yield Data\ndates = pd.date_range('2022-01-01', periods=100)\nyield_2y = np.linspace(0.5, 4.5, 100) + np.random.normal(0, 0.1, 100)\nyield_10y = np.linspace(1.5, 3.5, 100) + np.random.normal(0, 0.1, 100)\n\ndf = pd.DataFrame({'2Y': yield_2y, '10Y': yield_10y}, index=dates)\ndf['spread'] = df['10Y'] - df['2Y']\n\ninverted = df[df['spread'] < 0]\nprint(f'Days in Inversion: {len(inverted)}')\n"
        },
        "milestone": "🎯 Build a 'Macro Regime Monitor' that classifies the current environment into one of four quadrants: Goldilocks, Reflation, Stagflation, or Deflation.",
        "common_mistakes": [
            "Trading the headline number, not the internals: A 'beat' on headline CPI can be bearish for equities if core services inflation is re-accelerating — always decompose the data.",
            "Confusing correlation with causation in cross-asset: The Copper/Gold ratio signals growth expectations — it does not *cause* them. Don't build a trading rule on a ratio without understanding the underlying mechanism.",
            "Ignoring central bank credibility: Policy models assume central banks act rationally and predictably. Political interference or credibility crises (e.g., Turkey, Argentina) can invalidate standard macro frameworks entirely.",
            "Being too early on macro trades: A yield curve inversion can persist for 12–24 months before a recession materializes. Sizing correctly for a long-dated macro trade is as important as being directionally correct."
        ],
        "quiz_bank": [
            {
                "question": "Which yield curve regime is historically most associated with an impending recession?",
                "options": ["Bull Steepening", "Bear Flattening", "Inversion (Short rates > Long rates)", "Parallel Shift Up"],
                "answer": 2,
                "explanation": "Yield curve inversion has preceded almost every major US recession, signaling that the market expects lower future growth and inflation."
            },
            {
                "question": "What is the impact of rising 'Real Yields' on growth-oriented technology stocks?",
                "options": ["Prices rise due to liquidity", "Valuations compress as the discount rate increases", "No correlation", "Dividends increase"],
                "answer": 1,
                "explanation": "Real yields act as 'gravity' for valuations. As the risk-free real return rises, the present value of future earnings (high in growth stocks) drops."
            }
        ],
        "resources": [
            {"icon": "📖", "name": "Macroeconomics — Gregory Mankiw", "url": "https://www.amazon.com/Macroeconomics-N-Gregory-Mankiw/dp/1319105998"},
            {"icon": "🎓", "name": "Real Vision: Institutional Macro Insights", "url": "https://www.realvision.com/"},
            {"icon": "🎓", "name": "MacroVoices Podcast", "url": "https://www.macrovoices.com/"},
            {"icon": "📖", "name": "The Alchemy of Finance — George Soros", "url": "https://www.amazon.com/Alchemy-Finance-George-Soros/dp/0471445494"},
            {"icon": "🌐", "name": "FRED Economic Data (St. Louis Fed)", "url": "https://fred.stlouisfed.org/"}
        ],
        "glossary": [
            {"term": "Quantitative Easing", "definition": "A monetary policy whereby a central bank purchases government securities or other securities from the market in order to lower interest rates and increase the money supply."},
            {"term": "Yield Curve", "definition": "A line that plots the interest rates of bonds having equal credit quality but differing maturity dates."},
            {"term": "Macro-Quant", "definition": "An approach that combines systematic, quantitative investment rules with top-down macroeconomic analysis."}
        ]
    },
    "Stage 8": {
        "title": "Options Theory & Volatility Surface",
        "duration": "Advanced Elective",
        "difficulty": "Expert",
        "reading_time": "55h",
        "prereqs": "Stage 2, 4",
        "goal": "Master the non-linear world of derivatives and volatility trading.",
        "overview": "Options are the only instruments that allow you to trade pure volatility. This stage covers the Black-Scholes model, the 'Greeks' (Delta, Gamma, Vega), and how to exploit the Volatility Risk Premium (VRP).",
        "category": "Expert Electives",
        "guide": [
            "1. <b>Start with Options Pricing Calculators:</b> Use an online BSM calculator (CBOE has one free). Input different strikes and expiries and observe how IV changes the price more than any other input.",
            "2. <b>Simulate a Delta Hedge:</b> Using daily SPY data, simulate being short a call option and delta-hedging it daily. Calculate your P&L from Gamma gains vs. Theta paid.",
            "3. <b>Read the VIX Term Structure Daily:</b> Every morning, look at the VIX Futures curve on vixcentral.com. Notice if it is in Contango (normal) or Backwardation (fear). Track what happens to markets under each regime."
        ],
        "exercise": {
            "title": "The Volatility Surface Builder",
            "description": "Simulate an options chain and plot the 'Volatility Smile' (how IV increases as you move away from at-the-money).",
            "scaffold": "import numpy as np\nimport matplotlib.pyplot as plt\n\n# Strikes around spot (100)\nstrikes = np.linspace(80, 120, 20)\n\n# Simulate a 'Smile' effect\niv = 0.2 + 0.001 * (strikes - 100)**2\n\nplt.plot(strikes, iv, 'o-')\nplt.axvline(100, color='r', linestyle='--', label='At-The-Money')\nplt.title('The Volatility Smile')\nplt.xlabel('Strike Price')\nplt.ylabel('Implied Volatility')\nplt.legend()\nplt.show()\n"
        },
        "milestone": "🎯 Build a delta-hedging simulation that correctly calculates daily P&L (Gamma PnL + Theta decay) for a short straddle position over a 30-day period.",
        "common_mistakes": [
            "Buying options without understanding Theta: Buying weekly options and holding them through time decay is the fastest way to lose money in options. Time is *always* working against the buyer.",
            "Ignoring Implied Volatility Rank (IVR): Buying options when IV is at a 52-week high (expensive) and selling them when IV is at a 52-week low (cheap) is a common and costly error.",
            "Confusing Delta with probability of profit: A 0.30 Delta option does not have a 30% probability of being in-the-money at expiry. The correct measure is N(d2), not N(d1), from the BSM formula.",
            "Selling naked options without tail-risk management: Selling uncovered puts or calls for premium income is seductive until a black swan event delivers a loss that exceeds years of collected premium in a single day."
        ],
        "quiz_bank": [
            {
                "question": "Which 'Greek' measures an option's sensitivity to time decay?",
                "options": ["Delta", "Gamma", "Theta", "Vega"],
                "answer": 2,
                "explanation": "Theta (Θ) represents the daily loss in an option's value as it approaches expiration, assuming no change in the underlying price or volatility."
            },
            {
                "question": "What does a 'Positive Gamma' position mean for an options trader?",
                "options": ["They lose money if the market moves", "Their Delta increases as the underlying moves in their favor", "They are short volatility", "They benefit from time passing"],
                "answer": 1,
                "explanation": "Positive Gamma means your directional exposure (Delta) grows in the direction of the move, allowing you to profit from large 'jumps' in price."
            }
        ],
        "resources": [
            {"icon": "📖", "name": "Options, Futures & Other Derivatives — John Hull", "url": "https://www.amazon.com/Options-Futures-Other-Derivatives-10th/dp/013447208X"},
            {"icon": "📖", "name": "The Volatility Surface — Jim Gatheral", "url": "https://www.amazon.com/Volatility-Surface-Practitioners-Guide/dp/0471792519"},
            {"icon": "🎓", "name": "CBOE Options Institute: Free Education", "url": "https://www.cboe.com/education/"},
            {"icon": "🌐", "name": "VIX Central: VIX Term Structure Monitor", "url": "http://vixcentral.com/"},
            {"icon": "🎓", "name": "tastytrade: Practical Options Trading", "url": "https://tastytrade.com/learn/"},
            {"icon": "🌐", "name": "Quantpedia: The Encyclopedia of Algorithmic Strategies", "url": "https://quantpedia.com/"}
        ],
        "glossary": [
            {"term": "Black-Scholes Model", "definition": "A mathematical model used to estimate the fair price of European-style options."},
            {"term": "Volatility Risk Premium", "definition": "The difference between the implied volatility (market expectation) and the realized volatility (actual outcome) of an underlying asset."},
            {"term": "Greeks", "definition": "Financial measures used to assess the risk of an option position, including Delta, Gamma, Theta, and Vega."}
        ]
    },
    "Stage 9": {
        "title": "HFT & Low-Latency Infrastructure",
        "duration": "Months 12–18",
        "difficulty": "Expert",
        "reading_time": "60h",
        "prereqs": "Stage 1, Stage 6",
        "goal": "Master the hardware and software architectures required to compete in the sub-millisecond trading domain.",
        "overview": "The world of HFT is the extreme frontier of quantitative finance. At this level, alpha is measured in microseconds. This stage bridges the gap between pure mathematical finance and high-performance engineering, covering the 'plumbing' that allows institutional firms to harvest liquidity and manage risk at lightning speed.",
        "category": "Expert Electives",
        "guide": [
            "1. <b>Build a Toy LOB:</b> Write a Python script that maintains a sorted list of bids and asks. Simulate a market buy order and calculate the average price.",
            "2. <b>Research Colocation:</b> Learn why quants pay thousands to have their servers in the same building as the exchange.",
            "3. <b>Master kdb+/q:</b> Explore the industry-standard database for tick-level time-series data."
        ],
        "exercise": {
            "title": "The HFT Signal Engine",
            "description": "Calculate 'Order Book Imbalance' from a snapshot of the top 5 levels of the bid and ask.",
            "scaffold": "import numpy as np\n\n# Bid sizes (top 5 levels)\nbids = np.array([100, 250, 150, 300, 200])\n# Ask sizes (top 5 levels)\nasks = np.array([120, 100, 200, 150, 100])\n\n# Simple Imbalance: (Total Bids - Total Asks) / Total Volume\ntotal_bids = bids.sum()\ntotal_asks = asks.sum()\n\nimbalance = (total_bids - total_asks) / (total_bids + total_asks)\n\nprint(f'Order Book Imbalance: {imbalance:.4f}')\nif imbalance > 0.1:\n    print('Bullish Pressure (Buy Side Heavy)')\nelif imbalance < -0.1:\n    print('Bearish Pressure (Sell Side Heavy)')\n"
        },
        "milestone": "🎯 Build an 'Order Flow Tracker' that identifies large 'Iceberg' orders by detecting volume that fills at a price without the displayed size decreasing.",
        "common_mistakes": [
            "Ignoring Exchange Latency: A signal that works in a backtest with 1-minute data will fail in HFT if you don't account for the 5-10ms it takes for your order to reach the matching engine.",
            "Assuming perfect fills: In the real LOB, you are competing with thousands of others. You will often get 'partial fills' or be 'front-run' by faster participants.",
            "Overestimating alpha from simple imbalance: Order book imbalance is a 'noisy' signal. It works best when combined with other microstructural features like trade flow and cancelation rates.",
            "Neglecting the cost of technology: HFT is an arms race. If you don't have the fastest hardware and lowest-latency code, you are the liquidity for those who do."
        ],
        "quiz_bank": [
            {
                "question": "What does 'Order Book Imbalance' typically signal in the very short term?",
                "options": ["A guaranteed trend reversal", "Potential direction of the next price move based on buy/sell pressure", "Market close", "The end of a recession"],
                "answer": 1,
                "explanation": "Imbalance measures the ratio of buy-side to sell-side volume. High imbalance often precedes a move in the direction of the heavier side."
            },
            {
                "question": "What is 'Latent Arbitrage' in the context of HFT?",
                "options": ["Buying slow and selling fast", "Exploiting price differences for the same asset across different exchanges using superior speed", "Trading once a year", "Investing in real estate"],
                "answer": 1,
                "explanation": "Latency arbitrage involves being faster than the market to pick off stale quotes on one exchange when the price has already moved on another."
            }
        ],
        "topics": [
            {
                "category": "The HFT Tech Stack (Hardware & OS)",
                "items": [
                    {"text": "Colocation & The Physics of Latency: In HFT, the speed of light is a constraint. You must understand 'Colocation'—placing servers in the same exchange data center to minimize travel distance.", "is_interview_prep": True},
                    "Kernel Bypass & Low-Latency Linux: Standard operating systems are too slow.",
                    {"text": "FPGA & Hardware Acceleration: When C++ is too slow, we use hardware."}
                ]
            }
        ],
        "resources": [
            {"icon": "📖", "name": "Trading and Exchanges — Larry Harris", "url": "https://www.amazon.com/Trading-Exchanges-Market-Microstructure-Practitioners/dp/0195144708"}
        ],
        "glossary": [
            {"term": "HFT", "definition": "High-Frequency Trading."},
            {"term": "FPGA", "definition": "Field Programmable Gate Array."},
            {"term": "Kernel Bypass", "definition": "Networking stack bypass."}
        ]
    },
    "Stage 10": {
        "title": "Crypto & DeFi Quantitative Methods",
        "duration": "Advanced Elective",
        "difficulty": "Expert",
        "reading_time": "45h",
        "prereqs": "Stage 1, Stage 3",
        "goal": "Apply quantitative rigor to the frontier of decentralized finance and crypto assets.",
        "overview": "Crypto markets are the 'Wild West' of quant finance. With 24/7 trading and on-chain transparency, they offer unique alpha opportunities in arbitrage, MEV, and liquidity provisioning.",
        "category": "Expert Electives",
        "guide": [
            "1. Study the 'Ethereum Yellow Paper' to understand gas and EVM.",
            "2. Use Dune Analytics to build a dashboard for DEX volume.",
            "3. Learn 'Solidity' or 'Rust' for smart contract interaction."
        ],
        "exercise": {
            "title": "The Funding Arb",
            "description": "Calculate the annualized return of a basis trade (buying spot, selling perps).",
            "scaffold": "spot_price = 50000\nperp_price = 50050\nfunding_rate = 0.0001 # 0.01%\n\nannualized_return = (funding_rate * 3 * 365)\nprint(f'Annualized Funding Yield: {annualized_return:.2%}')"
        },
        "milestone": "🎯 Build a Python script that uses a WebSocket to track real-time liquidations across 3 major crypto exchanges.",
        "common_mistakes": [
            "Ignoring 'Gas' fees: In DeFi, a profitable arbitrage can be turned into a loss if you don't account for the $50-$100 cost of the transaction itself.",
            "Underestimating Smart Contract Risk: No amount of quant research can save you if the protocol you are trading on gets hacked or has a 'rug pull'.",
            "Trusting 'Oracle' prices blindly: Many DeFi protocols were exploited because their price oracles were manipulated. Always use decentralized oracles like Chainlink."
        ],
        "quiz_bank": [
            {
                "question": "In Uniswap's constant product formula (x * y = k), what happens to the price of X as you buy more of it?",
                "options": ["It stays the same", "It decreases", "It increases exponentially", "It fluctuates randomly"],
                "answer": 2,
                "explanation": "As you remove X from the pool (buy), the ratio of Y to X increases, driving the price of X higher along a curve."
            },
            {
                "question": "What is 'Impermanent Loss' in DeFi?",
                "options": ["A permanent loss of capital", "The opportunity cost of providing liquidity compared to just holding assets", "Trading fees", "A hack"],
                "answer": 1,
                "explanation": "Impermanent loss occurs when the price of the assets in a pool diverges from when you deposited them, making your pool value less than if you had simply held the assets."
            }
        ],
        "resources": [
            {"icon": "🌐", "name": "Dune Analytics: SQL-based On-chain Data", "url": "https://dune.com/"},
            {"icon": "📖", "name": "Mastering Bitcoin — Andreas Antonopoulos", "url": "https://www.amazon.com/Mastering-Bitcoin-Programming-Open-Blockchain/dp/1491954388"},
            {"icon": "💻", "name": "Flashbots: MEV Research & Tools", "url": "https://www.flashbots.net/"}
        ],
        "glossary": [
            {"term": "DeFi", "definition": "Decentralized Finance; a blockchain-based form of finance that does not rely on central financial intermediaries."},
            {"term": "MEV", "definition": "Maximal Extractable Value; the maximum value that can be extracted from block production in excess of the standard block reward and gas fees."},
            {"term": "Perpetual Swap", "definition": "A type of derivative similar to a futures contract but without an expiration date, using a funding rate mechanism to stay anchored to the spot price."}
        ]
    },
    "Stage 11": {
        "title": "Risk Management & Portfolio Oversight",
        "duration": "Advanced Capstone",
        "difficulty": "Expert",
        "reading_time": "40h",
        "prereqs": "All Previous Stages",
        "goal": "Build an institutional-grade risk management framework that ensures strategy longevity and fund survival.",
        "overview": "Risk management is not about 'avoiding' risk; it is about 'managing' it. In this capstone, you will learn the mathematical tools used by Chief Risk Officers (CROs) to ensure that a single bad day doesn't wipe out years of alpha. You will move from simple stop-losses to complex stress testing and capital allocation models.",
        "topics": [
            {
                "category": "Quantifying the Unthinkable",
                "items": [
                    {"text": "Value at Risk (VaR) vs. Expected Shortfall (CVaR): You must move beyond VaR (which only tells you the 'threshold' loss) to Expected Shortfall (which tells you the 'average' loss when that threshold is breached). CVaR is the institutional standard for managing tail risk.\n\nExample: A 95% VaR of $1M means there is a 5% chance you lose *at least* $1M. A 95% CVaR of $2.5M means that in those 5% of cases, your *average* loss is $2.5M. CVaR captures the 'severity' of the crash.", "is_interview_prep": True},
                    "Stress Testing & Scenario Analysis: A backtest is just one realization of history. You must learn to run 'What-If' scenarios: What happens to my portfolio if interest rates spike 100bps? What if 1987 happens again? Stress testing tells you where your hidden correlations lie.\n\nExample: You think your portfolio is diversified across Tech and Biotech. A 'Stress Test' shows that in a 'Rising Rate' scenario, both sectors drop 20% together, proving you weren't as hedged as you thought."
                ]
            },
            {
                "category": "Optimal Capital Allocation",
                "items": [
                    {"text": "The Kelly Criterion & Sizing for Growth: You must master the math of optimal betting. The Kelly Criterion tells you exactly how much to risk on each trade to maximize the long-term growth of your capital without hitting 'Ruin'.\n\nExample: If you have a strategy with a 60% win rate and 1:1 payoff, Kelly suggests risking 20% per trade. However, quants often use 'Fractional Kelly' (e.g., 1/4 Kelly) to buffer against model uncertainty.", "is_interview_prep": True},
                    "Risk Parity & Volatility Targeting: Institutional funds don't allocate by dollars; they allocate by 'Risk'. You will learn to use 'Volatility Targeting' to dynamically scale your position sizes so that your portfolio's risk remains constant, even as market volatility fluctuates.\n\nExample: In a calm market, you might hold $10M of exposure. If volatility doubles, you automatically cut your exposure to $5M to keep your 'Daily VaR' constant."
                ]
            }
        ],
        "guide": [
            "1. Read 'Against the Gods' by Peter Bernstein for the history of risk.",
            "2. Build a VaR/CVaR calculator in Python for your best strategy.",
            "3. Run a Monte Carlo simulation of your equity curve with varying leverage."
        ],
        "exercise": {
            "title": "The Ruin Simulation",
            "description": "Write a script that simulates a strategy with a 55% win rate and 1:1 payoff. Compare the equity curves of 1% risk per trade vs 10% risk per trade over 1,000 trades. Observe 'Path Dependency'.",
            "scaffold": "import numpy as np\n\nwin_rate = 0.55\nrisk_1 = 0.01\nrisk_2 = 0.10\n\nfor risk in [risk_1, risk_2]:\n    capital = 10000\n    for _ in range(100):\n        if np.random.random() < win_rate:\n            capital += capital * risk\n        else:\n            capital -= capital * risk\n    print(f'Risk {risk*100}% Final Capital: ${capital:.2f}')\n"
        },
        "milestone": "🎯 Complete a 'Risk Audit' of your portfolio, identifying your top 3 'Tail Risk' scenarios and proposing hedges for each.",
        "common_mistakes": [
            "Treating Risk as Static: Volatility clusters. Risk often spikes exactly when your strategy is performing at its worst. Always assume correlations go to 1 during a crash.",
            "Over-reliance on Historical VaR: History doesn't always repeat. Relying solely on the last 2 years of data will leave you unprepared for a new type of regime shift.",
            "Confusing 'Diversification' with 'Safety': Buying 50 different stocks in the same sector is not diversification; it's just a concentrated bet on that sector's risk factor."
        ],
        "quiz_bank": [
            {
                "question": "Why is Expected Shortfall (CVaR) considered superior to Value at Risk (VaR) for risk management?",
                "options": ["It is easier to calculate", "It is always a smaller number", "It accounts for the severity of losses in the 'tail' beyond the threshold", "It predicts the next crash"],
                "answer": 2,
                "explanation": "VaR only tells you the minimum loss at a certain confidence level; CVaR (Expected Shortfall) tells you the average loss in the worst-case scenarios, capturing 'tail risk' better."
            },
            {
                "question": "What does the Kelly Criterion help a trader optimize?",
                "options": ["Win rate", "Trade frequency", "Position sizing for maximum long-term growth", "Market impact"],
                "answer": 2,
                "explanation": "The Kelly Criterion calculates the mathematically optimal percentage of capital to risk on a bet to maximize long-term wealth growth."
            }
        ],
        "resources": [
            {"icon": "📖", "name": "Against the Gods — Peter Bernstein", "url": "https://www.amazon.com/Against-Gods-Remarkable-Story-Risk/dp/0471295639"},
            {"icon": "🎓", "name": "CFA Institute: Risk Management Overview", "url": "https://www.cfainstitute.org/en/membership/professional-development/refresher-readings/risk-management"},
            {"icon": "🌐", "name": "Risk.net: Institutional Risk News", "url": "https://www.risk.net/"}
        ],
        "glossary": [
            {"term": "Value-at-Risk (VaR)", "definition": "A statistical technique used to measure the amount of potential loss that could happen in a portfolio over a specified time horizon."},
            {"term": "Expected Shortfall", "definition": "A risk measure that quantifies the amount of tail risk an investment portfolio has; it is the average loss given that the loss is greater than the VaR."},
            {"term": "Kelly Criterion", "definition": "A formula used to determine the optimal size of a series of bets in order to maximize the logarithm of wealth."}
        ]
    },
    "Stage 12": {
        "title": "NLP & Alternative Data Alpha",
        "duration": "Advanced Elective",
        "difficulty": "Expert",
        "reading_time": "45h",
        "prereqs": "Stage 3, 5",
        "goal": "Extract alpha from unstructured text, news, and unconventional data sources using modern NLP and LLMs.",
        "overview": "90% of the world's data is unstructured. While most quants fight over the same price-action signals, the next frontier of alpha lies in reading earnings calls, tracking satellite imagery, and quantifying the sentiment of central bank speakers. This elective teaches you to turn 'words' into 'numbers' and 'noise' into 'signals'.",
        "topics": [
            {
                "category": "Modern NLP for Finance",
                "items": [
                    {"text": "Sentiment Analysis & FinBERT: You must move beyond simple 'word counts' to context-aware models. You will learn to use FinBERT—a BERT model pre-trained on financial text—to quantify the tone of news and earnings reports.\n\nExample: A traditional sentiment model might flag the word 'crushing' as negative. FinBERT understands that in the context of 'crushing earnings estimates,' it is highly positive.", "is_interview_prep": True},
                    "LLMs & Retrieval-Augmented Generation (RAG): Learn how Hedge Funds are using Large Language Models to parse 1,000-page 10-K filings in seconds, extracting specific risk factors and competitive advantages that are hidden from purely quantitative price models."
                ]
            },
            {
                "category": "Alternative Data Sources",
                "items": [
                    {"text": "Satellite Imagery & Geopolitical Tracking: Quantifying physical reality. You will study how funds use satellite data to track oil storage in China or retail traffic at major malls to predict economic shifts before they are officially reported.\n\nExample: By counting cars in Walmart parking lots across the US, a quant can estimate quarterly revenue with higher precision than the street consensus.", "is_interview_prep": True},
                    "Credit Card Flows & ESG Data: Using anonymized consumer spending data to forecast retail sales, and integrating ESG (Environmental, Social, Governance) scores as a long-term risk factor in portfolio construction."
                ]
            }
        ],
        "guide": [
            "1. Learn the HuggingFace `transformers` library.",
            "2. Build a scraper for FOMC minutes and run a sentiment model.",
            "3. Research 'Nowcasting'—using high-frequency data to predict slow-moving GDP."
        ],
        "exercise": {
            "title": "The Earnings Scraper",
            "description": "Simulate parsing an earnings call snippet to identify 'Hawkish' vs 'Dovish' keywords.",
            "scaffold": "transcript = \"\"\"Our outlook remains cautious despite beating estimates. We expect headwinds in the next quarter due to rising labor costs.\"\"\"\n\nhawkish_words = ['headwinds', 'cautious', 'rising costs', 'tighter']\ndovish_words = ['growth', 'beating estimates', 'expansion', 'favorable']\n\nscore = 0\nfor word in hawkish_words:\n    if word in transcript.lower(): score -= 1\nfor word in dovish_words:\n    if word in transcript.lower(): score += 1\n\nprint(f'Sentiment Score: {score}')\nprint(f'Stance: {\"Hawkish\" if score < 0 else \"Dovish\" if score > 0 else \"Neutral\"}')\n"
        },
        "milestone": "🎯 Build a sentiment-based strategy that trades the 'News Gap' and achieves a positive Sharpe over 1 year of backtested data.",
        "common_mistakes": [
            "Ignoring 'Look-ahead Bias' in news: Using news that was 'timestamped' at 9:00 AM but only available to the public at 9:15 AM will produce a fake backtest.",
            "Underestimating the cost of Alt-Data: Many datasets cost $50k-$200k/year. A retail quant must focus on 'Web Scraping' and open-source alternatives.",
            "Overfitting on small text samples: Sentiment on a single tweet is noise. Focus on aggregate flow across thousands of sources."
        ],
        "quiz_bank": [
            {
                "question": "What makes FinBERT superior to a standard sentiment dictionary for financial text?",
                "options": ["It is faster", "It understands financial context and nuance (e.g., 'beat estimates')", "It is free", "It only works on Bloomberg data"],
                "answer": 1,
                "explanation": "FinBERT is specifically trained on financial corpora (news, filings), allowing it to recognize that words like 'volatile' or 'crush' have different meanings in finance vs. general language."
            },
            {
                "question": "In NLP, what does 'Stemming' or 'Lemmatization' achieve?",
                "options": ["Predicting the next word", "Reducing words to their root form (e.g., 'trading' -> 'trade')", "Increasing vocabulary size", "Removing all numbers"],
                "answer": 1,
                "explanation": "Stemming and Lemmatization are preprocessing steps that reduce words to their base form so that the model treats 'trade', 'trading', and 'traded' as the same concept."
            }
        ],
        "resources": [
            {"icon": "🌐", "name": "HuggingFace: Transformer Models", "url": "https://huggingface.co/"},
            {"icon": "📖", "name": "Alternative Data — Alexander Denev", "url": "https://www.amazon.com/Book-Alternative-Data-Alexander-Denev/dp/1119601703"},
            {"icon": "🎓", "name": "NLP in Finance — Coursera", "url": "https://www.coursera.org/learn/nlp-finance"}
        ],
        "glossary": [
            {"term": "FinBERT", "definition": "A domain-specific NLP model based on the BERT architecture, pre-trained on a large corpus of financial text."},
            {"term": "RAG", "definition": "Retrieval-Augmented Generation; a technique that combines LLMs with external data retrieval to improve answer accuracy."},
            {"term": "Alternative Data", "definition": "Information about a particular company that is published by sources outside of the company itself, such as satellite imagery or social media sentiment."}
        ]
    },
    "Stage 13": {
        "title": "Execution Science & Market Impact",
        "duration": "Advanced Elective",
        "difficulty": "Expert",
        "reading_time": "40h",
        "prereqs": "Stage 6, 9",
        "goal": "Optimize the 'Implementation Shortfall' by mastering the science of order routing and market impact modeling.",
        "overview": "Alpha is what you 'think' you make; P&L is what you 'actually' keep. In institutional trading, your own size is your biggest enemy. This stage teaches you the Almgren-Chriss models and the engineering of 'Smart Order Routers' to hide your footprint from the market.",
        "topics": [
            {
                "category": "Optimal Execution Models",
                "items": [
                    {"text": "Almgren-Chriss Framework: The industry standard for 'Optimal Execution'. You will learn to solve the optimization problem: how to split a large order to balance 'Market Impact' (costs from moving the price) against 'Opportunity Cost' (risk of price moving before you finish).\n\nExample: If you sell too fast, you crash the price yourself. If you sell too slow, the market might crash while you still hold the position. Almgren-Chriss finds the 'Efficient Frontier' of execution.", "is_interview_prep": True},
                    "Implementation Shortfall (IS): Learn to measure the difference between the decision price (when you decided to trade) and the final average fill price. Minimizing IS is the primary goal of an execution desk."
                ]
            },
            {
                "category": "Smart Order Routing & Dark Pools",
                "items": [
                    {"text": "Dark Pools & Liquidity Fragmentation: Institutional liquidity is hidden. You will study how 'Dark Pools' (private exchanges) allow for large trades without immediate public disclosure, and the risks of 'predatory' HFTs sniffing out your hidden orders.\n\nExample: A quant uses a 'Smart Order Router' (SOR) to scan multiple lit exchanges and dark pools simultaneously, filling a 100k share order across 20 venues in milliseconds.", "is_interview_prep": True},
                    "Order Routing Logic: Building SORs that prioritize venues based on 'Fill Rate,' 'Rebate Structure,' and 'Latency'. You will learn the 'Maker-Taker' economics of exchange connectivity."
                ]
            }
        ],
        "guide": [
            "1. Derive the Almgren-Chriss linear impact model.",
            "2. Build a simulation of an 'Iceberg' order and its impact on the LOB.",
            "3. Study the 'IEX' Speed Bump and its impact on HFT arbitrage."
        ],
        "exercise": {
            "title": "The Execution Optimizer",
            "description": "Calculate a VWAP execution schedule for a 1M share order over a 6.5 hour trading day.",
            "scaffold": "total_shares = 1000000\nhours = 6.5\nintervals_per_hour = 12 # 5-min intervals\ntotal_intervals = int(hours * intervals_per_hour)\n\n# Assuming constant volume profile for simplicity\nshares_per_interval = total_shares / total_intervals\n\nprint(f'Execution Schedule: Buy {shares_per_interval:,.0f} shares every 5 minutes for {total_intervals} intervals.')\n"
        },
        "milestone": "🎯 Design an execution algorithm that achieves a 'Beating VWAP' benchmark on a historical tick-data simulation.",
        "common_mistakes": [
            "Ignoring 'Adverse Selection' in Dark Pools: Sometimes the only person who will trade with you in a dark pool is someone who knows more than you.",
            "Over-optimizing execution for 'quiet' days: Algorithms that work in low-volatility fail spectacularly during a market panic when liquidity vanishes.",
            "Trusting broker 'SOR' logic blindly: Institutional quants often build their own routers to ensure their 'Alpha' isn't leaked to the broker's HFT desk."
        ],
        "quiz_bank": [
            {
                "question": "What is the primary trade-off in the Almgren-Chriss optimal execution model?",
                "options": ["Speed vs. Accuracy", "Market Impact vs. Opportunity Cost", "Leverage vs. Margin", "Risk vs. Reward"],
                "answer": 1,
                "explanation": "Quants must balance the cost of moving the market (Impact) against the risk of the price moving away from them while they wait to fill (Opportunity Cost)."
            },
            {
                "question": "What is a 'Dark Pool' primarily used for by institutions?",
                "options": ["Illegal activities", "Hiding large orders from the public to minimize market impact", "Mining Bitcoin", "Storing physical gold"],
                "answer": 1,
                "explanation": "Dark pools are private exchanges that don't display their order book, allowing institutions to trade large blocks without signaling their intent to the broader market."
            }
        ],
        "glossary": [
            {"term": "Implementation Shortfall", "definition": "The difference between the theoretical price of an order at the time of decision and the actual execution price."},
            {"term": "Market Impact", "definition": "The price change directly resulting from the execution of a large trade."},
            {"term": "Dark Pool", "definition": "A private trading venue that does not display its order book to the public, used to minimize market impact."}
        ],
        "resources": [
            {"icon": "📖", "name": "Algorithmic Trading & DMA — Barry Johnson", "url": "https://www.amazon.com/Algorithmic-Trading-DMA-introduction-strategies/dp/0956399207"},
            {"icon": "🎓", "name": "Optimal Execution (Almgren) — Original Paper", "url": "https://www.math.nyu.edu/financial_mathematics/content/02_financial/almgren_chriss.pdf"},
            {"icon": "🌐", "name": "IEX: The Speed Bump Explained", "url": "https://www.iextrading.com/"}
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
    "Stage 6": ["Custom execution infra", "Bloomberg/Refinitiv", "AWS/GCP", "FIX Protocol"],
    "Stage 7": ["FRED API", "TradingView/ThinkOrSwim", "Economic Calendars"],
    "Stage 8": ["OptionStat", "CBOE Tools", "Greeks Calculators", "QuantLib (C++/Python)"],
    "Stage 9": ["C++ (Modern C++20)", "Solarflare OpenOnload", "FIX/SBE Engines", "FPGA Dev Kits"],
    "Stage 10": ["Dune Analytics", "Ethers.js / Web3.py", "Solidity/Rust", "MetaMask/Hardware Wallets"],
    "Stage 11": ["RiskMetrics", "Monte Carlo Simulators", "GARCH Modeling (arch library)", "VaR/CVaR Engines"],
    "Stage 12": ["HuggingFace Transformers", "NLTK/SpaCy", "BeautifulSoup/Scrapy", "OpenAI/Anthropic APIs"],
    "Stage 13": ["Smart Order Router (SOR) Simulators", "FIX Protocol Engines", "C++20", "Tick Data Warehouses (KDB+/Timescale)"]
}
