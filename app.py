# app.py
import streamlit as st
import os
from content import ROADMAP_DATA, TRAPS, TOOLS_CHECKLIST
from styles import apply_styles

# --- CONFIGURATION ---
st.set_page_config(
    page_title="Quantitative Trading Research Roadmap",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom styling
apply_styles()

# --- STATE MANAGEMENT ---
if 'sidebar_radio' not in st.session_state:
    st.session_state.sidebar_radio = "Overview"

if 'progress' not in st.session_state:
    st.session_state.progress = {}

# Helper to change page
def navigate_to(page_name):
    st.session_state.sidebar_radio = page_name

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h2 style="color: #00F2FF; margin-bottom: 0;">QUANT LAB</h2>
            <p style="color: #64748B; font-size: 0.8rem;">Research & Execution Roadmap</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Navigation list
    PAGES = ["Overview"] + [f"{key}: {val['title']}" for key, val in ROADMAP_DATA.items()] + ["Tools & Traps", "Progress Tracker"]
    
    page = st.radio(
        "Navigation",
        options=PAGES,
        key="sidebar_radio",
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.caption("v1.2.0 | Institutional Grade")

# --- OVERVIEW PAGE ---
if page == "Overview":
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        st.markdown(f"""
        <div class="hero-container" style="background-image: url('https://images.unsplash.com/photo-1611974717482-58a25a921820?auto=format&fit=crop&q=80&w=2000');">
            <div class="hero-overlay"></div>
            <div class="hero-content">
                <h1 class="hero-title">Quantitative Trading Research</h1>
                <p class="hero-subtitle">The Institutional Path to Alpha Generation</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🏹 The Mission")
        st.markdown("""
        <div class="tutorial-overview">
            Welcome to the <strong>Quant Lab</strong>. This is not a retail course; it is an institutional-grade 
            roadmap for those who seek to understand the mathematical and computational engines behind 
            global finance. We focus on <strong>Research Rigor</strong>, <strong>Execution Physics</strong>, 
            and <strong>Risk Discipline</strong>.
        </div>
        """, unsafe_allow_html=True)

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
            <div class="timeline-step">8</div>
            <div class="timeline-step">9</div>
            <div class="timeline-step">10</div>
            <div class="timeline-step">11</div>
            <div class="timeline-step">12</div>
            <div class="timeline-step">13</div>
            <div class="timeline-step">14</div>
            <div class="timeline-step">15</div>
            <div class="timeline-step">16</div>
        </div>
        """
        st.markdown(timeline_html, unsafe_allow_html=True)

    st.markdown("---")
    
    # --- SEARCH & FILTERS ---
    st.markdown("### 🔍 Discovery")
    search_col, filter_col = st.columns([2, 1])
    
    with search_col:
        search_query = st.text_input("Search topics, tools, or concepts...", placeholder="e.g. 'Log-Returns', 'C++', 'Sharpe Ratio'", key="roadmap_search")
    
    with filter_col:
        difficulty_filter = st.multiselect(
            "Filter by Difficulty",
            options=["Beginner", "Intermediate", "Advanced", "Expert"],
            default=[]
        )

    # Filter Logic
    filtered_stages = []
    for s_key, s_data in ROADMAP_DATA.items():
        # Match Search Query
        match_search = True
        if search_query:
            all_content = f"{s_data['title']} {s_data['overview']} {s_data['goal']}".lower()
            # Also search topics
            for cat in s_data['topics']:
                all_content += f" {cat['category']}".lower()
                for item in cat['items']:
                    item_text = item['text'] if isinstance(item, dict) else item
                    all_content += f" {item_text}".lower()
            
            match_search = search_query.lower() in all_content
        
        # Match Difficulty
        match_diff = True
        if difficulty_filter:
            match_diff = s_data['difficulty'] in difficulty_filter
            
        if match_search and match_diff:
            filtered_stages.append((s_key, s_data))

    if not filtered_stages:
        st.info("No stages match your search or filter criteria. Try broadening your search.")
    else:
        # Render Filtered Grid
        cols = st.columns(2)
        for idx, (key, stage) in enumerate(filtered_stages):
            with cols[idx % 2]:
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
                    if isinstance(item, dict):
                        item_text = item.get('text', '')
                        is_prep = item.get('is_interview_prep', False)
                        code_snippet = item.get('code', None)
                    else:
                        item_text = item
                        is_prep = False
                        code_snippet = None
                    
                    badge_html = '<span style="background:#1E293B; color:#A78BFA; font-size:0.65rem; padding:1px 6px; border-radius:4px; margin-left:8px; border:1px solid #A78BFA44; font-weight:700;">INTERVIEW PREP</span>' if is_prep else ''
                    
                    # Render text with LaTeX support
                    # We use a wrapper to maintain the dot/bullet style but let Streamlit handle the LaTeX
                    st.markdown(f"**•** {item_text} {badge_html}", unsafe_allow_html=True)
                    
                    if code_snippet:
                        st.code(code_snippet, language="python")
        
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

        # Glossary Card Section
        if "glossary" in stage_data:
            st.markdown("---")
            st.markdown("### 📖 Stage Glossary")
            cols = st.columns(len(stage_data["glossary"]))
            for idx, item in enumerate(stage_data["glossary"]):
                with cols[idx]:
                    st.markdown(f"""
                    <div class="glass-card" style="padding: 1.25rem; height: 100%; border-top: 3px solid #A78BFA;">
                        <div style="font-size: 0.75rem; font-weight: 700; color: #A78BFA; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem;">{item['term']}</div>
                        <div style="font-size: 0.85rem; color: #CBD5E1; line-height: 1.5;">{item['definition']}</div>
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
        import re
        match = re.search(r'\d+', stage_key)
        stage_num = int(match.group()) if match else 0
        if stage_num in (1, 2):
            tools_key = "Stage 1-2"
        elif stage_num in (3, 4):
            tools_key = "Stage 3-4"
        else:
            tools_key = f"Stage {stage_num}"
            
        if tools_key not in TOOLS_CHECKLIST:
            tools_key = "Stage 6"
        
        for tool in TOOLS_CHECKLIST[tools_key]:
            st.markdown(f"✅ {tool}")

    # --- QUIZ SECTION ---
    if "quiz" in stage_data:
        import random
        st.markdown("---")
        st.markdown("### 🧠 The Knowledge Check")
        st.markdown('<p style="color:#94A3B8; font-size:0.9rem; margin-bottom:1.5rem;">Test your mastery of this stage\'s concepts before moving forward.</p>', unsafe_allow_html=True)
        
        quiz_score = 0
        
        quiz_indices_key = f"quiz_indices_{stage_key}"
        if quiz_indices_key not in st.session_state:
            pool_size = len(stage_data["quiz"])
            sample_size = min(5, pool_size)
            st.session_state[quiz_indices_key] = random.sample(range(pool_size), sample_size)
            
        selected_indices = st.session_state[quiz_indices_key]
        total_qs = len(selected_indices)
        
        for q_idx_disp, original_idx in enumerate(selected_indices):
            quiz_item = stage_data["quiz"][original_idx]
            q_key = f"quiz_{stage_key}_{original_idx}"
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1.5rem; margin-bottom: 1rem;">
                <div style="font-size: 0.75rem; font-weight: 700; color: #A78BFA; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.05em;">Question {q_idx_disp + 1}</div>
                <div style="font-size: 1rem; color: #E2E8F0; font-weight: 500; margin-bottom: 1rem;">{quiz_item['question']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Using radio for options
            user_choice = st.radio(
                f"Select an answer for Question {q_idx_disp + 1}",
                options=quiz_item["options"],
                key=q_key,
                label_visibility="collapsed"
            )
            
            # Show feedback immediately if the button was clicked
            btn_key = f"btn_{q_key}"
            submitted_key = f"submitted_{q_key}"
            
            if st.button(f"Submit Answer {q_idx_disp + 1}", key=btn_key):
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
        if all(st.session_state.get(f"submitted_quiz_{stage_key}_{idx}", False) for idx in selected_indices):
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
    st.markdown("## 🪤 Common Pitfalls & Traps")
    
    for trap in TRAPS:
        with st.expander(f"⚠️ {trap['title']}", expanded=False):
            st.markdown(f"""
            <div class="glass-card trap-card">
                <p>{trap['description']}</p>
            </div>
            """, unsafe_allow_html=True)

# --- PROGRESS TRACKER PAGE ---
elif page == "Progress Tracker":
    st.markdown("## 📈 Your Research Progress")
    
    total_topics = sum(len(stage["topics"]) for stage in ROADMAP_DATA.values())
    completed_topics = len(st.session_state.progress)
    overall_pct = int((completed_topics / total_topics) * 100) if total_topics > 0 else 0

    st.markdown(f"""
    <div class="glass-card" style="text-align: center; padding: 2rem;">
        <div style="font-size: 0.875rem; font-weight: 700; color: #A78BFA; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.5rem;">Overall Completion</div>
        <div style="font-size: 3.5rem; font-weight: 800; color: #F1F5F9; line-height: 1;">{overall_pct}%</div>
        <div style="background: rgba(255,255,255,0.05); border-radius: 999px; height: 12px; margin-top: 1.5rem; overflow: hidden;">
            <div style="width: {overall_pct}%; height: 100%; background: linear-gradient(90deg, #00F2FF, #8A2BE2); box-shadow: 0 0 20px rgba(0, 242, 255, 0.4);"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    for stage_key, stage in ROADMAP_DATA.items():
        # Get flattened list of items for this stage
        stage_items = []
        for cat in stage["topics"]:
            for item in cat["items"]:
                stage_items.append(item)
        
        stage_topic_keys = [f"{stage_key}_{i}" for i in range(len(stage_items))]
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

            for i, item in enumerate(stage_items):
                item_text = item['text'] if isinstance(item, dict) else item
                key = f"{stage_key}_{i}"
                label = item_text.split(":")[0].strip() if ":" in item_text else item_text[:50].strip() + "..."
                
                checked = st.checkbox(f"{label}", key=key, value=st.session_state.progress.get(key, False))
                st.session_state.progress[key] = checked

    if st.button("🔄 Reset All Progress", type="secondary"):
        st.session_state.progress = {}
        # Clear all quiz submissions and randomly selected questions
        keys_to_delete = [k for k in st.session_state.keys() if k.startswith("submitted_quiz_") or k.startswith("quiz_indices_")]
        for k in keys_to_delete:
            del st.session_state[k]
        st.rerun()
