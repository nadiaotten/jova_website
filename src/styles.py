"""Custom CSS and styling for JOVA website."""

# Warm, artisanal color palette - premium food brand
PRIMARY = "#8B2942"      # Burgundy/wine
SECONDARY = "#C4A35A"    # Gold/amber
ACCENT = "#2C1810"       # Dark brown
BG_LIGHT = "#FDF8F3"     # Cream
BG_CARD = "#FFFFFF"
TEXT_MUTED = "#5C4A3D"
BORDER = "#E8DDD4"

# Option menu styles
OPTION_MENU_STYLES = {
    "container": {
        "padding": "0!important",
        "background-color": "#FFFFFF",
    },
    "menu-title": {
        "color": "#AA9E96",
        "font-size": "20px",
        "font-weight": "600",
    },
    "icon": {
        "color": "#AA9E96",
        "font-size": "18px",
    },
    "nav-link": {
        "font-size": "16px",
        "text-align": "left",
        "margin": "0px",
        "color": "#AA9E96",
        "--hover-color": "#F5F1EE",
    },
    "nav-link-selected": {
        "background-color": "#AA9E96",
        "color": "white",
    },
}


def inject_custom_css() -> None:
    """Inject custom CSS for JOVA branding."""
    st_css = """
    <style>

    /* Force light mode */
    .stApp, [data-testid="stAppViewContainer"] {
        color-scheme: light !important;
        background: linear-gradient(180deg, #FDF8F3 0%, #FAF5EF 50%, #F5EDE4 100%) !important;
        color: #2C1810 !important;
    }
    
    .stCaption, [data-testid="stCaptionContainer"] {
        color: #5C4A3D !important;
    }

    
    #customers th {
        background: #8B2942 !important;
        color: white !important;
        padding: 12px 16px !important;
        text-align: left;
        font-weight: 600;
    }

    
    /* Footer */
    .jova-footer {
        margin-top: 1rem;
        padding: 1.5rem;
        background: linear-gradient(135deg, #E8E4E0 0%, #D8D4D0 100%);
        border-radius: 8px;
        color: #2C1810 !important;
        text-align: center;
        font-size: 1rem;
    }
    
    
    
    /* Make header transparent but keep sidebar toggle button visible */
    [data-testid="stHeader"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }
    # .stApp > header {border: none !important;}
    
    
    /* Reduce top padding */
    div[data-testid="stVerticalBlock"] > div:first-child {padding-top: 0.5rem !important;}
    .block-container {padding-top: 1rem !important; border-top: none !important; box-shadow: none !important;}
    div[data-testid="stAppViewContainer"] {border-top: none !important;}
    div[data-testid="stAppViewContainer"] > div {border-top: none !important; box-shadow: none !important;}
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #E8E4E0 0%, #D8D4D0 100%) !important;
    }

        /* Selectbox styling */
    div[data-baseweb="select"] > div {
        background-color: white !important;
        color: #AA9E96 !important;
        border-radius: 8px;
    }

    /* Home page text sizing */
    .stMarkdown h2 {
        font-size: 1.5rem !important;
    }

    .stMarkdown h3 {
        font-size: 1.1rem !important;
    }

    .stMarkdown p {
        font-size: 0.95rem !important;
    }

    /* Reduce text sizes in all layouts */
    .stMarkdown {
        font-size: 0.9rem !important;
    }

    #customers {
        font-size: 0.85rem !important;
    }

    #customers th, #customers td {
        padding: 8px 12px !important;
        font-size: 0.85rem !important;
    }

    </style>
    """


    import streamlit as st
    st.markdown(st_css, unsafe_allow_html=True)


def get_icon(icon_name: str) -> str:
    """Return emoji icon for consistent use."""
    icons = {
        "home": "🏠",
        "products": "🥓",
        "award": "🏆",
        "contact": "📞",
        "email": "✉️",
        "phone": "📱",
        "map": "📍",
        "certification": "✅",
        "medal": "🥇",
    }
    return icons.get(icon_name, "•")
