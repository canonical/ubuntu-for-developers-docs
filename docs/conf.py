import datetime
from docutils.parsers.rst import roles
from sphinx.util.docutils import SphinxRole
from docutils import nodes

# Configuration for the Sphinx documentation builder.
# All configuration specific to your project should be done in this file.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# For our custom configuration, see the Canonical Sphinx extension:
# https://github.com/canonical/canonical-sphinx
#
# If you're not familiar with Sphinx and don't want to use advanced
# features, it is sufficient to update the settings in the "Project
# information" section.

############################################################
# Project information
############################################################

# Product name
project = "Ubuntu Desktop as a Developer Platform"
author = "Canonical Ltd."

# The title you want to display for the documentation in the sidebar.
# You might want to include a version number here.
# To not display any title, set this option to an empty string.
html_title = "Ubuntu for Developers"

# The default value uses CC-BY-SA as the license and the current year
# as the copyright year.
#
# If your documentation needs a different copyright license, use that
# instead of 'CC-BY-SA'. Also, if your documentation is included as
# part of the code repository of your project, it'll inherit the license
# of the code. So you'll need to specify that license here (instead of
# 'CC-BY-SA').
#
# For static works, it is common to provide the year of first publication.
# Another option is to give the first year and the current year
# for documentation that is often changed, e.g. 2022–2023 (note the en-dash).
#
# A way to check a GitHub repo's creation date is to obtain a classic GitHub
# token with 'repo' permissions here: https://github.com/settings/tokens
# Next, use 'curl' and 'jq' to extract the date from the GitHub API's output:
#
# curl -H 'Authorization: token <TOKEN>' \
#   -H 'Accept: application/vnd.github.v3.raw' \
#   https://api.github.com/repos/canonical/<REPO> | jq '.created_at'

copyright = "%s CC-BY-SA, %s" % (datetime.date.today().year, author)

# Open Graph configuration - defines what is displayed as a link preview
# when linking to the documentation from another website (see https://ogp.me/)
# The URL where the documentation will be hosted (leave empty if you
# don't know yet)
ogp_site_url = "https://canonical-ubuntu-for-developers.readthedocs-hosted.com/"
# The documentation website name (usually the same as the product name)
ogp_site_name = project
# The URL of an image or logo that is used in the preview
ogp_image = "https://assets.ubuntu.com/v1/253da317-image-document-ubuntudocs.svg"

# Update with the local path to the favicon for your product
# (default is the circle of friends)
# html_favicon = '.sphinx/_static/favicon.png'

# (Some settings must be part of the html_context dictionary, while others
#  are on root level. Don't move the settings.)
html_context = {
    # Change to the link to the website of your product (without "https://")
    # For example: "ubuntu.com/lxd" or "microcloud.is"
    # If there is no product website, edit the header template to remove the
    # link (see the readme for instructions).
    "product_page": "ubuntu.com/desktop/developers",
    # Add your product tag (the orange part of your logo, will be used in the
    # header) to ".sphinx/_static" and change the path here (start with "_static")
    # (default is the circle of friends)
    # 'product_tag': '_static/tag.png',
    # Change to the discourse instance you want to be able to link to
    # using the :discourse: metadata at the top of a file
    # (use an empty value if you don't want to link)
    "discourse": "https://discourse.ubuntu.com/c/foundations/",
    # Change to the Mattermost channel you want to link to
    # (use an empty value if you don't want to link)
    "mattermost": "",
    # Change to the Matrix channel you want to link to
    # (use an empty value if you don't want to link)
    "matrix": "https://matrix.to/#/#documentation:ubuntu.com",
    # Change to the GitHub URL for your project
    # This is used, for example, to link to the source files and allow creating
    # GitHub issues directly from the documentation.
    "github_url": "https://github.com/canonical/ubuntu-for-developers-docs",
    # Change to the branch for this version of the documentation
    # 'github_version': 'main',
    # Change to the folder that contains the documentation
    # (usually "/" or "/docs/")
    "repo_folder": "/docs/",
    # Change to an empty value if your GitHub repo doesn't have issues enabled.
    # This will disable the feedback button and the issue link in the footer.
    "github_issues": "enabled",
    # Controls the existence of Previous / Next buttons at the bottom of pages
    # Valid options: none, prev, next, both
    "sequential_nav": "both",
    # Controls whether to display the contributors for each file
    "display_contributors": True,
    # Controls the time frame for showing the contributors
    # "display_contributors_since": ""
}

