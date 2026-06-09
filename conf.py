# Configuration file for the Sphinx documentation builder.

project = 'fbchat-muqit'
copyright = '2025, Muhammad MuQiT'
author = 'Muhammad MuQiT'
release = "1.2.2"
version = release

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
]

# Napoleon settings
napoleon_google_docstring = True 
napoleon_include_init_with_doc = True
napoleon_use_param = True
napoleon_use_rtype = True

templates_path = ['_templates']
exclude_patterns = []  # This only affects .rst files, not Python modules

# -- Options for HTML output -------------------------------------------------

html_theme = 'furo'
html_static_path = ['_static']
html_show_sphinx = False
html_show_sourcelink = False

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]


html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "blue",
        "color-brand-content": "#CC3333",
    },
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/togashigreat/fbchat-muqit",
            "html": "",
            "class": "fa-brands fa-solid fa-github fa-2x",
        },
    ],
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
}


