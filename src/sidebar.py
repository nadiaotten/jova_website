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

        danseurs = utils.show_image("danseurs.png")
        st.image(danseurs, width='stretch')
        left, center, right = st.columns([1, 2, 1])
        with center:
            jova_logo = utils.show_image("jova.png")
            st.image(jova_logo, width=60)


