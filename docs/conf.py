import datetime
import os
import textwrap

from docutils import nodes
from docutils.parsers.rst import roles
from sphinx.util.docutils import SphinxRole

# Configuration for the Sphinx documentation builder.
# All configuration specific to your project should be done in this file.
#
# If you're new to Sphinx and don't want any advanced or custom features,
# just go through the items marked 'TODO'.
#
# A complete list of built-in Sphinx configuration values:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# The Sphinx Stack uses the Canonical Sphinx theme to keep all documentation consistent
# and on brand:
# https://github.com/canonical/canonical-sphinx

#######################
# Project information #
#######################

# Project name
project = "Ubuntu Desktop as a Developer Platform"

# Author name; used in the default copyright statement in the page footer
author = "Canonical Ltd."

# The year in the copyright statement
copyright = f"{datetime.date.today().year}"

# Sidebar documentation title
# To disable the title, set it to an empty string.
html_title = "Ubuntu for Developers"

# Documentation website URL
ogp_site_url = "https://ubuntu.com/developers/docs/"

# Preview name of the documentation website
# TODO: To use a different name for the project in previews, update the next line.
ogp_site_name = project

# Preview image URL
# TODO: To customise the preview image, update the next line.
ogp_image = "https://assets.ubuntu.com/v1/cc828679-docs_illustration.svg"

# Product favicon; shown in bookmarks, browser tabs, etc.
# TODO: To customise the favicon, uncomment and update the next line.
# html_favicon = "_static/favicon.png"

# Dictionary of values to pass into the Sphinx context for all pages:
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_context
html_context = {
    # Product page URL; can be different from product docs URL
    # TODO: Change to your product website URL, dropping the 'https://' prefix (e.g.,
    #       'ubuntu.com/lxd'). If there's no such website, remove the {{ product_page }}
    #       link from the _templates/header.html file.
    "product_page": "ubuntu.com/desktop/developers",
    # Product tag image; the orange part of your logo, shown in the page header
    # TODO: To add a tag image, uncomment and update as needed.
    # 'product_tag': '_static/tag.png',
    # Your Discourse instance URL
    # TODO: Change to your Discourse instance URL or leave empty.
    "discourse": "https://discourse.ubuntu.com/c/foundations/",
    # Your Mattermost channel URL
    # TODO: Change to your Mattermost channel URL or leave empty.
    "mattermost": "",
    # Your Matrix channel URL
    # TODO: Change to your Matrix channel URL or leave empty.
    "matrix": "https://matrix.to/#/#documentation:ubuntu.com",
    # Your documentation GitHub repository URL If set, links for viewing the
    # documentation source files and creating GitHub issues are added at the bottom of
    # each page.
    # TODO: Change to your documentation GitHub repository URL or leave empty.
    "github_url": "https://github.com/canonical/ubuntu-for-developers-docs",
    # Docs branch in the repo; used in links for viewing the source files
    "repo_default_branch": "main",
    # Docs location in the repo; used in links for viewing the source files
    "repo_folder": "/docs/",
    # Previous / Next buttons at the bottom of pages
    # Valid options: none, prev, next, both
    "sequential_nav": "both",
    # Display contributors on individual pages
    "display_contributors": True,
    # Links for the "Ubuntu docs" dropdown in the site header
    # (used by the custom header template in _templates/header.html)
    "ubuntu_docs": [
        {"title": "Ubuntu Desktop", "url": "https://documentation.ubuntu.com/desktop/"},
        {"title": "Ubuntu Server", "url": "https://ubuntu.com/server/docs/"},
        {
            "title": "Ubuntu on WSL",
            "url": "https://documentation.ubuntu.com/wsl/latest/",
        },
        {
            "title": "Ubuntu release notes",
            "url": "https://documentation.ubuntu.com/release-notes/",
        },
        {"title": "Ubuntu project", "url": "https://documentation.ubuntu.com/project/"},
        {"title": "Ubuntu Pro", "url": "https://documentation.ubuntu.com/pro/"},
    ],
    # Required for feedback button
    "github_issues": "enabled",
    # Passes the top-level 'author' value to the theme
    "author": author,
    # Documentation license information
    "license": {
        # TODO: Specify your project's license.
        # For the name, we recommend using the standard shorthand identifier from
        # https://spdx.org/licenses
        "name": "",
        # TODO: Link directly to your project's license statement.
        "url": "",
    },
}

