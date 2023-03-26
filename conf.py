# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'L4'
copyright = '2023, Meng Weng Wong'
author = 'Meng Weng Wong, edited and organised by Nemo'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys
sys.path.insert(0, os.path.abspath(".."))

extensions = [
    'sphinx_design' ,
    'sphinxawesome_theme',
    'sphinxcontrib.inkscapeconverter'
    'sphinx.ext.autosectionlabel'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv', 'sphinxawesome_theme']

latex_elements = {
        'extrapackages': r'\usepackage{pmboxdraw}',
        # Enable these for ipad pdf
        #'sphinxsetup': 'hmargin=0.1in,vmargin=0.1in',
        #'papersize': 'a5paper',
        #'pointsize': '12pt',
}
latex_engine = "xelatex"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinxawesome_theme'
html_theme_path = ['sphinxawesome_theme/theme.conf']
html_static_path = ['_static']
html_collapsible_definitions = True
