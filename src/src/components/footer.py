"""Footer component for JOVA website."""

import streamlit as st

from src.i18n import t


def render_footer() -> None:
    """Render the site footer."""
    st.markdown("---")
    st.markdown(
        f"""
        <div class="jova-footer">
            <p><strong>{t("footer_address")}</strong></p>
            <p>📍 {t("footer_tagline")}</p>
            <p>
                <a href="mailto:info@jova.be">info@jova.be</a> · 
                <a href="tel:+3242646818">+32 (0)4 264 68 18</a>
            </p>
            <p style="opacity: 0.8; margin-top: 1rem; font-size: 0.85rem;">
                {t("footer_copyright")}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
