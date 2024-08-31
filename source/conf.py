import os
import sys
sys.path.insert(0, os.path.abspath('_ext'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Descendants of Johannes and Magdalena Herr Glick'
copyright = '1982, Sarah M. Glick, Gladys Glick Guthrie'
author = 'Sarah M. Glick, Gladys Glick Guthrie'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.linkcode',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

extensions.append('edit_on_github')

edit_on_github_project = 'yourusername/yourrepo'
edit_on_github_branch = 'main'

def linkcode_resolve(domain, info):
    if domain != 'py':
        return None
    if not info['module']:
        return None
    filename = info['module'].replace('.', '/')
    return f"https://github.com/Johannes-Glick/descendants/blob/main/{filename}.py"

