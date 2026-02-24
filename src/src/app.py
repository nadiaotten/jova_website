import streamlit as st

from src.body import body_app
from src.sidebar import sidebar_app
from src.styles import inject_custom_css


def app() -> None:
    st.set_page_config(
        page_title="JOVA — Charcuterie de qualité depuis 1988",
        page_icon="🥓",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    inject_custom_css()
    sidebar_app()
    body_app()
