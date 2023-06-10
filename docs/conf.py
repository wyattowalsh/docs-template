# -- Imports ----------------------------------------------------------------
import os
import sys
from datetime import datetime

# -- Paths ------------------------------------------------------------------
sys.path.insert(0, os.path.abspath("../../"))

# -- Constants --------------------------------------------------------------
current_year = str(datetime.now().year)

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "docs"
copyright = f"{current_year}, Wyatt Walsh <wyattowalsh@gmail.com>"
author = "Wyatt Walsh <wyattowalsh@gmail.com>"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.graphviz",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_git",
    "sphinx_markdown_builder",
    "sphinx_copybutton",
    "sphinx_design",
    "myst_parser",
    "sphinxcontrib.mermaid",
    "hoverxref.extension",
    "sphinx_sitemap",
    "sphinx_togglebutton",
    "sphinx_favicon",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_baseurl = "localhost:7777"
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_logo = "_static/img/logo.webp"
html_favicon = "_static/img/favicon/favicon.ico"
html_sidebars = {"**": ["sidebar-nav-bs"]}
html_theme_options = {
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links"],
    "navbar_persistent": ["search-button", "theme-switcher"],
    "primary_sidebar_end": ["navbar-logo"],
    "secondary_sidebar_items": ["page-toc"],
    "footer_start": ["copyright", "sphinx-version"],
    "show_toc_level": 2,
    "show_nav_level": 3,
    "navigation_depth": 4,
    "header_links_before_dropdown": 5,
    "icon_links": [
        {
            # Label for this link
            "name": "GitHub",
            # URL where the link will redirect
            "url": "https://github.com/wyattowalsh/docs",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "_static/img/icons/github.svg",
            # The type of image to be used (see below for details)
            "type": "local",
            "attributes": {
                "target": "_blank",
                "rel": "noopener me",
                "class": "nav-link gh-icon",
            },
        },
    ],
    "icon_links_label": "Quick Links",
    "use_edit_page_button": True,
    "search_bar_text": "Search site here...",
    "navigation_with_keys": True,
    "navbar_align": "left",
}
html_css_files = [
    "css/custom.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300;1,400;1,500;1,600;1,800&family=Ubuntu+Mono:ital,wght@0,400;0,700;1,400;1,700&display=swap",
]
html_js_files = [
    "https://kit.fontawesome.com/ebaeac9722.js",
    "https://unpkg.com/@mui/material@latest/umd/material-ui.production.min.js",
]

# sphinx-panels shouldn't add bootstrap css since the pydata-sphinx-theme
# already loads it
panels_add_bootstrap_css = False
sd_fontawesome_latex = True

# -- Internationalization ------------------------------------------------
# specifying the natural language populates some key tags
language = "en"
autosummary_generate = True

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True
numpydoc_show_class_members = False

# Sphinx Copybutton settings
copybutton_copy_empty_lines = True
# copybutton_exclude = ['.linenos']

# Myst settings
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_heading_anchors = 3
myst_dmath_allow_labels = True
myst_dmath_double_inline = True

hoverxref_auto_ref = True

sitemap_filename = "sitemap.xml"

favicons = [
    "img/favicon/apple-touch-icon.png",
    "img/favicon/favicon-32x32.png",
    "img/favicon/favicon-16x16.png",
    "img/favicon/favicon.ico",
    "img/favicon/android-chrome-192x192.png",
    "img/favicon/android-chrome-512x512.png",
    "img/favicon/site.webmanifest",
]

autodoc_member_order = "bysource"
