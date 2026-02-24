"""Custom CSS and styling for JOVA website."""

# Warm, artisanal color palette - premium food brand
PRIMARY = "#8B2942"      # Burgundy/wine
SECONDARY = "#C4A35A"    # Gold/amber
ACCENT = "#2C1810"       # Dark brown
BG_LIGHT = "#FDF8F3"     # Cream
BG_CARD = "#FFFFFF"
TEXT_DARK = "#2C1810"
TEXT_MUTED = "#5C4A3D"
BORDER = "#E8DDD4"


def inject_custom_css() -> None:
    """Inject custom CSS for JOVA branding."""
    st_css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=Source+Sans+3:wght@400;500;600&display=swap');
    
    :root {
        --jova-primary: #8B2942;
        --jova-gold: #C4A35A;
        --jova-brown: #2C1810;
        --jova-cream: #FDF8F3;
    }
    
    /* Main app styling */
    .stApp {
        background: linear-gradient(180deg, #FDF8F3 0%, #FAF5EF 50%, #F5EDE4 100%);
    }
    
    /* Header / title area */
    .jova-hero {
        background: linear-gradient(135deg, #8B2942 0%, #6B1E32 100%);
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(139, 41, 66, 0.2);
    }
    
    .jova-hero h1 {
        color: white !important;
        font-family: 'Cormorant Garamond', serif !important;
        font-weight: 700 !important;
        font-size: 2.5rem !important;
    }
    
    .jova-hero p {
        color: rgba(255,255,255,0.9) !important;
        font-size: 1.1rem !important;
    }
    
    /* Section styling */
    .stSubheader, .stHeader {
        font-family: 'Cormorant Garamond', serif !important;
        color: #2C1810 !important;
        border-bottom: 2px solid #C4A35A;
        padding-bottom: 0.5rem !important;
    }
    
    /* Product cards */
    .product-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 2px 12px rgba(44, 24, 16, 0.08);
        transition: transform 0.2s, box-shadow 0.2s;
        border: 1px solid #E8DDD4;
    }
    
    .product-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 24px rgba(139, 41, 66, 0.12);
    }
    
    /* Contact info styling */
    .contact-box {
        background: white;
        border-radius: 12px;
        padding: 1.5rem 2rem;
        border-left: 4px solid #8B2942;
        box-shadow: 0 2px 12px rgba(44, 24, 16, 0.06);
    }
    
    /* Rewards table */
    #customers {
        font-family: 'Source Sans 3', sans-serif !important;
        border-collapse: collapse;
        width: 100%;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 12px rgba(44, 24, 16, 0.08);
    }
    
    #customers th {
        background: #8B2942 !important;
        color: white !important;
        padding: 12px 16px !important;
        text-align: left;
        font-weight: 600;
    }
    
    #customers td {
        padding: 10px 16px !important;
        border-bottom: 1px solid #E8DDD4;
    }
    
    #customers tr:nth-child(even) {
        background: #FAF7F2 !important;
    }
    
    #customers tr:hover {
        background: #F5EDE4 !important;
    }
    
    /* Footer */
    .jova-footer {
        margin-top: 4rem;
        padding: 2rem;
        background: linear-gradient(135deg, #E8E4E0 0%, #D8D4D0 100%);
        border-radius: 12px;
        color: #2C1810;
        text-align: center;
        font-size: 0.9rem;
    }
    
    .jova-footer a {
        color: #8B2942 !important;
    }
    
    /* Icon badges */
    .icon-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: rgba(139, 41, 66, 0.1);
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.25rem;
        font-weight: 500;
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Remove header and reduce top padding for more content space */
    [data-testid="stHeader"] {display: none !important;}
    div[data-testid="stVerticalBlock"] > div:first-child {padding-top: 0.5rem !important;}
    .block-container {padding-top: 1rem !important; border-top: none !important; box-shadow: none !important;}
    
    /* Remove top line/border */
    [data-testid="stHeader"] {border: none !important; box-shadow: none !important;}
    .stApp > header {border: none !important;}
    div[data-testid="stAppViewContainer"] {border-top: none !important;}
    div[data-testid="stAppViewContainer"] > div {border-top: none !important; box-shadow: none !important;}
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #E8E4E0 0%, #D8D4D0 100%) !important;
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: #2C1810 !important;
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
