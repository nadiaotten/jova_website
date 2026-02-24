"""Main body content for JOVA website."""

import base64
from pathlib import Path

import streamlit as st
import urllib3
from streamlit_option_menu import option_menu

from src import utils
from src.components import render_footer
from src.config import PRODUCTS_MAIN
from src.i18n import t, get_menu_items
from src.styles import get_icon

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# --------------------------------------------------------------------
# LAYOUTS

def _layout_accueil() -> None:
    """Home page layout."""
    st.markdown(
        f'<h2 style="text-align: center; margin-top: 2.5rem; margin-bottom: 4rem;">{t("welcome_title")}</h2>',
        unsafe_allow_html=True,
    )
    st.markdown(t("welcome_p1"))
    st.markdown(t("welcome_p2"))
    st.markdown(t("welcome_p3"))
    st.markdown(t("welcome_p4"))

    st.markdown("---")
    st.markdown(t("refs_label"))

    # Highlight badges
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"### {get_icon('medal')} {t('badge_medals')}")
        st.caption(t("badge_medals_caption"))
    with c2:
        st.markdown(f"### {get_icon('certification')} {t('badge_cert')}")
        st.caption(t("badge_cert_caption"))
    with c3:
        st.markdown(f"### {get_icon('home')} {t('badge_gen')}")
        st.caption(t("badge_gen_caption"))

    # Extra spacing before footer on home page
    st.markdown('<div style="height: 5rem;"></div>', unsafe_allow_html=True)


def _layout_produits() -> None:
    """Products page layout."""
    st.markdown(
        f'<h2 style="text-align: center; margin-bottom: 4rem;">{t("products_title")}</h2>',
        unsafe_allow_html=True,
    )

    # Main products in cards
    for i in range(0, len(PRODUCTS_MAIN), 3):
        cols = st.columns(3)
        for col, (img_id, name) in zip(cols, PRODUCTS_MAIN[i : i + 3]):
            with col:
                utils.display_product(img_id, name)

    st.markdown("---")
    st.markdown(f"### {t('products_presentations')}")

    product_images = [f"plat{j}.jpg" for j in range(1, 11)]
    for i in range(0, len(product_images), 3):
        cols = st.columns(3)
        for col, img in zip(cols, product_images[i : i + 3]):
            with col:
                utils.load_image(img)


