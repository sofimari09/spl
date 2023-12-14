# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
"""
Module for source/conf.py.
It is used to configure Sphinx documentation builder.
"""
import os
import sys

sys.path.insert(0, os.path.abspath('../../src'))

project = 'spl'
copyright = '2023, Sofia'
author = 'Sofia'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


def skip_module(app, what, name, obj, skip, options):
    if name == 'colorama':
        return True
    return None


def setup(app):
    app.connect("autodoc-skip-member", skip_module)


autodoc_mock_imports = ["colorama", "prettytable", "regex", "matplotlib", "pyfiglet",
                        "pandas", "dateutil"]