# Enables the edit button on pages. Needs a link to a
# public repository on GitHub or Launchpad. Any of the following link domains
# are accepted:
# - https://github.com/example-org/example"
# - https://launchpad.net/example
# - https://git.launchpad.net/example
html_theme_options = {
    "source_edit_link": html_context["github_url"],
}

# Project slug
# (documentation is hosted on https://documentation.ubuntu.com/)
slug = "developers/docs"

#######################
# Sitemap configuration: https://sphinx-sitemap.readthedocs.io/
#######################

# Canonical URL used to generate the sitemap and canonical links
html_baseurl = "https://ubuntu.com/developers/docs/"

# sphinx-sitemap uses html_baseurl to generate the full URL for each page:
sitemap_url_scheme = "{link}"

# Custom sitemap file name (avoids clashing with the llms.txt file)
sitemap_filename = "doc-sitemap.xml"

# Include `lastmod` dates in the sitemap:
sitemap_show_lastmod = True

# TODO: Exclude pages that aren't user-facing from the sitemap (e.g., module pages
# generated by autodoc).
# Pages excluded from the sitemap:
sitemap_excludes = [
    "404/",
    "genindex/",
    "search/",
]

################################
# Template and asset locations #
################################

html_static_path = ["_static"]
templates_path = ["_templates"]

#############
# Redirects #
#############

# Add redirects to the 'redirects.txt' file
# https://sphinxext-rediraffe.readthedocs.io/en/latest/

# To set up redirects in the Read the Docs project dashboard:
# https://docs.readthedocs.io/en/stable/guides/redirects.html

rediraffe_branch = "main"
rediraffe_redirects = "redirects.txt"

# Strips '/index.html' from destination URLs when building with 'dirhtml'
rediraffe_dir_only = True


############################
# sphinx-llm configuration #
############################

# Use the url-suffix mode for Markdown copies of pages
llms_txt_suffix_mode = "url-suffix"
llms_txt_suppress_unknown_node_warnings = True

# This description is included in llms.txt to provide some initial context for your
# product docs.
# TODO: Add a description in the form "This is the documentation for <product name>,
# <first sentence of home page>".
llms_txt_description = textwrap.dedent(
    """\
    This documentation provides guidance for using the Ubuntu Desktop
    Linux distribution as a development platform. The guides focus on
    setting up and using the Ubuntu system as a workstation for developers,
    with an emphasis on the following toolchains: Python, Golang, Rust,
    GCC, Clang, .NET, Java, and Zig.
    """
)

# The base URL for references built by sphinx-markdown-builder.
markdown_http_base = "https://documentation.ubuntu.com/ubuntu-for-developers"

###########################
# Link checker exceptions #
###########################

# A regex list of URLs that are ignored by 'make linkcheck'
linkcheck_ignore = [
    "http://127.0.0.1:8000",
    r"https://crates\.io.*",
    r"https://www\.nongnu\.org/.*",
    r"https://www\.gnu\.org/.*",
    r"https://matrix\.to/.*",
    r"https://blog\.local-optimum\.net/.*",
    r"https://www\.winehq\.org.*",
]

# A regex list of URLs where anchors are ignored by 'make linkcheck'
linkcheck_anchors_ignore_for_url = [r"https://github\.com/.*"]

# How long the link checker will wait for a response for each request
# TODO: Decrease to improve run time or increase if links frequently time out.
# linkcheck_timeout = 30

# Give linkcheck multiple tries on failure
linkcheck_retries = 3

########################
# Configuration extras #
########################

# Custom MyST syntax extensions; see
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
# NOTE: By default, the following MyST extensions are enabled:
#   - substitution
#   - deflist
#   - linkify
myst_enable_extensions = {"colon_fence"}