def _layout_recompenses() -> None:
    """Awards page layout."""
    st.markdown(
        f'<h2 style="text-align: center; margin-bottom: 4rem;">{t("awards_title")}</h2>',
        unsafe_allow_html=True,
    )

    recompenses_html = f"""
    <table id="customers" width="100%" cellpadding="10">
        <tr>
            <th>{t("awards_year")}</th>
            <th>{t("awards_product")}</th>
            <th>{t("awards_medal")}</th>
            <th>{t("awards_title_col")}</th>
            <th>{t("awards_origin")}</th>
        </tr>
        <tr><td>1987</td><td>Saucisse cuite & fumée</td><td>Médaille d'Or</td><td>Concours professionnels Euro Beef</td><td>Belgique, Bruxelles</td></tr>
        <tr><td>1988</td><td>Saucisse cuite & fumée</td><td>Diplôme d'Argent</td><td>Concours international de bouchers EurovleseM</td><td>Belgique, Anvers</td></tr>
        <tr><td>1988</td><td>Saucisse cuite & fumée</td><td>Diplôme d'Or</td><td>Concours international de bouchers EurovleseM</td><td>Belgique, Anvers</td></tr>
        <tr><td>1988</td><td>Saucisson aux dés de jambon 6% M.G.</td><td>Diplôme d'Or</td><td>Concours international de bouchers EurovleseM</td><td>Belgique, Anvers</td></tr>
        <tr><td>1992</td><td>Saucisse cuite & fumée</td><td>Médaille d'Argent</td><td>Interfair '92</td><td>Danmark</td></tr>
        <tr><td>1992</td><td>Saucisson aux dés de jambon 6% M.G.</td><td>Médaille d'Argent</td><td>Interfair '92</td><td>Danmark</td></tr>
        <tr><td>1992</td><td>Saucisse cuite & fumée</td><td>Médaille d'Or</td><td>Internationaler Fachwettbewerb Öfa Wels</td><td>Autriche</td></tr>
        <tr><td>1994</td><td>Saucisse cuite & fumée</td><td>Médaille d'Argent</td><td>Internationaler Fachwettbewerb Öfa Wels</td><td>Autriche</td></tr>
        <tr><td>1995</td><td>Saucisse cuite & fumée</td><td>Médaille d'Argent</td><td>Deutscher Fleischer-Verband</td><td>Allemagne, Frankfurt</td></tr>
        <tr><td>1998</td><td>Saucisson aux dés de jambon 6% M.G.</td><td>Diplôme d'Excellence « Saucicréor »</td><td>Confrérie des Chevaliers de la Grand'Table</td><td>France, Sologne</td></tr>
        <tr><td>1998</td><td>Saucisse cuite & fumée</td><td>Médaille d'Or « Saucicréor »</td><td>Confrérie des Chevaliers de la Grand'Table</td><td>France, Sologne</td></tr>
        <tr><td>2003</td><td>Saucisse cuite & fumée</td><td>Médaille d'Or</td><td>Confrérie des Chevaliers du Goûte-Andouille de Jargeau</td><td>Pays-Bas</td></tr>
        <tr><td>2003</td><td>Saucisson aux dés de jambon 6% M.G.</td><td>Médaille d'Or</td><td>Confrérie des Chevaliers du Goûte-Andouille de Jargeau</td><td>Pays-Bas</td></tr>
        <tr><td>2007</td><td>Saucisse cuite & fumée</td><td>Médaille d'Or</td><td>DLG-Prämierte Spitzenqualität</td><td>Allemagne, Frankfurt</td></tr>
        <tr><td>2007</td><td>Saucisson aux dés de jambon 6% M.G.</td><td>Médaille d'Or</td><td>DLG-Prämierte Spitzenqualität</td><td>Allemagne, Frankfurt</td></tr>
        <tr><td>2008</td><td>Saucisse cuite & fumée</td><td>Médaille d'Or</td><td>DLG-Prämierte Spitzenqualität</td><td>Allemagne, Frankfurt</td></tr>
        <tr><td>2008</td><td>Saucisson aux dés de jambon 6% M.G.</td><td>Médaille d'Or</td><td>DLG-Prämierte Spitzenqualität</td><td>Allemagne, Frankfurt</td></tr>
        <tr><td>2009</td><td>Saucisse cuite & fumée</td><td>Médaille d'Or</td><td>DLG-Prämierte Spitzenqualität</td><td>Allemagne, Frankfurt</td></tr>
        <tr><td>2009</td><td>Saucisson aux dés de jambon 6% M.G.</td><td>Médaille d'Argent</td><td>DLG-Prämierte Spitzenqualität</td><td>Allemagne, Frankfurt</td></tr>
        <tr><td>2010</td><td>Saucisse cuite & fumée</td><td>Une étoile</td><td>ITQI</td><td>Belgique, Bruxelles</td></tr>
        <tr><td>2010</td><td>Saucisse cuite & fumée</td><td>Médaille d'Or</td><td>Deutscher Fleischer-Verband</td><td>Allemagne, Frankfurt</td></tr>
        <tr><td>2010</td><td>Saucisson aux dés de jambon 6% M.G.</td><td>Médaille d'Or</td><td>Deutscher Fleischer-Verband</td><td>Allemagne, Frankfurt</td></tr>
        <tr><td>2010</td><td>Saucisse cuite & fumée</td><td>Médaille d'Or</td><td>DLG-Prämierte Spitzenqualität</td><td>Allemagne, Frankfurt</td></tr>
        <tr><td>2010</td><td>Saucisson aux dés de jambon 6% M.G.</td><td>Médaille d'Argent</td><td>DLG-Prämierte Spitzenqualität</td><td>Allemagne, Frankfurt</td></tr>
        <tr><td>2010</td><td>Nature</td><td>Médaille d'Argent</td><td>DLG-Prämierte Spitzenqualität</td><td>Allemagne, Frankfurt</td></tr>
        <tr><td>2012</td><td>Ficelle de jambon au piment d'Espelette</td><td>Une étoile</td><td>ITQI</td><td>Belgique, Bruxelles</td></tr>
    </table>
    """

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown(recompenses_html, unsafe_allow_html=True)
    with col2:
        or_image = utils.show_image("OR.jpg")
        st.image(or_image, width=280)


