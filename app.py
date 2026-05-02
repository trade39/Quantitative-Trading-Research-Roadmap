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
         "Stage 4: Strategy", "Stage 5: Advanced", "Stage 6: Professional", "Stage 7: Macroeconomics", "Tools & Traps"]

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
            st.markdown(f"""
            <div class="glass-card">
                <span class="stage-badge">{stage['duration']}</span>
                <h3 style="font-size: 1.05rem; font-weight: 700; color: #E2E8F0; margin-top: 0.85rem; margin-bottom: 0.4rem; letter-spacing: -0.01em;">{key}: {stage['title']}</h3>
                <p style="font-size: 0.875rem; color: #64748B; line-height: 1.65; margin-bottom: 0;">{stage['goal']}</p>
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
    <div style="margin-bottom: 0.35rem;">
        <span class="stage-badge">{stage_data['duration']}</span>
    </div>
    <h1 style="font-size: 2rem; font-weight: 800; letter-spacing: -0.03em; color: #F1F5F9; margin-top: 0.25rem; margin-bottom: 0.25rem;">{stage_key}: {stage_data['title']}</h1>
    """, unsafe_allow_html=True)
    
    # New Overview Section
    if "overview" in stage_data:
        st.markdown(f"""
        <div class="tutorial-overview">
            {stage_data['overview']}
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📚 Core Curriculum")
        for topic in stage_data['topics']:
            with st.container():
                st.markdown(f"<div class='topic-category'>{topic['category']}</div>", unsafe_allow_html=True)
                for item in topic['items']:
                    st.markdown(f"• {item}")
        
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

    with col2:
        st.markdown("### 📖 Resources")
        for res in stage_data['resources']:
            st.markdown(f"<div class='glass-card' style='padding: 1rem;'>{res}</div>", unsafe_allow_html=True)
            
        st.markdown("### 🛠️ Recommended Tools")
        tools_key = "Stage 1-2" if "1" in stage_key or "2" in stage_key else \
                    "Stage 3-4" if "3" in stage_key or "4" in stage_key else \
                    "Stage 5" if "5" in stage_key else \
                    "Stage 6" if "6" in stage_key else "Stage 6" # Default to Stage 6 tools for Macro
        
        for tool in TOOLS_CHECKLIST[tools_key]:
            st.markdown(f"✅ {tool}")

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
