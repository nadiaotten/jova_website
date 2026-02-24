"""Configuration and constants for JOVA website."""

from pathlib import Path

# Paths
ASSETS_DIR = Path(__file__).parent.parent / "assets"

# Menu configuration with icons (Bootstrap Icons)
MENU_ITEMS = [
    ("Accueil", "house"),
    ("Nos Produits", "basket"),
    ("Nos Récompenses", "trophy"),
    ("Contact", "telephone"),
]

# Product catalog
PRODUCTS_MAIN = [
    ("kielbasa.jpg", "Kielbasa"),
    ("krako.jpg", "Krakowka"),
    ("kabanoz.jpg", "Kabanozy"),
    ("parowki.jpg", "Parowki"),
    ("choucroutin.jpg", "Choucroutin"),
    ("breakfast.jpg", "Saucisses Breakfast"),
]

# Image path resolution (handle case variations)
IMAGE_ALIASES = {
    "jova.png": ["jova.PNG", "jova.png"],
    "carte.jpg": ["carte.JPG", "carte.jpg"],
}