def _layout_contact() -> None:
    """Contact page layout."""
    st.markdown(
        f'<h2 style="text-align: center; margin-bottom: 4rem;">{t("contact_title")}</h2>',
        unsafe_allow_html=True,
    )

    # Address and map section
    st.markdown(f"### {t('contact_where')}")
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown(
            f"""
            <div style="background: white; padding: 1.5rem 2rem; border-radius: 12px; border-left: 4px solid #8B2942; box-shadow: 0 2px 12px rgba(44,24,16,0.06);">
                <p style="margin: 0; font-size: 1.1rem;"><strong>JOVA SA</strong></p>
                <p style="margin: 0.5rem 0 0 0;">Rue de l'Abbaye, 46</p>
                <p style="margin: 0.25rem 0 0 0;">4040 Herstal</p>
                <p style="margin: 0.25rem 0 0 0;">Belgique</p>
                <p style="margin: 1rem 0 0 0; font-size: 0.85rem; color: #6c757d;"><em>{t("contact_map_hint")}</em></p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        map_path = utils.get_image_path("carte.jpg")
        if map_path.exists():
            with open(map_path, "rb") as f:
                encoded = base64.b64encode(f.read()).decode()
            mime = "image/jpeg" if map_path.suffix.lower() in (".jpg", ".jpeg") else "image/png"
            link = "https://www.google.be/maps/place/Rue+de+l'Abbaye+46,+4040+Herstal"
            st.markdown(
                f'<a href="{link}" target="_blank"><img src="data:{mime};base64,{encoded}" width="650" style="border-radius:12px; box-shadow: 0 2px 12px rgba(44,24,16,0.08);"></a>',
                unsafe_allow_html=True,
            )

    st.markdown("")
    st.markdown("---")
    st.markdown(f"### {t('contact_how')}")

    # Contact info in a clean card layout
    col_contact1, col_contact2 = st.columns(2)

    with col_contact1:
        st.markdown(
            f"""
            <div style="background: white; padding: 1.5rem 2rem; border-radius: 12px; box-shadow: 0 2px 12px rgba(44,24,16,0.06); margin-bottom: 1rem;">
                <p style="margin: 0 0 1rem 0; font-weight: 600;">✉️ {t("contact_email")}</p>
                <p style="margin: 0;"><a href="mailto:info@jova.be" style="color: #8B2942; font-size: 1.1rem;">info@jova.be</a></p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_contact2:
        st.markdown(
            f"""
            <div style="background: white; padding: 1.5rem 2rem; border-radius: 12px; box-shadow: 0 2px 12px rgba(44,24,16,0.06); margin-bottom: 1rem;">
                <p style="margin: 0 0 1rem 0; font-weight: 600;">📱 {t("contact_phone")}</p>
                <p style="margin: 0.25rem 0;"><strong>{t("contact_office")}</strong><br><a href="tel:+3242646818">+32 (0)4 264 68 18</a></p>
                <p style="margin: 0.5rem 0 0.25rem 0;"><strong>Ewa Otten</strong><br><a href="tel:+32498153434">+32 (0)498 15 34 34</a></p>
                <p style="margin: 0.25rem 0;"><strong>Jean Otten</strong><br><a href="tel:+32496722172">+32 (0)496 72 21 72</a></p>
                <p style="margin: 0.25rem 0;"><strong>Dimitri Otten</strong> <em style="font-size: 0.85rem;">{t("contact_english")}</em><br><a href="tel:+32478266260">+32 (0)478 26 62 60</a></p>
            </div>
            """,
            unsafe_allow_html=True,
        )


# --------------------------------------------------------------------
# MAIN

def body_app() -> None:
    """Main body application."""
    menu_items = get_menu_items()
    menu_labels = [label for label, _ in menu_items]
    menu_icons = ["house", "basket", "trophy", "telephone"]

    # Sidebar menu
    with st.sidebar:
        selected_label = option_menu(
            "Menu",
            menu_labels,
            icons=menu_icons,
            default_index=0,
            menu_icon="list",
        )
        selected_key = next(k for lbl, k in menu_items if lbl == selected_label)
        st.session_state.conversion_menu = selected_label

    # Route to layout
    layouts = {
        "home": _layout_accueil,
        "products": _layout_produits,
        "awards": _layout_recompenses,
        "contact": _layout_contact,
    }
    layouts.get(selected_key, _layout_accueil)()

    render_footer()
