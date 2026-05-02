# styles.py
import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

        /* Base styles */
        html, body, [data-testid="stAppViewContainer"] {
            font-family: 'Inter', sans-serif;
            background-color: #0E1117;
            color: #E2E8F0;
        }

        /* Sidebar Hover Effect */
        section[data-testid="stSidebar"] {
            width: 80px !important;
            min-width: 80px !important;
            transition: width 0.3s ease-in-out !important;
            background-color: rgba(17, 25, 40, 0.8) !important;
            backdrop-filter: blur(15px) !important;
            border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
            overflow-x: hidden !important;
        }

        section[data-testid="stSidebar"]:hover {
            width: 320px !important;
            min-width: 320px !important;
            background-color: rgba(17, 25, 40, 0.98) !important;
        }

        /* Sidebar Content Visibility */
        [data-testid="stSidebarContent"] {
            width: 320px !important;
            transition: opacity 0.3s ease;
        }

        section[data-testid="stSidebar"]:not(:hover) [data-testid="stSidebarContent"] {
            opacity: 0;
            pointer-events: none;
        }

        /* Adjust Main Content Area */
        [data-testid="stAppViewContainer"] {
            margin-left: 0 !important;
        }
        
        .main .block-container {
            padding-left: 100px !important;
            padding-right: 2rem !important;
        }

        /* Sidebar indicator when collapsed */
        section[data-testid="stSidebar"]::before {
            content: '🚀';
            position: absolute;
            top: 25px;
            left: 28px;
            font-size: 24px;
            z-index: 1001;
            transition: opacity 0.3s;
        }

        section[data-testid="stSidebar"]:not(:hover)::before {
            opacity: 1;
        }

        section[data-testid="stSidebar"]:hover::before {
            opacity: 0;
        }

        /* Hero section */
        .hero-container {
            position: relative;
            height: 300px;
            border-radius: 20px;
            overflow: hidden;
            margin-bottom: 2rem;
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
            background: linear-gradient(180deg, rgba(14, 17, 23, 0) 0%, rgba(14, 17, 23, 0.8) 100%);
        }
        
        .hero-content {
            position: relative;
            z-index: 1;
            padding: 2rem;
        }

        .hero-title {
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(90deg, #00F2FF, #8A2BE2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }

        /* Glassmorphism Cards */
        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            transition: transform 0.3s ease, border-color 0.3s ease;
        }
        
        .glass-card:hover {
            transform: translateY(-5px);
            border-color: rgba(0, 242, 255, 0.4);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        }

        /* Clickable Card Wrapper (Smooth Navigation) */
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
            height: 150px !important; /* Matches approximate card height */
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

        .stage-badge {
            background: rgba(0, 242, 255, 0.1);
            color: #00F2FF;
            padding: 0.25rem 0.75rem;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 600;
            border: 1px solid rgba(0, 242, 255, 0.2);
            margin-bottom: 1rem;
            display: inline-block;
        }

        .topic-category {
            color: #8A2BE2;
            font-weight: 600;
            margin-top: 1rem;
            margin-bottom: 0.5rem;
            font-size: 1.1rem;
        }

        .milestone-box {
            background: rgba(255, 215, 0, 0.05);
            border-left: 4px solid #FFD700;
            padding: 1rem;
            border-radius: 4px 12px 12px 4px;
            margin-top: 1.5rem;
        }

        /* Custom Progress Tracker */
        .roadmap-timeline {
            display: flex;
            justify-content: space-between;
            margin-bottom: 3rem;
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
            background: rgba(255, 255, 255, 0.1);
            z-index: 0;
        }

        .timeline-step {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: #1e293b;
            border: 2px solid rgba(255, 255, 255, 0.2);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 1;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .timeline-step.active {
            background: #00F2FF;
            color: #0E1117;
            border-color: #00F2FF;
            box-shadow: 0 0 15px rgba(0, 242, 255, 0.5);
        }

        /* Hide Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Resource Links */
        .resource-link {
            color: #A1A1AA;
            text-decoration: none;
            display: block;
            margin-bottom: 0.5rem;
            transition: color 0.2s;
        }
        
        .resource-link:hover {
            color: #00F2FF;
        }
        
        /* Trap Card */
        .trap-card {
            border-left: 4px solid #EF4444;
            background: rgba(239, 68, 68, 0.05);
        }
        </style>
    """, unsafe_allow_html=True)
