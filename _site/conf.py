# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import datetime

import sys
import os

sys.path.append(os.path.abspath('sphinxext'))


# -- Project information -----------------------------------------------------

project = "Geir Villy Isaksen's cheats sheets"
copyright = f'{datetime.datetime.now().year}, Geir Villy Isaksen'
author = 'Geir Villy Isaksen'

# Logo setup
#html_favicon = '...'
#html_logo = 'artsy/cheats_sheets_logo_white_200px.png'

html_title = "Geir Villy Isaksen's cheats sheets"
html_short_title = 'GVI cheats'
html_show_sourcelink = False
html_permalinks_icon = '<span>#</span>'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
import markdown

#md = markdown.Markdown(extensions=['pymdownx.emoji'])

extensions = ['myst_parser',
              'sphinx.ext.githubpages',
              'sphinxemoji.sphinxemoji']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    #"linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]


# Add any paths that contain templates here, relative to this directory.
templates_path = []

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv', '_book', 'README.md']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'groundwork'
#html_theme = 'alabaster'
#html_theme = 'sphinx_rtd_theme'
html_theme = 'sphinxawesome_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# Output file base name for HTML help builder.
htmlhelp_basename = 'SphinxwithMarkdowndoc'

# this configures where "view page source" (top right on rendered page) points to
html_context = {
    'display_github': True,
     'html_show_sourcelink':  False,
    'github_user': 'isaksengeir',
    'github_repo': 'isaksengeir@github.io',
    'github_version': 'master/'
}




