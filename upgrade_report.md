# In-Place Upgrade Report: Canonical Sphinx Starter Pack

**Date:** 2025-12-08
**Status:** Success

## Executive Summary
The Sphinx documentation project in `docs/` has been successfully upgraded to the latest Canonical Sphinx Starter Pack standards. The upgrade was performed in-place, preserving all project-specific content, custom extensions, and metadata while adopting the new configuration structure, dependencies, and build tooling.

## Detailed Changes

### 1. Configuration (`conf.py`)
The `conf.py` file was completely reconstructed to align with the new starter pack while retaining local customizations.

*   **Base Configuration**: Adopted the new starter pack's structure for imports, path setup, and global variables.
*   **Project Metadata**: Preserved `project`, `author`, `copyright`, `html_title`, and Open Graph Protocol (OGP) settings.
*   **HTML Context**: Retained all `html_context` settings (links to GitHub, Discourse, Mattermost, etc.) and `html_theme_options`.
*   **Extensions**:
    *   Migrated to the explicit extension list required by the new `canonical-sphinx` package.
    *   Added new required extensions: `sphinx_design`, `sphinx_copybutton`, `sphinx_terminal`, `sphinx_reredirects`, `sphinxext.opengraph`, etc.
    *   Preserved custom extensions: `sphinxcontrib.mermaid`, `sphinx_prompt`, `sphinx.ext.extlinks`.
*   **Custom Roles**: Re-registered custom roles `CommandRole` (for `:command:`) and `pkg_role` (for `:pkg:`).
*   **Prolog/Epilog**: Added `rst_prolog` for global role definitions (`:center:`, `:h2:`, etc.) and `rst_epilog` for including reuse files (`links.txt`, `substitutions.txt`).

### 2. Dependencies (`requirements.txt`)
The dependency list was updated to match the new ecosystem.

*   **Core**: Updated `canonical-sphinx` to `>=0.5.1`.
*   **Explicit Additions**: Added individual packages that are no longer bundled automatically (e.g., `sphinx-design`, `sphinx-notfound-page`, `sphinx-tabs`).
*   **Custom**: Retained `sphinxcontrib-mermaid` and `sphinx-prompt`.

### 3. Build System (`Makefile`)
The `Makefile` was replaced with the latest version from the starter pack.
*   Includes improved targets for linting (`lint-md`), spelling (`spelling`, `woke`), and accessibility checks (`pa11y`).
*   Standardized environment variables and build paths.

### 4. Content & Structure
*   **Reuse Files**: Copied updated reuse assets (`links.txt`, `substitutions.txt`, `substitutions.yaml`) from the starter pack to `docs/reuse/`.
*   **Cleanup**: Removed temporary backup directories and the source starter pack directory (`sp-updated/`) after verification.

## Migration of Custom Content

### `{terminal}` Directive Syntax Change
A significant breaking change in the `sphinx-terminal` extension was identified and resolved. The `:input:` option is deprecated and no longer supported.

**Old Syntax:**
```markdown
```{terminal}
:user: dev
:host: ubuntu
:input: some command

output
```
```

**New Syntax:**
```markdown
```{terminal}
:user: dev
:host: ubuntu

some command

output
```
```

**Action Taken:**
An automated script was developed and executed to migrate all instances of the `{terminal}` directive in the following files:
*   `docs/howto/dotnet-setup.md`
*   `docs/howto/gcc-setup.md`
*   `docs/howto/python-setup.md`
*   `docs/explanation/debugging-with-dotnet.md`
*   `docs/tutorials/dotnet-use.md`
*   `docs/tutorials/go-use.md`
*   `docs/tutorials/python-use.md`
*   `docs/tutorials/java-use.md`
*   `docs/tutorials/gcc-use.md`
*   `docs/tutorials/rust-use.md`

This ensured that the build completed with **zero warnings** related to terminal directives.

## Build Status

*   **Command**: `make html`
*   **Result**: **Success**
*   **Warnings**: 0
*   **Output Directory**: `docs/_build/`

## Verification & Next Steps

1.  **Visual Inspection**: It is recommended to manually check the rendered HTML pages, particularly those containing terminal blocks (e.g., `howto/python-setup.html`), to ensure the styling and layout are correct.
2.  **Version Control**: The repository is currently in a clean state with the upgrade applied. You should review the changes and commit them to your version control system.
3.  **Future Maintenance**: When adding new terminal blocks, ensure you use the new syntax (command in the body, separated by a blank line).
