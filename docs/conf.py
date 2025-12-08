import datetime
import os
import sys
import yaml
from docutils import nodes
from sphinx.util.docutils import SphinxRole
from docutils.parsers.rst import roles

# Configuration for the Sphinx documentation builder.
# All configuration specific to your project should be done in this file.

############################################################
# Project information
############################################################

# Product name
project = "Ubuntu Desktop as a Developer Platform"
author = "Canonical Ltd."

# The title you want to display for the documentation in the sidebar.
html_title = "Ubuntu for Developers"

# Copyright
copyright = "%s CC-BY-SA, %s" % (datetime.date.today().year, author)

# Open Graph configuration
ogp_site_url = "https://documentation.ubuntu.com/ubuntu-for-developers/"
ogp_site_name = project
ogp_image = "https://assets.ubuntu.com/v1/253da317-image-document-ubuntudocs.svg"

# html_favicon = '.sphinx/_static/favicon.png'

html_context = {
    "product_page": "ubuntu.com/desktop/developers",
    # 'product_tag': '_static/tag.png',
    "discourse": "https://discourse.ubuntu.com/c/foundations/",
    "mattermost": "",
    "matrix": "https://matrix.to/#/#documentation:ubuntu.com",
    "github_url": "https://github.com/canonical/ubuntu-for-developers-docs",
    "repo_folder": "/docs/",
    "github_issues": "enabled",
    "sequential_nav": "both",
    "display_contributors": True,
    'repo_default_branch': 'main',
}

html_theme_options = {
    "source_edit_link": html_context["github_url"],
}

slug = "ubuntu-for-developers"

#######################
# Template and asset locations
#######################

html_static_path = [".sphinx/_static"]
templates_path = [".sphinx/_templates"]

############################################################
# Redirects
############################################################

redirects = {}

############################################################
# Link checker exceptions
############################################################

linkcheck_ignore = [
    "http://127.0.0.1:8000",
    "https://crates.io",
    r"https://www\.nongnu\.org/.*",
    r"https://www\.gnu\.org/.*",
    r"https://matrix\.to/.*",
    "https://blog.local-optimum.net/getting-started-with-autoinstall-on-ubuntu-desktop-24-04-lts-147a1defb2de",
    "https://github.com/canonical/ACME/*"
]

linkcheck_anchors_ignore_for_url = [r"https://github\.com/.*"]

linkcheck_retries = 3

############################################################
# Additions to default configuration
############################################################

myst_enable_extensions = {"colon_fence"}

extensions = [
    "canonical_sphinx",
    "notfound.extension",
    "sphinx_design",
    "sphinx_reredirects",
    "sphinx_tabs.tabs",
    "sphinxcontrib.jquery",
    "sphinxext.opengraph",
    "sphinx_config_options",
    "sphinx_contributor_listing",
    "sphinx_filtered_toctree",
    "sphinx_related_links",
    "sphinx_roles",
    "sphinx_terminal",
    "sphinx_ubuntu_images",
    "sphinx_youtube_links",
    "sphinxcontrib.cairosvgconverter",
    "sphinx_last_updated_by_git",
    "sphinx.ext.intersphinx",
    "sphinx_sitemap",
    # Custom extensions
    "sphinxcontrib.mermaid",
    "sphinx_prompt",
    "sphinx.ext.extlinks",
]

myst_fence_as_directive = ["mermaid"]

exclude_patterns = [
    "reuse",
    "doc-cheat-sheet*",
]

html_css_files = ["custom_header.css", "cookie_banner.css"]
html_js_files = ["js/bundle.js"]

manpages_url = (
    "https://manpages.ubuntu.com/manpages/plucky/en/man{section}/{page}.{section}.html"
)

############################################################
# Additional configuration
############################################################

rst_prolog = """
.. role:: center
   :class: align-center
.. role:: h2
    :class: hclass2
.. role:: woke-ignore
    :class: woke-ignore
.. role:: vale-ignore
    :class: vale-ignore
"""

rst_epilog = """
.. include:: /reuse/links.txt
.. include:: /reuse/substitutions.txt
"""

# Allow for use of link substitutions
extlinks = {"lpsrc": ("https://launchpad.net/ubuntu/+source/%s", "%s")}

intersphinx_mapping = {
    "ubuntu-server": ("https://documentation.ubuntu.com/server/", None),
    "launchpad": ("https://documentation.ubuntu.com/launchpad/en/latest/", None),
    "adsys": ("https://documentation.ubuntu.com/adsys/stable/", None),
    "starter-pack": (
        "https://canonical-starter-pack.readthedocs-hosted.com/latest/",
        None,
    ),
    'sphinxcontrib-mermaid': ('https://sphinxcontrib-mermaid-demo.readthedocs.io/en/latest', None)
}

html_baseurl = "https://documentation.ubuntu.com/ubuntu-for-developers/"
sitemap_url_scheme = "{link}"

# Workaround for https://github.com/canonical/canonical-sphinx/issues/34
if "discourse_prefix" not in html_context and "discourse" in html_context:
    html_context["discourse_prefix"] = html_context["discourse"] + "/t/"

# Workaround for substitutions.yaml
if os.path.exists('./reuse/substitutions.yaml'):
    with open('./reuse/substitutions.yaml', 'r') as fd:
        myst_substitutions = yaml.safe_load(fd.read())

# Redefine the Sphinx 'command' role to behave/render like 'literal'
class CommandRole(SphinxRole):
    def run(self):
        text = self.text
        node = nodes.literal(text, text)
        return [node], []

def setup(app):
    roles.register_local_role("command", CommandRole())

# Define a custom role for package-name formatting
def pkg_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = nodes.literal(rawtext, text)
    return [node], []

roles.register_local_role("pkg", pkg_role)
