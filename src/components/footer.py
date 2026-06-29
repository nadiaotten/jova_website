"""Footer component for JOVA website."""

import streamlit as st

from src.i18n import t


def render_footer() -> None:
    """Render the site footer."""
    
    st.write("")
    st.write("")

    st.markdown(
        f"""
        <div class="jova-footer">
            <p>📍 {t("footer_tagline")}</p>
            <p>
                <a href="mailto:info@jova.be">info@jova.be</a> · 
                <a href="tel:+3242646818">+32 (0)4 264 68 18</a>
            </p>
            <p style="opacity: 0.8; margin-top: 0.5rem; font-size: 0.75rem;">
                {t("footer_copyright")}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
