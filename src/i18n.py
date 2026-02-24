"""Internationalization (i18n) - Multi-language support for JOVA website."""

import streamlit as st

# Language codes and display names with flags
LANGUAGES = {
    "fr": "🇫🇷 Français",
    "en": "🇬🇧 English",
    "nl": "🇳🇱 Nederlands",
    "de": "🇩🇪 Deutsch",
}

DEFAULT_LANG = "fr"

# All translations
TRANSLATIONS = {
    "fr": {
        # Menu
        "menu_home": "Accueil",
        "menu_products": "Nos Produits",
        "menu_awards": "Nos Récompenses",
        "menu_contact": "Contact",
        # Sidebar
        "sidebar_caption": "JOVA — Charcuterie de qualité",
        # Accueil
        "welcome_title": "Bienvenue sur le site JOVA",
        "welcome_p1": "Dans le métier depuis **4 générations**, c'est en 1988 que Jean Otten et son épouse créent la société « JOVA ».",
        "welcome_p2": "Spécialisée dans la fabrication de saucisses et saucissons cuits, fumés de première qualité, JOVA allie savoir-faire et qualité (certifié IFS) afin de vous offrir un produit sain !",
        "welcome_p3": "Préparés à base de viandes de porc et de bœuf de premier choix, nos deux spécialités ont remporté **19 médailles d'or** à différents concours internationaux.",
        "welcome_p4": "La saucisse cuite et fumée ainsi que le saucisson aux dés de jambon à 6 % de matière grasse peuvent être consommés chaud ou froid et vendus en libre service comme au rayon coupe.",
        "refs_label": "**Nos références :** grande distribution (Metro, Makro, Delhaize, Colruyt, Renmans, Cora, Intermarché…), ainsi que les plus grands grossistes de Belgique.",
        "badge_medals": "19 médailles d'or",
        "badge_medals_caption": "Concours internationaux",
        "badge_cert": "Certifié IFS",
        "badge_cert_caption": "Qualité garantie",
        "badge_gen": "4 générations",
        "badge_gen_caption": "Savoir-faire artisanal",
        # Produits
        "products_title": "🥓 Nos Produits",
        "products_presentations": "Présentations de nos produits",
        # Awards
        "awards_title": "🏆 Nos Récompenses",
        "awards_year": "Années",
        "awards_product": "Produits",
        "awards_medal": "Médailles/diplômes",
        "awards_title_col": "Intitulés",
        "awards_origin": "Origine",
        # Contact
        "contact_title": "📞 Contact",
        "contact_where": "📍 Où nous trouver",
        "contact_map_hint": "Cliquez sur la carte pour l'agrandir",
        "contact_how": "✉️ Nous contacter",
        "contact_email": "Par mail",
        "contact_phone": "Par téléphone",
        "contact_office": "Bureaux",
        "contact_english": "(English)",
        # Footer
        "footer_address": "JOVA SA — Rue de l'Abbaye 46, 4040 Herstal, Belgique",
        "footer_tagline": "4 générations de savoir-faire · 19 médailles d'or · Certifié IFS",
        "footer_copyright": "© JOVA — Charcuterie de qualité depuis 1988",
        "language_label": "Langue",
    },
    "en": {
        "menu_home": "Home",
        "menu_products": "Our Products",
        "menu_awards": "Our Awards",
        "menu_contact": "Contact",
        "sidebar_caption": "JOVA — Quality charcuterie",
        "welcome_title": "Welcome to JOVA website",
        "welcome_p1": "In the business for **4 generations**, it was in 1988 that Jean Otten and his wife created the company \"JOVA\".",
        "welcome_p2": "Specializing in the production of high-quality cooked and smoked sausages, JOVA combines expertise and quality (IFS certified) to offer you a healthy product!",
        "welcome_p3": "Prepared from top-quality pork and beef, our two specialties have won **19 gold medals** at various international competitions.",
        "welcome_p4": "The cooked and smoked sausage as well as the ham dice sausage with 6% fat content can be consumed hot or cold and sold in self-service as well as at the deli counter.",
        "refs_label": "**Our references:** large retailers (Metro, Makro, Delhaize, Colruyt, Renmans, Cora, Intermarché…), as well as the largest wholesalers in Belgium.",
        "badge_medals": "19 gold medals",
        "badge_medals_caption": "International competitions",
        "badge_cert": "IFS certified",
        "badge_cert_caption": "Guaranteed quality",
        "badge_gen": "4 generations",
        "badge_gen_caption": "Artisan know-how",
        "products_title": "🥓 Our Products",
        "products_presentations": "Our product presentations",
        "awards_title": "🏆 Our Awards",
        "awards_year": "Year",
        "awards_product": "Products",
        "awards_medal": "Medals/Diplomas",
        "awards_title_col": "Titles",
        "awards_origin": "Origin",
        "contact_title": "📞 Contact",
        "contact_where": "📍 Find us",
        "contact_map_hint": "Click on the map to enlarge",
        "contact_how": "✉️ Contact us",
        "contact_email": "By email",
        "contact_phone": "By phone",
        "contact_office": "Office",
        "contact_english": "(English)",
        "footer_address": "JOVA SA — Rue de l'Abbaye 46, 4040 Herstal, Belgium",
        "footer_tagline": "4 generations of know-how · 19 gold medals · IFS certified",
        "footer_copyright": "© JOVA — Quality charcuterie since 1988",
        "language_label": "Language",
    },
    "nl": {
        "menu_home": "Home",
        "menu_products": "Onze Producten",
        "menu_awards": "Onze Onderscheidingen",
        "menu_contact": "Contact",
        "sidebar_caption": "JOVA — Kwaliteitscharcuterie",
        "welcome_title": "Welkom op de Jova-website",
        "welcome_p1": "Al **vier generaties** in het vak, was het in 1988 dat Jean Otten en zijn vrouw het bedrijf \"JOVA\" oprichtten.",
        "welcome_p2": "Gespecialiseerd in de productie van hoogwaardige gekookte en gerookte worsten, combineert JOVA vakmanschap en kwaliteit (IFS-gecertificeerd) om u een gezond product te bieden!",
        "welcome_p3": "Bereid met varkens- en rundvlees van topkwaliteit, hebben onze twee specialiteiten **19 gouden medailles** gewonnen op verschillende internationale wedstrijden.",
        "welcome_p4": "De gekookte en gerookte worst evenals de hamblokjesworst met 6% vetgehalte kunnen zowel warm als koud worden geconsumeerd en zowel in zelfbediening als aan de toonbank worden verkocht.",
        "refs_label": "**Onze referenties:** grote retailers (Metro, Makro, Delhaize, Colruyt, Renmans, Cora, Intermarché…), evenals de grootste groothandels in België.",
        "badge_medals": "19 gouden medailles",
        "badge_medals_caption": "Internationale wedstrijden",
        "badge_cert": "IFS-gecertificeerd",
        "badge_cert_caption": "Gegarandeerde kwaliteit",
        "badge_gen": "4 generaties",
        "badge_gen_caption": "Ambachtelijk vakmanschap",
        "products_title": "🥓 Onze Producten",
        "products_presentations": "Onze productpresentaties",
        "awards_title": "🏆 Onze Onderscheidingen",
        "awards_year": "Jaar",
        "awards_product": "Producten",
        "awards_medal": "Medailles/Diploma's",
        "awards_title_col": "Titels",
        "awards_origin": "Herkomst",
        "contact_title": "📞 Contact",
        "contact_where": "📍 Waar ons te vinden",
        "contact_map_hint": "Klik op de kaart om te vergroten",
        "contact_how": "✉️ Neem contact op",
        "contact_email": "Per e-mail",
        "contact_phone": "Per telefoon",
        "contact_office": "Kantoor",
        "contact_english": "(English)",
        "footer_address": "JOVA SA — Rue de l'Abbaye 46, 4040 Herstal, België",
        "footer_tagline": "4 generaties vakmanschap · 19 gouden medailles · IFS-gecertificeerd",
        "footer_copyright": "© JOVA — Kwaliteitscharcuterie sinds 1988",
        "language_label": "Taal",
    },
    "de": {
        "menu_home": "Startseite",
        "menu_products": "Unsere Produkte",
        "menu_awards": "Unsere Auszeichnungen",
        "menu_contact": "Kontakt",
        "sidebar_caption": "JOVA — Qualitätswurstwaren",
        "welcome_title": "Herzlich willkommen auf der JOVA-Website",
        "welcome_p1": "Seit **vier Generationen** im Handel gründeten Jean Otten und seine Frau 1988 das Unternehmen JOVA.",
        "welcome_p2": "Spezialisiert auf die Herstellung von hochwertigen gekochten und geräucherten Würsten verbindet JOVA Know-how und Qualität (IFS-zertifiziert).",
        "welcome_p3": "Hergestellt aus erstklassigem Schweine- und Rindfleisch haben unsere zwei Spezialitäten **19 Goldmedaillen** bei verschiedenen internationalen Wettbewerben gewonnen.",
        "welcome_p4": "Die gekochte und geräucherte Wurst sowie die Schinkenwürfelwurst mit 6% Fett können warm oder kalt verzehrt und sowohl im Selbstbedienungsbereich als auch an der Theke verkauft werden.",
        "refs_label": "**Unsere Referenzen:** Großhändler (Metro, Makro, Delhaize, Colruyt, Renmans, Cora, Intermarché…) sowie die größten Großhändler in Belgien.",
        "badge_medals": "19 Goldmedaillen",
        "badge_medals_caption": "Internationale Wettbewerbe",
        "badge_cert": "IFS-zertifiziert",
        "badge_cert_caption": "Geprüfte Qualität",
        "badge_gen": "4 Generationen",
        "badge_gen_caption": "Handwerkliches Know-how",
        "products_title": "🥓 Unsere Produkte",
        "products_presentations": "Unsere Produktpräsentationen",
        "awards_title": "🏆 Unsere Auszeichnungen",
        "awards_year": "Jahr",
        "awards_product": "Produkte",
        "awards_medal": "Medaillen/Diplome",
        "awards_title_col": "Titel",
        "awards_origin": "Herkunft",
        "contact_title": "📞 Kontakt",
        "contact_where": "📍 Wo Sie uns finden",
        "contact_map_hint": "Klicken Sie auf die Karte zum Vergrößern",
        "contact_how": "✉️ Kontaktieren Sie uns",
        "contact_email": "Per E-Mail",
        "contact_phone": "Per Telefon",
        "contact_office": "Büro",
        "contact_english": "(English)",
        "footer_address": "JOVA SA — Rue de l'Abbaye 46, 4040 Herstal, Belgien",
        "footer_tagline": "4 Generationen Know-how · 19 Goldmedaillen · IFS-zertifiziert",
        "footer_copyright": "© JOVA — Qualitätswurstwaren seit 1988",
        "language_label": "Sprache",
    },
}

def get_lang() -> str:
    """Get current language from session state."""
    if "lang" not in st.session_state:
        st.session_state.lang = DEFAULT_LANG
    return st.session_state.lang


def set_lang(lang: str) -> None:
    """Set current language in session state."""
    if lang in LANGUAGES:
        st.session_state.lang = lang


def t(key: str) -> str:
    """Get translation for the given key in current language."""
    lang = get_lang()
    return TRANSLATIONS.get(lang, TRANSLATIONS[DEFAULT_LANG]).get(key, key)


# Menu internal keys for routing (language-independent)
MENU_KEYS = ["home", "products", "awards", "contact"]
# Map internal key to translation key for menu labels
MENU_LABEL_KEYS = {
    "home": "menu_home",
    "products": "menu_products",
    "awards": "menu_awards",
    "contact": "menu_contact",
}


def get_menu_items() -> list[tuple[str, str]]:
    """Get menu items with (translated_label, internal_key) for routing."""
    return [(t(MENU_LABEL_KEYS[key]), key) for key in MENU_KEYS]
