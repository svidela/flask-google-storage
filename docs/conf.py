# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from collections import OrderedDict

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

import flask_googlestorage

project = "Flask-GoogleStorage"
copyright = "2020, Santiago Videla"
author = "Santiago Videla"
version = release = flask_googlestorage.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx_issues",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "flask": ("http://flask.pocoo.org/docs/", None),
    "google-cloud-storage": ("https://googleapis.dev/python/storage/latest/index.html", None),
}
issues_github_path = "svidela/flask-googlestorage"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

html_theme_options = {
    "description": "Google Cloud Storage for Flask",
    "description_font_style": "italic",
    "github_user": "svidela",
    "github_repo": "flask-googlestorage",
    "github_button": False,
    "github_banner": True,
    "codecov_button": True,
    "sidebar_width": "240px",
    "code_font_size": "0.8em",
    "extra_nav_links": OrderedDict(
        [
            ("flask-googlestorage@PyPI", "http://pypi.python.org/pypi/flask-googlestorage"),
            ("flask-googlestorage@GitHub", "http://github.com/svidela/flask-googlestorage"),
        ]
    ),
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
