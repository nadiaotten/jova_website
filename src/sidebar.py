import streamlit as st

from src import utils
from src.i18n import get_lang, set_lang, LANGUAGES, t


def sidebar_app() -> None:
    with st.sidebar:
        # Language selector
        lang_options = list(LANGUAGES.keys())
        lang_labels = [LANGUAGES[code] for code in lang_options]
        current_idx = lang_options.index(get_lang())
        selected_lang = st.selectbox(
            t("language_label"),
            options=lang_options,
            format_func=lambda x: LANGUAGES[x],
            index=current_idx,
            key="lang_selector",
        )
        set_lang(selected_lang)

        st.markdown("---")
        danseurs = utils.show_image("danseurs.png")
        st.image(danseurs, use_container_width=True)
        left, center, right = st.columns([1, 2, 1])
        with center:
            jova_logo = utils.show_image("jova.png")
            st.image(jova_logo, width=160)
        st.markdown(
            f'<p style="text-align: center; font-size: 0.9rem; color: #5C4A3D !important;">{t("sidebar_caption")}</p>',
            unsafe_allow_html=True,
        )
        st.markdown("---")
