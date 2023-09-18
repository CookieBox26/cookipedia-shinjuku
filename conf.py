# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Cookipedia.Shinjuku'
copyright = '2023, Chihiro Mihara'
author = 'Chihiro Mihara'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_css_files = ['custom.css']
html_static_path = ['_static']

# html_search_language = 'ja'
# html_search_options = {
#     'type': 'sphinx.search.ja.MecabSplitter',
#     'dic_enc': 'utf-8',
#     'dict': '"C:\\Program Files\\MeCab\\dic\\ipadic"',
# }