# Custom Sphinx extensions; see
# https://www.sphinx-doc.org/en/master/usage/extensions/index.html
# NOTE: Deprecated extensions scheduled for removal in Sphinx Stack 3.0
# (sphinx_reredirects, sphinx_tabs, sphinx_config_options,
# sphinx_contributor_listing, sphinx_filtered_toctree, sphinx_related_links,
# sphinx_ubuntu_images, sphinx_youtube_links) are not loaded: this project
# does not use them.
extensions = [
    "canonical_sphinx",
    "notfound.extension",
    "sphinx_design",
    "sphinx_rerediraffe",
    "sphinxcontrib.jquery",
    "sphinxext.opengraph",
    "sphinx_llm.txt",
    "sphinx_roles",
    "sphinx_terminal",
    "sphinxcontrib.cairosvgconverter",
    "sphinx_last_updated_by_git",
    "sphinx.ext.intersphinx",
    "sphinx_sitemap",
    # Project-specific extensions
    "sphinx.ext.extlinks",
    "sphinxcontrib.mermaid",
]

# Excludes files or directories from processing
exclude_patterns = [
    "doc-cheat-sheet*",
    ".venv*",
    "reuse",
]

# Adds custom CSS files, located remotely or in 'html_static_path'.
html_css_files = ["custom_header.css", "cookie_banner.css"]

# Adds custom JavaScript files, located remotely or in 'html_static_path'.
html_js_files = ["js/bundle.js", "js/overwrite_links.js"]

# Appends extra markup to the end of every document written in reST
# rst_epilog = """
# """

# Feedback button at the top; enabled by default
# TODO: Disable the button if your project is unsuitable for public feedback.
# disable_feedback_button = True

# Your manpage URL
# TODO: To enable manpage links, uncomment and replace {codename} with required
#       release, preferably an LTS release (e.g. noble). Do *not* substitute
#       {section} or {page}; these will be replaced by sphinx at build time
#
# NOTE: If set, adding ':manpage:' to an .rst file
#       adds a link to the corresponding man section at the bottom of the page.
manpages_url = (
    "https://manpages.ubuntu.com/manpages/questing/man{section}/{page}.{section}.html"
)

############################################################
# Additional configuration
############################################################

# Add any configuration that is not covered by the common conf.py file.

# sphinx-llm config
llms_txt_suffix_mode = "url-suffix"
llms_txt_suppress_unknown_node_warnings = True
llms_txt_description = (
    "This documentation provides guidance for using the Ubuntu Desktop "
    "Linux distribution as a development platform. The guides focus on "
    "setting up and using the Ubuntu system as a workstation for developers, "
    "with an emphasis on the following toolchains: Python, Golang, Rust, "
    "GCC, Clang, .NET, Java, and Zig."
    "https://manpages.ubuntu.com/manpages/latest/man{section}/{page}.{section}.html"
)

# Specifies a reST snippet to be prepended to each .rst file
# This defines a :center: role that centers table cell content.
# This defines a :h2: role that styles content for use with PDF generation.
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

# Cross-documentation reference mapping
intersphinx_mapping = {
    "ubuntu-server": ("https://documentation.ubuntu.com/server/", None),
    "launchpad": ("https://documentation.ubuntu.com/launchpad/en/latest/", None),
    "adsys": ("https://documentation.ubuntu.com/adsys/stable/", None),
    "project": ("https://ubuntu.com/project/docs/", None),
}

# Allow for use of link substitutions
extlinks = {"lpsrc": ("https://launchpad.net/ubuntu/+source/%s", "%s")}


# Redefine the Sphinx 'command' role to behave/render like 'literal'
class CommandRole(SphinxRole):
    def run(self):
        text = self.text
        node = nodes.literal(text, text)
        return [node], []


def setup(app):
    roles.register_local_role("command", CommandRole())
    # Workaround for https://github.com/canonical/canonical-sphinx/issues/34
    if (
        "discourse_prefix" not in app.config.html_context
        and "discourse" in app.config.html_context
    ):
        app.config.html_context["discourse_prefix"] = (
            f"{app.config.html_context['discourse']}/t/"
        )


# Define a custom role for package-name formatting
def pkg_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = nodes.literal(rawtext, text)
    return [node], []


roles.register_local_role("pkg", pkg_role)
