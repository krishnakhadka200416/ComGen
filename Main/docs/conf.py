#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# SDV documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  9 13:47:02 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.

import sdv

# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'm2r2',
    'nbsphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.githubpages',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'sphinx_toolbox.collapse'
]

ipython_execlines = [
    "from utils import is_valid, transform, reverse_transform",
    "import pandas as pd",
    "pd.set_option('display.width', 1000000)",
    "pd.set_option('display.max_columns', 1000)",
]

autosummary_generate = True
autodoc_typehints = "none"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['sdv_theme/_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# Jupyter Notebooks
nbsphinx_execute = 'never'
nbsphinx_prolog = """
.. raw:: html

    <style>
        .nbinput .prompt,
        .nboutput .prompt {
            display: none;
        }
    </style>
"""

# General information about the project.
project = 'SDV'
slug = 'sdv'
title = project + ' Documentation',
copyright = '2022, DataCebo, Inc.'
author = 'DataCebo, Inc.'
description = 'Synthetic Data Generation for tabular, relational and time series data.'
user = 'sdv-dev'

# New docs for V1.0 Beta announcement
rst_prolog = """
    .. admonition:: Try the new SDV 1.0 Beta!

        We are transitioning to a new version of SDV with improved workflows, new features
        and an updated documentation site.

        `Click here to go to the new docs pages. <https://docs.sdv.dev/sdv/>`_
"""

# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
version = sdv.__version__
# The full version, including alpha/beta/rc tags.
release = sdv.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['.py', '_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sdv_theme'
html_theme_path = ['.']

# Readthedocs additions
html_context = {
    'display_github': True,
    'github_user': user,
    'github_repo': project,
    'github_version': 'main',
    'conf_py_path': '/docs/',
}

# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {
#     'collapse_navigation': True,
#     'display_version': True,
# }
html_theme_options = {
    "github_url": "https://github.com/sdv-dev/SDV",
    "twitter_url": "https://twitter.com/sdv_dev",
    "slack_url": "https://bit.ly/sdv-slack-invite",
    "show_prev_next": True,
    "google_analytics_id": "UA-180602145-3",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [
    'sdv_theme/static',
    'images',
]
html_css_files = [
    'sdv.css',
]

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'images/SDV.ico'

# If given, this must be the name of an image file (path relative to the
# configuration directory) that is the logo of the docs. It is placed at
# the top of the sidebar; its width should therefore not exceed 200 pixels.
html_logo = 'images/SDV.png'

# -- Options for HTMLHelp output ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = slug + 'doc'


# -- Options for LaTeX output ------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [(
    master_doc,
    slug + '.tex',
    title,
    author,
    'manual'
)]


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(
    master_doc,
    slug,
    title,
    [author],
    1
)]


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [(
    master_doc,
    slug,
    title,
    author,
    slug,
    description,
    'Miscellaneous'
)]
