# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from __future__ import annotations

# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('.'))

from ext.monkey_patch_sphinx import monkey_patch

monkey_patch()


# -- Project information -----------------------------------------------------

project = 'evmos'
copyright = '2022, protodjango'
author = 'protodjango'

# The full version, including alpha/beta/rc tags
from evmos import __version__ as release

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # Built-in plugins
    'sphinx.ext.napoleon',  # Docstring preprocessing
    'sphinx.ext.autodoc',  # Docstring embedding into final documents
    'sphinx.ext.autosectionlabel',  # Use section header as anchor
    'sphinx.ext.autosummary',  # Auto summary generation
    'sphinx.ext.intersphinx',  # References
    'sphinx.ext.viewcode',  # Links to source
    # Custom
    'ext.monkey_patch_sphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Autodoc config ----------------------------------------------------------

autoclass_content = 'both'
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
    'ignore-module-all': False,
    'autosummary': True,
    'autosummary-members': True,
    'autosummary-undoc-members': True,
    # 'autosummary-nosignatures': True,
    'autosummary-ignore-module-all': False,
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'eth_typing': ('https://eth-typing.readthedocs.io/en/latest/', None),
    'betterproto': ('https://test-betterproto.readthedocs.io/en/docs/', None),
}
