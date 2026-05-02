# app.py
import streamlit as st
import base64
from pathlib import Path
from styles import apply_styles
from content import ROADMAP_DATA, TRAPS, TOOLS_CHECKLIST

# Page Config
st.set_page_config(
    page_title="Quant Research Roadmap",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
apply_styles()

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def get_img_with_href(local_img_path):
    img_format = Path(local_img_path).suffix.replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    return f"data:image/{img_format};base64,{bin_str}"

# Navigation Options
PAGES = ["Overview", "Stage 1: Foundation", "Stage 2: Math & Stats", "Stage 3: Programming", 
         "Stage 4: Strategy", "Stage 5: Advanced", "Stage 6: Professional", "Stage 7: Macroeconomics",
         "Stage 8: Options & Derivatives", "Tools & Traps", "📖 Glossary", "✅ My Progress"]

# Helper for smooth navigation
def navigate_to(target):
    st.session_state.sidebar_radio = target

# Initialize session state from query params for external navigation (clickable cards)
if "nav" in st.query_params:
    st.session_state.sidebar_radio = st.query_params["nav"]
    st.query_params.clear()

if "sidebar_radio" not in st.session_state:
    st.session_state.sidebar_radio = "Overview"

# Sidebar Navigation
st.sidebar.title("🚀 Navigation")
page = st.sidebar.radio("Jump to Section", 
    PAGES,
    key="sidebar_radio"
)

# Hero Section Image Path
hero_img_path = Path("assets/hero.png")
hero_img_base64 = ""

if hero_img_path.exists():
    try:
        hero_img_base64 = get_img_with_href(str(hero_img_path))
    except Exception as e:
        st.error(f"Error loading hero image: {e}")
else:
    # Fallback or placeholder if needed
    pass

# --- OVERVIEW PAGE ---
if page == "Overview":
    hero_style = f"background-image: url('{hero_img_base64}');" if hero_img_base64 else "background: linear-gradient(135deg, #1E1E2E 0%, #11111B 100%);"
    st.markdown(f"""
        <div class="hero-container" style="{hero_style}">
            <div class="hero-overlay"></div>
            <div class="hero-content">
                <div class="hero-title">Quantitative Trading Research</div>
                <div class="hero-subtitle">The Complete 19-Month Learning Journey</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### 🗺️ The Path to Mastery")
        st.markdown("""
        <p style="font-size: 0.9375rem; line-height: 1.85; color: #94A3B8; margin-bottom: 1.75rem;">
        The journey from absolute beginner to professional quantitative researcher is a multi-phase evolution.
        Each stage builds the foundation for the next — completion of Stages 1–4 alone puts you ahead of 90% of retail traders.
        </p>
        """, unsafe_allow_html=True)
        
        # Timeline Visualization
        timeline_html = """
        <div class="roadmap-timeline">
            <div class="timeline-step active">1</div>
            <div class="timeline-step">2</div>
            <div class="timeline-step">3</div>
            <div class="timeline-step">4</div>
            <div class="timeline-step">5</div>
            <div class="timeline-step">6</div>
            <div class="timeline-step">7</div>
        </div>
        """
        st.markdown(timeline_html, unsafe_allow_html=True)
        
        # Summary Cards
        for i, (key, stage) in enumerate(ROADMAP_DATA.items()):
            # Match exact string in PAGES list
            matching_page = next((p for p in PAGES if p.startswith(f"{key}:")), None)
            target_page = matching_page if matching_page else f"{key}: {stage['title']}"
            
            # Render card visually, then use a Streamlit button styled as a CTA
            diff_color = "#22C55E" if stage.get('difficulty') == "Beginner" else "#FBBF24" if stage.get('difficulty') == "Intermediate" else "#EF4444" if stage.get('difficulty') == "Expert" else "#F97316"
            
            st.markdown(f"""
            <div class="glass-card">
                <div style="display: flex; gap: 0.5rem; margin-bottom: 0.5rem;">
                    <span class="stage-badge">{stage['duration']}</span>
                    <span class="stage-badge" style="background: rgba(255,255,255,0.06); color: {diff_color}; border: 1px solid {diff_color}33;">{stage.get('difficulty', 'TBD')}</span>
                </div>
                <h3 style="font-size: 1.05rem; font-weight: 700; color: #E2E8F0; margin-top: 0.5rem; margin-bottom: 0.4rem; letter-spacing: -0.01em;">{key}: {stage['title']}</h3>
                <p style="font-size: 0.875rem; color: #64748B; line-height: 1.65; margin-bottom: 0.75rem;">{stage['goal']}</p>
                <div style="display: flex; align-items: center; gap: 1rem; border-top: 1px solid rgba(255,255,255,0.05); pt: 0.75rem; margin-top: 0.75rem; font-size: 0.75rem; color: #94A3B8;">
                    <span>⏱️ {stage.get('reading_time', 'N/A')} study</span>
                    <span>🧩 Prereq: {stage.get('prereqs', 'None')}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.button(
                f"→ Open {key}",
                key=f"btn_{key}",
                on_click=navigate_to,
                args=(target_page,),
                use_container_width=True
            )

# --- STAGE PAGES ---
elif "Stage" in page:
    stage_key = page.split(":")[0].strip()
    try:
        stage_data = ROADMAP_DATA[stage_key]
    except KeyError:
        st.error(f"KeyError: '{stage_key}' not found in ROADMAP_DATA. Available keys: {list(ROADMAP_DATA.keys())}")
        st.stop()
    
    st.markdown(f"""
    <div style="display: flex; gap: 0.6rem; margin-bottom: 0.5rem;">
        <span class="stage-badge">{stage_data['duration']}</span>
        <span class="stage-badge" style="background: rgba(255,255,255,0.06); color: #94A3B8;">⏱️ {stage_data.get('reading_time', 'N/A')}</span>
        <span class="stage-badge" style="background: rgba(255,255,255,0.06); color: #94A3B8;">🧩 Prereq: {stage_data.get('prereqs', 'None')}</span>
    </div>
    <h1 style="font-size: 2rem; font-weight: 800; letter-spacing: -0.03em; color: #F1F5F9; margin-top: 0.25rem; margin-bottom: 0.25rem;">{stage_key}: {stage_data['title']}</h1>
    """, unsafe_allow_html=True)
    
    # New Overview Section
    if "overview" in stage_data:
        st.markdown(f"""
        <div class="glass-card" style="margin-bottom: 2rem; border-left: 4px solid #A78BFA;">
            <p style="color: #E2E8F0; line-height: 1.7; margin-bottom: 0;">{stage_data['overview']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📚 Core Curriculum")
        for topic in stage_data['topics']:
            with st.container():
                st.markdown(f"<div class='topic-category'>{topic['category']}</div>", unsafe_allow_html=True)
                for item in topic['items']:
                    item_text = item['text'] if isinstance(item, dict) else item
                    is_prep = item.get('is_interview_prep', False) if isinstance(item, dict) else False
                    
                    badge_html = '<span style="background:#1E293B; color:#A78BFA; font-size:0.65rem; padding:1px 6px; border-radius:4px; margin-left:8px; border:1px solid #A78BFA44; font-weight:700;">INTERVIEW PREP</span>' if is_prep else ''
                    st.markdown(f"<p style='margin-bottom:0.8rem; line-height:1.6;'>• {item_text}{badge_html}</p>", unsafe_allow_html=True)
        
        # New Step-by-Step Guide Section
        if "guide" in stage_data:
            st.markdown("### 📝 Step-by-Step Guide")
            st.markdown('<div class="guide-container">', unsafe_allow_html=True)
            for step in stage_data['guide']:
                st.markdown(f"<div class='guide-step'>{step}</div>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # New Practical Exercise Section
        if "exercise" in stage_data:
            st.markdown(f"""
            <div class="exercise-box">
                <div class="exercise-header">🚀 Practical Exercise</div>
                {stage_data['exercise']}
            </div>
            """, unsafe_allow_html=True)

        if "milestone" in stage_data:
            st.markdown(f"""
            <div class="milestone-box">
                <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; color: #FBBF24; margin-bottom: 0.75rem;">🎯 Stage Milestone</div>
                <div style="font-size: 0.9rem; line-height: 1.8; color: #CBD5E1;">{stage_data['milestone']}</div>
            </div>
            """, unsafe_allow_html=True)

        # Common Mistakes Section
        if "common_mistakes" in stage_data:
            st.markdown("### ⚠️ Common Mistakes to Avoid")
            for mistake in stage_data['common_mistakes']:
                st.markdown(f"""
            <div style="background: rgba(239,68,68,0.08); border-left: 3px solid #EF4444; border-radius: 0 8px 8px 0;
                        padding: 0.75rem 1rem; margin-bottom: 0.6rem;">
                <span style="font-size: 0.875rem; color: #FCA5A5; line-height: 1.7;">{mistake}</span>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("### 📖 Resources")
        for res in stage_data['resources']:
            st.markdown(f"""
            <a href="{res['url']}" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
                <div class="glass-card resource-card" style="padding: 0.85rem 1rem; margin-bottom: 0.6rem; display: flex; align-items: center; gap: 0.75rem; transition: all 0.2s ease; cursor: pointer;">
                    <span style="font-size: 1.25rem; line-height: 1;">{res['icon']}</span>
                    <div style="flex: 1;">
                        <div style="font-size: 0.875rem; font-weight: 600; color: #E2E8F0; line-height: 1.4;">{res['name']}</div>
                        <div style="font-size: 0.75rem; color: #64748B; margin-top: 0.2rem; word-break: break-all;">{res['url']}</div>
                    </div>
                    <span style="font-size: 0.85rem; color: #A78BFA; opacity: 0.8;">↗</span>
                </div>
            </a>
            """, unsafe_allow_html=True)
            
        st.markdown("### 🛠️ Recommended Tools")
        tools_key = "Stage 1-2" if "1" in stage_key or "2" in stage_key else \
                    "Stage 3-4" if "3" in stage_key or "4" in stage_key else \
                    "Stage 5" if "5" in stage_key else \
                    "Stage 7" if "7" in stage_key else \
                    "Stage 8" if "8" in stage_key else "Stage 6"
        
        for tool in TOOLS_CHECKLIST[tools_key]:
            st.markdown(f"✅ {tool}")

    # --- QUIZ SECTION ---
    if "quiz" in stage_data:
        st.markdown("---")
        st.markdown("### 🧠 The Knowledge Check")
        st.markdown('<p style="color:#94A3B8; font-size:0.9rem; margin-bottom:1.5rem;">Test your mastery of this stage\'s concepts before moving forward.</p>', unsafe_allow_html=True)
        
        quiz_score = 0
        total_qs = len(stage_data["quiz"])
        
        for q_idx, quiz_item in enumerate(stage_data["quiz"]):
            q_key = f"quiz_{stage_key}_{q_idx}"
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1.5rem; margin-bottom: 1rem;">
                <div style="font-size: 0.75rem; font-weight: 700; color: #A78BFA; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.05em;">Question {q_idx + 1}</div>
                <div style="font-size: 1rem; color: #E2E8F0; font-weight: 500; margin-bottom: 1rem;">{quiz_item['question']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Using radio for options
            user_choice = st.radio(
                f"Select an answer for Question {q_idx + 1}",
                options=quiz_item["options"],
                key=q_key,
                label_visibility="collapsed"
            )
            
            # Show feedback immediately if the button was clicked
            btn_key = f"btn_{q_key}"
            submitted_key = f"submitted_{q_key}"
            
            if st.button(f"Submit Answer {q_idx + 1}", key=btn_key):
                st.session_state[submitted_key] = True

            if st.session_state.get(submitted_key, False):
                choice_idx = quiz_item["options"].index(user_choice)
                is_correct = choice_idx == quiz_item["answer"]
                
                if is_correct:
                    st.success("✨ Correct!")
                    quiz_score += 1
                else:
                    st.error("❌ Not quite.")
                
                st.markdown(f"""
                <div style="background: rgba(167,139,250,0.1); border: 1px dashed rgba(167,139,250,0.3); border-radius: 8px; padding: 1rem; margin-top: 0.5rem; margin-bottom: 2rem;">
                    <div style="font-size: 0.75rem; font-weight: 700; color: #A78BFA; margin-bottom: 0.25rem;">PEDAGOGICAL INSIGHT</div>
                    <div style="font-size: 0.85rem; color: #CBD5E1; line-height: 1.6;">{quiz_item['explanation']}</div>
                </div>
                """, unsafe_allow_html=True)

        # Quiz completion summary
        if all(st.session_state.get(f"submitted_quiz_{stage_key}_{i}", False) for i in range(total_qs)):
            st.markdown(f"""
            <div style="background: linear-gradient(90deg, rgba(34,197,94,0.1), rgba(167,139,250,0.1)); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 1.5rem; text-align: center; margin-top: 1rem;">
                <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🎓</div>
                <div style="font-size: 1rem; font-weight: 700; color: #E2E8F0;">Stage Mastery: {quiz_score}/{total_qs}</div>
                <div style="font-size: 0.85rem; color: #94A3B8; margin-top: 0.25rem;">You've completed the knowledge check for {stage_data['title']}.</div>
            </div>
            """, unsafe_allow_html=True)

# --- TOOLS & TRAPS PAGE ---
elif page == "Tools & Traps":
    st.markdown("## 🛠️ The Quant's Toolkit")
    
    cols = st.columns(len(TOOLS_CHECKLIST))
    for i, (stage, tools) in enumerate(TOOLS_CHECKLIST.items()):
        with cols[i]:
            st.markdown(f"""
            <div style="margin-bottom: 0.25rem;">
                <span style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; color: #A78BFA;">{stage}</span>
            </div>
            """, unsafe_allow_html=True)
            for tool in tools:
                st.markdown(f"<p style='font-size:0.875rem; color:#94A3B8; line-height:1.65; margin-bottom:0.3rem;'>• {tool}</p>", unsafe_allow_html=True)
                
    st.markdown("---")
    st.markdown("## ⚠️ The 5 Traps That Kill Researchers")
    
    for trap in TRAPS:
        st.markdown(f"""
        <div class="glass-card trap-card">
            <h4 style="font-size: 0.925rem; font-weight: 700; color: #FCA5A5; margin-top: 0; margin-bottom: 0.5rem;">{trap['title']}</h4>
            <p style="font-size: 0.875rem; line-height: 1.75; color: #94A3B8; margin-bottom: 0;">{trap['description']}</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Built with ❤️ for aspiring Quants")
st.sidebar.markdown("Complete Stage 1–4 to unlock the 90th percentile of researchers.")

# --- GLOSSARY PAGE ---
if page == "📖 Glossary":
    st.markdown("## 📖 Quant Glossary")
    st.markdown('<p style="color:#94A3B8; font-size:0.9rem; margin-bottom:1.5rem;">A searchable reference of all key quantitative finance terms used across the roadmap.</p>', unsafe_allow_html=True)

    GLOSSARY = [
        ("Alpha", "Excess return generated by a strategy above a risk-adjusted benchmark. The 'Holy Grail' of quantitative research."),
        ("Beta", "Sensitivity of a portfolio's returns to the overall market. A Beta of 1.2 means the portfolio moves 1.2x the market."),
        ("Backtest", "Simulation of a trading strategy using historical data to estimate how it would have performed in the past."),
        ("Bid-Ask Spread", "The difference between the highest price a buyer will pay (bid) and the lowest price a seller will accept (ask). A direct cost of trading."),
        ("Black Swan", "An extremely rare, high-impact event (e.g., 2008 financial crisis) that falls far outside normal statistical expectations."),
        ("Brownian Motion", "A continuous-time stochastic process used to model random price movements. The mathematical backbone of most options pricing models."),
        ("Carry Trade", "Borrowing in a low-interest-rate currency and investing in a higher-yielding one. Profits from the interest rate differential."),
        ("Cointegration", "A statistical relationship where two non-stationary series maintain a stable, mean-reverting linear combination over time. The basis of pairs trading."),
        ("Convexity", "The non-linear relationship between bond prices and yields. Also used to describe the positive Gamma exposure of long options positions."),
        ("Delta", "The rate of change of an option's price with respect to a $1 change in the underlying asset. Ranges from 0 to 1 for calls, -1 to 0 for puts."),
        ("Drawdown", "The peak-to-trough decline of a portfolio or strategy's equity curve. Maximum Drawdown is the largest historical loss from peak to trough."),
        ("EV (Expected Value)", "The probability-weighted average outcome of all possible results. A positive EV strategy should generate profit over a large enough sample."),
        ("Factor Model", "A model that explains asset returns via exposure to systematic risk factors (e.g., Market, Size, Value, Momentum in the Fama-French framework)."),
        ("Gamma", "The rate of change of Delta with respect to a $1 move in the underlying. Long gamma positions benefit from large moves in either direction."),
        ("HRP (Hierarchical Risk Parity)", "A portfolio construction method using machine learning and graph theory to allocate risk across asset clusters rather than raw correlations."),
        ("Implied Volatility (IV)", "The market's forward-looking expectation of future price volatility, inferred from current options prices via the Black-Scholes model."),
        ("Information Ratio (IR)", "A measure of risk-adjusted alpha: IR = Alpha / Tracking Error. Quantifies the skill of an active manager relative to their benchmark."),
        ("Kelly Criterion", "A formula for calculating the optimal bet size to maximize long-term portfolio growth: f* = (bp - q) / b."),
        ("Kurtosis", "A measure of the 'fat-tailedness' of a distribution. Financial returns have excess kurtosis (leptokurtosis), meaning crashes are far more frequent than a normal distribution predicts."),
        ("LOB (Limit Order Book)", "A real-time record of all outstanding limit orders at every price level. The central matching engine of modern exchanges."),
        ("Log-Return", "The natural logarithm of the price ratio: ln(P_t / P_{t-1}). Used in finance for its additive properties across time periods."),
        ("Look-Ahead Bias", "A critical backtesting error where future information is unintentionally used to generate past signals, producing artificially inflated results."),
        ("Market Impact", "The adverse price movement caused by a trader's own orders. Large orders 'push' the market against the trader, eroding profitability."),
        ("Meta-Labeling", "A machine learning technique (López de Prado) where a secondary model filters the signals of a primary model to improve Precision."),
        ("OMS / EMS", "Order Management System / Execution Management System. The institutional software stack for routing, tracking, and managing trade orders."),
        ("Overfitting", "When a model is too closely fitted to historical data and captures noise rather than genuine signal, resulting in poor out-of-sample performance."),
        ("P-Value", "The probability of observing a result at least as extreme as the one obtained, assuming the null hypothesis is true. A low p-value (< 0.05) suggests statistical significance."),
        ("Pairs Trading", "A market-neutral strategy that buys an undervalued asset and simultaneously sells an overvalued correlated asset, profiting from convergence."),
        ("PCA (Principal Component Analysis)", "A dimensionality reduction technique that extracts uncorrelated 'factors' from a large dataset. Widely used in factor investing and risk decomposition."),
        ("Realized Volatility (RV)", "The actual historical volatility of an asset, typically measured as the annualized standard deviation of daily log-returns."),
        ("Regime", "A distinct market state characterized by consistent statistical properties (e.g., 'Bull / Low Vol' vs. 'Bear / High Vol'). Strategies can behave very differently across regimes."),
        ("Sharpe Ratio", "Risk-adjusted return metric: (Return - Risk-Free Rate) / Standard Deviation of Returns. The gold standard for comparing strategies."),
        ("Skewness", "A measure of asymmetry in a return distribution. Negative skew means large losses are more frequent than a normal distribution would predict."),
        ("Slippage", "The difference between the expected price of a trade and the actual executed price, caused by market impact and latency."),
        ("Sortino Ratio", "Like the Sharpe Ratio, but only penalizes downside volatility. More appropriate for strategies with asymmetric return profiles."),
        ("Stationarity", "A time series is stationary if its mean, variance, and autocorrelation are constant over time. A required property for most statistical and ML models."),
        ("Survivorship Bias", "The error of only analyzing assets that 'survived' to the present (e.g., stocks still in the S&P 500 today), ignoring delisted or bankrupt companies."),
        ("Theta", "The daily time decay of an option's value. An option loses value each day purely from the passage of time, all else equal."),
        ("Unit Root", "A property of a non-stationary time series (like raw prices) where shocks have permanent effects. Detected via the ADF (Augmented Dickey-Fuller) test."),
        ("Vega", "An option's sensitivity to a 1% change in implied volatility. Long options are always long Vega — they benefit from increases in market fear."),
        ("VIX", "The CBOE Volatility Index, measuring the implied volatility of 30-day SPX options. Often called the 'Fear Gauge' of Wall Street."),
        ("VRP (Volatility Risk Premium)", "The persistent tendency for implied volatility to exceed realized volatility on average. Systematically selling options harvests this premium."),
        ("VWAP", "Volume Weighted Average Price. An execution benchmark used by institutions to minimize market impact when trading large orders."),
        ("Walk-Forward Analysis", "An out-of-sample testing method where a model is trained on a rolling window and tested on the immediately following period, mimicking live deployment."),
        ("Z-Score", "A standardized measure of how many standard deviations a value is from the mean: Z = (X - μ) / σ. The core signal in mean-reversion strategies."),
    ]

    search_query = st.text_input("🔍 Search terms...", placeholder="e.g. Sharpe, Delta, Cointegration...").lower()
    filtered = [(t, d) for t, d in GLOSSARY if search_query in t.lower() or search_query in d.lower()] if search_query else GLOSSARY

    st.markdown(f'<p style="color:#64748B; font-size:0.8rem; margin-bottom:1rem;">{len(filtered)} term{"s" if len(filtered) != 1 else ""} found</p>', unsafe_allow_html=True)

    for term, definition in filtered:
        st.markdown(f"""
        <div style="background: rgba(167,139,250,0.07); border: 1px solid rgba(167,139,250,0.15); border-radius: 10px;
                    padding: 0.85rem 1.1rem; margin-bottom: 0.5rem;">
            <div style="font-size: 0.875rem; font-weight: 700; color: #A78BFA; margin-bottom: 0.3rem;">{term}</div>
            <div style="font-size: 0.85rem; color: #94A3B8; line-height: 1.7;">{definition}</div>
        </div>
        """, unsafe_allow_html=True)

# --- PROGRESS TRACKER PAGE ---
elif page == "✅ My Progress":
    st.markdown("## ✅ My Learning Progress")
    st.markdown('<p style="color:#94A3B8; font-size:0.9rem; margin-bottom:1.5rem;">Track your journey through the Quant Roadmap. Your progress is saved for this session.</p>', unsafe_allow_html=True)

    # Initialize progress state
    if "progress" not in st.session_state:
        st.session_state.progress = {}

    stage_milestones = {
        k: {
            "title": v["title"],
            "duration": v["duration"],
            "milestone": v.get("milestone", ""),
            "topics": [(item['text'] if isinstance(item, dict) else item) for topic in v["topics"] for item in topic["items"]]
        }
        for k, v in ROADMAP_DATA.items()
    }

    total_topics = sum(len(s["topics"]) for s in stage_milestones.values())
    completed_topics = sum(1 for key in st.session_state.progress if st.session_state.progress[key])
    overall_pct = int((completed_topics / total_topics) * 100) if total_topics > 0 else 0

    # Overall progress bar
    bar_color = "#22C55E" if overall_pct >= 75 else "#A78BFA" if overall_pct >= 40 else "#FBBF24"
    st.markdown(f"""
    <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 1.25rem 1.5rem; margin-bottom: 1.75rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.6rem;">
            <span style="font-size:0.9rem; font-weight:700; color:#E2E8F0;">Overall Roadmap Completion</span>
            <span style="font-size:1.4rem; font-weight:800; color:{bar_color};">{overall_pct}%</span>
        </div>
        <div style="background:rgba(255,255,255,0.07); border-radius:999px; height:10px; overflow:hidden;">
            <div style="width:{overall_pct}%; height:100%; background:linear-gradient(90deg,{bar_color},{bar_color}CC); border-radius:999px; transition:width 0.4s ease;"></div>
        </div>
        <div style="font-size:0.78rem; color:#64748B; margin-top:0.5rem;">{completed_topics} of {total_topics} concepts marked complete</div>
    </div>
    """, unsafe_allow_html=True)

    for stage_key, stage in stage_milestones.items():
        stage_topic_keys = [f"{stage_key}_{i}" for i in range(len(stage["topics"]))]
        stage_done = sum(1 for k in stage_topic_keys if st.session_state.progress.get(k, False))
        stage_total = len(stage_topic_keys)
        stage_pct = int((stage_done / stage_total) * 100) if stage_total > 0 else 0

        with st.expander(f"{stage_key}: {stage['title']} — {stage_pct}% complete  ({stage['duration']})", expanded=False):
            st.markdown(f"""
            <div style="background:rgba(255,255,255,0.04); border-radius:8px; height:6px; margin-bottom:1rem; overflow:hidden;">
                <div style="width:{stage_pct}%; height:100%; background:linear-gradient(90deg,#A78BFA,#7C3AED); border-radius:8px;"></div>
            </div>
            """, unsafe_allow_html=True)

            if stage["milestone"]:
                st.markdown(f'<div style="font-size:0.8rem; color:#FBBF24; margin-bottom:0.85rem;">🎯 Milestone: {stage["milestone"]}</div>', unsafe_allow_html=True)

            for i, item in enumerate(stage["topics"]):
                key = f"{stage_key}_{i}"
                label = item.split(":")[0].strip() if ":" in item else item[:50].strip() + "..."
                checked = st.checkbox(f"{label}", key=key, value=st.session_state.progress.get(key, False))
                st.session_state.progress[key] = checked

    if st.button("🔄 Reset All Progress", type="secondary"):
        st.session_state.progress = {}
        # Clear all quiz submissions
        keys_to_delete = [k for k in st.session_state.keys() if k.startswith("submitted_quiz_")]
        for k in keys_to_delete:
            del st.session_state[k]
        st.rerun()
