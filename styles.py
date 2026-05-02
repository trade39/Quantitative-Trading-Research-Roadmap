# styles.py
import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=JetBrains+Mono:wght@400;500&display=swap');

        /* ═══════════════════════════════════
           BASE & TYPOGRAPHY SYSTEM
        ═══════════════════════════════════ */
        html, body, [data-testid="stAppViewContainer"] {
            font-family: 'Inter', sans-serif;
            background-color: #0E1117;
            color: #C8D6E5;
            font-size: 15px;
            line-height: 1.7;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }

        /* Global heading resets */
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Inter', sans-serif;
            font-weight: 700;
            letter-spacing: -0.02em;
            line-height: 1.25;
            color: #EDF2F7;
            margin-top: 0;
        }

        /* Streamlit native headings */
        [data-testid="stMarkdownContainer"] h1 {
            font-size: 2.25rem;
            font-weight: 800;
            letter-spacing: -0.03em;
            color: #F1F5F9;
            margin-bottom: 1.25rem;
            padding-bottom: 0.75rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }

        [data-testid="stMarkdownContainer"] h2 {
            font-size: 1.75rem;
            font-weight: 700;
            color: #E2E8F0;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }

        [data-testid="stMarkdownContainer"] h3 {
            font-size: 1.2rem;
            font-weight: 600;
            color: #CBD5E1;
            margin-top: 1.75rem;
            margin-bottom: 0.75rem;
            letter-spacing: -0.01em;
        }

        [data-testid="stMarkdownContainer"] h4 {
            font-size: 1rem;
            font-weight: 600;
            color: #94A3B8;
            margin-top: 1.25rem;
            margin-bottom: 0.5rem;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            font-size: 0.8rem;
        }

        /* Paragraph & body text */
        [data-testid="stMarkdownContainer"] p {
            font-size: 0.9375rem;
            line-height: 1.8;
            color: #94A3B8;
            margin-bottom: 1rem;
        }

        /* Bullet lists */
        [data-testid="stMarkdownContainer"] ul,
        [data-testid="stMarkdownContainer"] ol {
            padding-left: 1.5rem;
            margin-bottom: 0.75rem;
        }

        [data-testid="stMarkdownContainer"] li {
            font-size: 0.9375rem;
            line-height: 1.75;
            color: #94A3B8;
            margin-bottom: 0.35rem;
        }

        /* Strong / emphasis */
        [data-testid="stMarkdownContainer"] strong {
            color: #E2E8F0;
            font-weight: 600;
        }

        [data-testid="stMarkdownContainer"] em {
            color: #CBD5E1;
            font-style: italic;
        }

        /* Inline code */
        [data-testid="stMarkdownContainer"] code {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.825rem;
            background: rgba(0, 242, 255, 0.08);
            color: #67E8F9;
            padding: 0.15em 0.45em;
            border-radius: 4px;
            border: 1px solid rgba(0, 242, 255, 0.15);
        }

        /* Horizontal rule */
        hr {
            border: none;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            margin: 2.5rem 0;
        }

        /* ═══════════════════════════════════
           LAYOUT & CONTAINER SPACING
        ═══════════════════════════════════ */
        .main .block-container {
            max-width: 1200px !important;
            padding-top: 3rem !important;
            padding-bottom: 5rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
        }

        /* Column gaps */
        [data-testid="column"] {
            gap: 1.5rem;
        }

        /* ═══════════════════════════════════
           HOVER-EXPAND SIDEBAR
        ═══════════════════════════════════ */
        [data-testid="stSidebar"] {
            min-width: 80px !important;
            max-width: 80px !important;
            width: 80px !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            background-color: rgba(17, 25, 40, 0.9) !important;
            backdrop-filter: blur(20px) !important;
            border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
            overflow: hidden !important;
            z-index: 1000 !important;
        }

        [data-testid="stSidebar"]:hover {
            min-width: 300px !important;
            max-width: 300px !important;
            width: 300px !important;
            box-shadow: 10px 0 40px rgba(0, 0, 0, 0.6) !important;
        }

        [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
            width: 260px !important;
            opacity: 0;
            transition: opacity 0.2s ease;
            padding-left: 1.25rem !important;
            padding-right: 1.25rem !important;
        }

        [data-testid="stSidebar"]:hover [data-testid="stVerticalBlock"] {
            opacity: 1;
        }

        /* Sidebar heading */
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {
            font-size: 1rem !important;
            font-weight: 700 !important;
            letter-spacing: 0.04em !important;
            color: #E2E8F0 !important;
            margin-bottom: 1rem !important;
        }

        /* Sidebar radio labels */
        [data-testid="stSidebar"] .stRadio label {
            font-size: 0.875rem !important;
            color: #94A3B8 !important;
            line-height: 1.6 !important;
            white-space: nowrap !important;
        }

        /* Sidebar caption */
        [data-testid="stSidebar"] .stCaption {
            font-size: 0.75rem !important;
            color: #475569 !important;
            line-height: 1.6 !important;
        }

        /* Collapsed Sidebar Icon */
        [data-testid="stSidebar"]::before {
            content: '🚀';
            position: absolute;
            top: 2rem;
            left: 50%;
            transform: translateX(-50%);
            font-size: 1.4rem;
            opacity: 1;
            transition: opacity 0.2s ease;
        }

        [data-testid="stSidebar"]:hover::before {
            opacity: 0;
        }

        [data-testid="collapsedControl"] {
            display: none !important;
        }

        [data-testid="stSidebarContent"] {
            overflow-x: hidden !important;
        }

        /* ═══════════════════════════════════
           HERO SECTION
        ═══════════════════════════════════ */
        .hero-container {
            position: relative;
            height: 320px;
            border-radius: 20px;
            overflow: hidden;
            margin-bottom: 2.5rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            background-size: cover;
            background-position: center;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
        }

        .hero-overlay {
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: linear-gradient(180deg, rgba(14, 17, 23, 0.1) 0%, rgba(14, 17, 23, 0.82) 100%);
        }

        .hero-content {
            position: relative;
            z-index: 1;
            padding: 2.5rem;
        }

        .hero-title {
            font-size: 3rem;
            font-weight: 800;
            letter-spacing: -0.04em;
            background: linear-gradient(90deg, #00F2FF, #8A2BE2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.6rem;
            line-height: 1.1;
        }

        .hero-subtitle {
            font-size: 1.05rem;
            color: #94A3B8;
            font-weight: 400;
            letter-spacing: 0.01em;
        }

        /* ═══════════════════════════════════
           GLASSMORPHISM CARDS
        ═══════════════════════════════════ */
        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.09);
            padding: 1.5rem 1.75rem;
            margin-bottom: 1rem;
            transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
        }

        .glass-card:hover {
            transform: translateY(-4px);
            border-color: rgba(0, 242, 255, 0.35);
            box-shadow: 0 12px 36px rgba(0, 0, 0, 0.45);
        }

        .glass-card h3 {
            font-size: 1.05rem;
            font-weight: 700;
            color: #E2E8F0;
            margin-top: 0.75rem;
            margin-bottom: 0.5rem;
        }

        .glass-card p {
            font-size: 0.875rem;
            color: #64748B;
            line-height: 1.65;
            margin-bottom: 0;
        }

        /* ═══════════════════════════════════
           CLICKABLE CARD WRAPPER
        ═══════════════════════════════════ */
        .card-wrapper {
            position: relative;
            cursor: pointer;
        }

        .card-wrapper .stButton {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 10;
        }

        .card-wrapper .stButton > button {
            width: 100% !important;
            height: 150px !important;
            opacity: 0 !important;
            border: none !important;
            background: transparent !important;
            cursor: pointer !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        .card-wrapper .stButton > button:hover {
            background: transparent !important;
            border: none !important;
        }

        .card-wrapper .stButton > button:focus {
            box-shadow: none !important;
            outline: none !important;
        }

        /* ═══════════════════════════════════
           STAGE BADGE
        ═══════════════════════════════════ */
        .stage-badge {
            background: rgba(0, 242, 255, 0.08);
            color: #22D3EE;
            padding: 0.3rem 0.9rem;
            border-radius: 999px;
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            border: 1px solid rgba(0, 242, 255, 0.2);
            margin-bottom: 0.85rem;
            display: inline-block;
        }

        /* ═══════════════════════════════════
           TOPIC CATEGORY SUBHEADINGS
        ═══════════════════════════════════ */
        .topic-category {
            color: #A78BFA;
            font-weight: 700;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-top: 1.5rem;
            margin-bottom: 0.6rem;
            padding-bottom: 0.35rem;
            border-bottom: 1px solid rgba(167, 139, 250, 0.2);
        }

        /* ═══════════════════════════════════
           MILESTONE BOX
        ═══════════════════════════════════ */
        .milestone-box {
            background: rgba(255, 215, 0, 0.04);
            border-left: 3px solid #FBBF24;
            padding: 1.25rem 1.5rem;
            border-radius: 4px 12px 12px 4px;
            margin-top: 2rem;
        }

        .milestone-box p,
        .milestone-box li {
            font-size: 0.9rem;
            line-height: 1.75;
            color: #CBD5E1;
        }

        /* ═══════════════════════════════════
           ROADMAP TIMELINE
        ═══════════════════════════════════ */
        .roadmap-timeline {
            display: flex;
            justify-content: space-between;
            margin-bottom: 2.5rem;
            position: relative;
            padding: 0 1rem;
        }

        .roadmap-timeline::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 0;
            right: 0;
            height: 2px;
            background: rgba(255, 255, 255, 0.08);
            z-index: 0;
        }

        .timeline-step {
            width: 42px;
            height: 42px;
            border-radius: 50%;
            background: #1e293b;
            border: 2px solid rgba(255, 255, 255, 0.15);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 1;
            font-weight: 700;
            font-size: 0.875rem;
            cursor: pointer;
            transition: all 0.3s ease;
            color: #64748B;
        }

        .timeline-step.active {
            background: #00F2FF;
            color: #0E1117;
            border-color: #00F2FF;
            box-shadow: 0 0 18px rgba(0, 242, 255, 0.55);
        }

        /* ═══════════════════════════════════
           RESOURCE LINKS
        ═══════════════════════════════════ */
        .resource-link {
            color: #64748B;
            text-decoration: none;
            display: block;
            margin-bottom: 0.5rem;
            font-size: 0.875rem;
            transition: color 0.2s;
        }

        .resource-link:hover {
            color: #00F2FF;
        }

        /* ═══════════════════════════════════
           TRAP CARD
        ═══════════════════════════════════ */
        .trap-card {
            border-left: 3px solid #EF4444 !important;
            background: rgba(239, 68, 68, 0.04) !important;
        }

        .trap-card h4 {
            font-size: 0.925rem !important;
            font-weight: 700 !important;
            color: #FCA5A5 !important;
            margin-top: 0 !important;
            margin-bottom: 0.5rem !important;
        }

        .trap-card p {
            font-size: 0.875rem !important;
            line-height: 1.7 !important;
            color: #94A3B8 !important;
            margin-bottom: 0 !important;
        }

        /* ═══════════════════════════════════
           TUTORIAL / OVERVIEW BOX
        ═══════════════════════════════════ */
        .tutorial-overview {
            font-size: 0.9375rem;
            line-height: 1.85;
            color: #94A3B8;
            margin-bottom: 2rem;
            padding: 1.5rem 2rem;
            background: rgba(0, 242, 255, 0.03);
            border-radius: 12px;
            border-left: 3px solid #00F2FF;
        }

        .tutorial-overview strong {
            color: #E2E8F0;
        }

        /* ═══════════════════════════════════
           GUIDE CONTAINER
        ═══════════════════════════════════ */
        .guide-container {
            background: rgba(138, 43, 226, 0.04);
            border-radius: 14px;
            padding: 1.5rem 1.75rem;
            margin-top: 1.25rem;
            border: 1px dashed rgba(167, 139, 250, 0.25);
        }

        .guide-step {
            margin-bottom: 1rem;
            display: flex;
            align-items: flex-start;
            font-size: 0.9rem;
            line-height: 1.75;
            color: #94A3B8;
        }

        .guide-step:last-child {
            margin-bottom: 0;
        }

        /* ═══════════════════════════════════
           EXERCISE BOX
        ═══════════════════════════════════ */
        .exercise-box {
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.07) 0%, rgba(5, 150, 105, 0.03) 100%);
            border: 1px solid rgba(16, 185, 129, 0.18);
            padding: 1.5rem 1.75rem;
            border-radius: 14px;
            margin-top: 2rem;
        }

        .exercise-header {
            color: #34D399;
            font-weight: 700;
            font-size: 0.875rem;
            text-transform: uppercase;
            letter-spacing: 0.07em;
            margin-bottom: 0.75rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .exercise-box p,
        .exercise-box li {
            font-size: 0.9rem;
            line-height: 1.78;
            color: #94A3B8;
        }

        /* ═══════════════════════════════════
           STREAMLIT BUTTON OVERRIDES
        ═══════════════════════════════════ */
        .stButton > button {
            font-family: 'Inter', sans-serif !important;
            font-size: 0.8rem !important;
            font-weight: 600 !important;
            letter-spacing: 0.04em !important;
            border-radius: 8px !important;
            padding: 0.5rem 1.2rem !important;
            transition: all 0.2s ease !important;
        }

        /* ═══════════════════════════════════
           STREAMLIT EXPANDER
        ═══════════════════════════════════ */
        [data-testid="stExpander"] summary {
            font-size: 0.9rem !important;
            font-weight: 600 !important;
            color: #CBD5E1 !important;
            letter-spacing: 0.01em !important;
        }

        /* ═══════════════════════════════════
           MISCELLANEOUS
        ═══════════════════════════════════ */
        [data-testid="stAppViewContainer"] {
            padding-left: 0 !important;
        }

        /* Divider lines */
        [data-testid="stMarkdownContainer"] hr {
            margin: 2rem 0;
        }

        /* Caption text */
        .stCaption, [data-testid="stCaptionContainer"] {
            font-size: 0.78rem !important;
            line-height: 1.6 !important;
            color: #475569 !important;
        }
        </style>
    """, unsafe_allow_html=True)
