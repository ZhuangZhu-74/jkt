html_theme = 'sphinx_rtd_theme'

extensions = [
    "recommonmark", "sphinx_markdown_tables", "sphinx.ext.coverage",
    "sphinx.ext.autosummary", "sphinx_md", "sphinx.ext.napoleon",
    "sphinx.ext.githubpages", "autoapi.extension"
]
autoapi_dirs = ['./']
autoapi_keep_files = True
autoapi_add_toctree_entry = False
autosummary_generate = True
autoapi_options = ["members", "show-module-summary"]
autoapi_ignore = []

templates_path = ['_templates']
exclude_patterns = []

source_suffix = [".html"]