# Enables the edit button on pages. Needs a link to a
# public repository on GitHub or Launchpad. Any of the following link domains
# are accepted:
# - https://github.com/example-org/example"
# - https://launchpad.net/example
# - https://git.launchpad.net/example
#
html_theme_options = {
    "source_edit_link": html_context["github_url"],
}

# If your project is on documentation.ubuntu.com, specify the project
# slug (for example, "lxd") here.
# slug = ""

# These paths are needed if you want to override any default assets.
# You can comment them out if you don't need this (but you can also just
# leave them).

html_static_path = [".sphinx/_static"]
templates_path = [".sphinx/_templates"]

############################################################
# Redirects
############################################################

# Set up redirects (https://documatt.gitlab.io/sphinx-reredirects/usage.html)
# For example: 'explanation/old-name.html': '../how-to/prettify.html',
# You can also configure redirects in the Read the Docs project dashboard
# (see https://docs.readthedocs.io/en/stable/guides/redirects.html).
# NOTE: If this variable is not defined, set to None, or the dictionary is empty,
# the sphinx_reredirects extension will be disabled.
redirects = {}

############################################################
# Link checker exceptions
############################################################

# Links to ignore when checking links
linkcheck_ignore = [
    "http://127.0.0.1:8000",
    "https://crates.io",
    r"https://www\.nongnu\.org/.*",
    r"https://www\.gnu\.org/.*",
    r"https://matrix\.to/.*",
]

# Pages on which to ignore anchors
# (This list will be appended to linkcheck_anchors_ignore_for_url)
linkcheck_anchors_ignore_for_url = [r"https://github\.com/.*"]

linkcheck_retries = 3

############################################################
# Additions to default configuration
############################################################

# The following settings are appended to the default configuration.
# Use them to extend the default functionality.

# By default, the following MyST extensions are enabled:
# substitution, deflist, linkify
# If you need more extensions, add them here.
myst_enable_extensions = {"colon_fence"}

# You must include the canonical_sphinx extension here.
# This extension automatically enables the following Sphinx extensions:
# custom-rst-roles, myst_parser, notfound.extension, related-links,
# sphinx_copybutton, sphinx_design, sphinx_tabs.tabs,
# sphinx_reredirects, sphinxcontrib.jquery, sphinxext.opengraph,
# terminal-output, youtube-links
# If you need more extensions, add them here (in addition to
# canonical_sphinx).
extensions = [
    "canonical_sphinx",
    "sphinxcontrib.cairosvgconverter",
    "sphinx_last_updated_by_git",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.mermaid",
    "sphinx_prompt",
    "sphinx.ext.extlinks",
    "sphinx_sitemap",
]

myst_fence_as_directive = ["mermaid"]

# Add files or directories that should be excluded from processing.
exclude_patterns = [
    "reuse",
]

# Add custom CSS files (located in .sphinx/_static/)
html_css_files = ["custom_header.css", "cookie_banner.css"]

# Add custom JavaScript files (located in .sphinx/_static/)
html_js_files = ["js/bundle.js"]

# The following settings override the default configuration.

# By default, the documentation includes a feedback button at the top.
# You can disable it by setting the following configuration to True.
# disable_feedback_button = False

# If you are using the :manpage: role, set this variable to the URL for the version
# that you want to link to:
manpages_url = (
    "https://manpages.ubuntu.com/manpages/plucky/en/man{section}/{page}.{section}.html"
)

############################################################
# Additional configuration
############################################################

# Add any configuration that is not covered by the common conf.py file.

# Define a :center: role that can be used to center the content of table cells.
rst_prolog = """
.. role:: center
   :class: align-center
"""


# Allow for use of link substitutions
extlinks = {"lpsrc": ("https://launchpad.net/ubuntu/+source/%s", "%s")}


# Define intersphinx mapping
intersphinx_mapping = {
    "ubuntu-server": ("https://documentation.ubuntu.com/server/", None),
    "launchpad": ("https://documentation.ubuntu.com/launchpad/en/latest/", None),
    "adsys": ("https://documentation.ubuntu.com/adsys/stable/", None),
    "starter-pack": (
        "https://canonical-starter-pack.readthedocs-hosted.com/latest/",
        None,
    ),
}


# Sitemap configuration
html_baseurl = "https://documentation.ubuntu.com/ubuntu-for-developers/"
sitemap_url_scheme = "{link}"


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
