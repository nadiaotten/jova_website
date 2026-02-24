from io import BytesIO
from pathlib import Path

import pandas as pd
import streamlit as st
from PIL import Image

from src import exceptions
from src.config import ASSETS_DIR


def _resolve_image_path(img_id: str) -> Path:
    """Resolve image path, handling case variations."""
    path = ASSETS_DIR / img_id
    if path.exists():
        return path
    for f in ASSETS_DIR.iterdir():
        if f.name.lower() == img_id.lower():
            return f
    return path  # Return original, let it raise


def get_image_path(img_id: str) -> Path:
    """Return resolved path for an asset image."""
    return _resolve_image_path(img_id)


@st.cache_resource
def show_image(img_id: str):
    path = _resolve_image_path(img_id)
    return Image.open(path)

@st.cache_resource
def load_image(img_id):
    image = show_image(img_id)
    st.image(image, width=300, use_container_width="auto")

@st.cache_resource
def display_product(img_id, name):
    image = show_image(img_id)
    st.write(f"**{name}**")
    st.image(image, width=300, use_container_width="auto")


@st.cache_resource
def load_metadata(md_file):
    with open(f"assets/{md_file}", "r") as f:
        meta_data_content = f.read()
    return meta_data_content


def get_image(
    file: str,
    dir: Path = Path("assets"),
) -> Image:
    try:
        return st.session_state[file]
    except KeyError:
        path = dir.joinpath(file)
        try:
            st.session_state[file] = Image.open(path)
            return get_image(file)
        except FileNotFoundError as e:
            raise exceptions.AssetNotFound(f"Image not found at {path}") from e


def get_markdown(
    file: str,
    dir: Path = Path("assets"),
) -> Image:
    try:
        return st.session_state[file]
    except KeyError:
        path = dir.joinpath(file)
        try:
            with open(path, "r") as f:
                st.session_state[file] = f.read()
            return get_markdown(file)
        except FileNotFoundError as e:
            raise exceptions.AssetNotFound(f"Markdown not found at {path}") from e

