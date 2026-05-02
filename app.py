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
         "Stage 4: Strategy", "Stage 5: Advanced", "Stage 6: Professional", "Tools & Traps"]

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
                <p style="font-size: 1.2rem; color: #A1A1AA;">The Complete 19-Month Learning Journey</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### 🗺️ The Path to Mastery")
        st.markdown("""
        The journey from absolute beginner to professional quantitative researcher is a multi-phase evolution. 
        Each stage builds the foundation for the next. Completion of Stages 1–4 alone puts you ahead of 90% of retail traders.
        """)
        
        # Timeline Visualization
        timeline_html = """
        <div class="roadmap-timeline">
            <div class="timeline-step active">1</div>
            <div class="timeline-step">2</div>
            <div class="timeline-step">3</div>
            <div class="timeline-step">4</div>
            <div class="timeline-step">5</div>
            <div class="timeline-step">6</div>
        </div>
        """
        st.markdown(timeline_html, unsafe_allow_html=True)
        
        # Summary Cards
        for i, (key, stage) in enumerate(ROADMAP_DATA.items()):
            target_page = f"{key}: {stage['title']}"
            
            # Create a clickable wrapper
            with st.container():
                st.markdown(f'<div class="card-wrapper">', unsafe_allow_html=True)
                
                # Invisible button that covers the card (using callback for safe state update)
                st.button(f"Go to {key}", key=f"btn_{key}", on_click=navigate_to, args=(target_page,), use_container_width=True)
                
                # Visual representation
                st.markdown(f"""
                <div class="glass-card">
                    <span class="stage-badge">{stage['duration']}</span>
                    <h3>{key}: {stage['title']}</h3>
                    <p style="color: #A1A1AA;">{stage['goal']}</p>
                </div>
                """, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

# --- STAGE PAGES ---
elif "Stage" in page:
    stage_key = page.split(":")[0].strip()
    stage_data = ROADMAP_DATA[stage_key]
    
    st.markdown(f"## {stage_key}: {stage_data['title']}")
    st.markdown(f"<span class='stage-badge'>{stage_data['duration']}</span>", unsafe_allow_html=True)
    
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
                <div style="font-weight: bold; color: #FFD700; margin-bottom: 0.5rem;">🎯 Stage Milestone</div>
                {stage_data['milestone']}
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("### 📖 Resources")
        for res in stage_data['resources']:
            st.markdown(f"<div class='glass-card' style='padding: 1rem;'>{res}</div>", unsafe_allow_html=True)
            
        st.markdown("### 🛠️ Recommended Tools")
        tools_key = "Stage 1-2" if "1" in stage_key or "2" in stage_key else \
                    "Stage 3-4" if "3" in stage_key or "4" in stage_key else \
                    "Stage 5" if "5" in stage_key else "Stage 6"
        
        for tool in TOOLS_CHECKLIST[tools_key]:
            st.markdown(f"✅ {tool}")

# --- TOOLS & TRAPS PAGE ---
elif page == "Tools & Traps":
    st.markdown("## 🛠️ The Quant's Toolkit")
    
    cols = st.columns(len(TOOLS_CHECKLIST))
    for i, (stage, tools) in enumerate(TOOLS_CHECKLIST.items()):
        with cols[i]:
            st.markdown(f"#### {stage}")
            for tool in tools:
                st.markdown(f"• {tool}")
                
    st.markdown("---")
    st.markdown("## ⚠️ The 5 Traps That Kill Researchers")
    
    for trap in TRAPS:
        st.markdown(f"""
        <div class="glass-card trap-card">
            <h4 style="color: #EF4444; margin-top:0;">{trap['title']}</h4>
            <p style="margin-bottom:0;">{trap['description']}</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Built with ❤️ for aspiring Quants")
st.sidebar.markdown("Complete Stage 1–4 to unlock the 90th percentile of researchers.")
