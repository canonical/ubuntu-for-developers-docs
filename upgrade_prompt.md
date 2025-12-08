Title: In-Place Upgrade of Canonical Sphinx Starter Pack with Breaking Change Mitigation

Mission:
Perform a robust, in-place upgrade of an existing Sphinx documentation project (`docs/`) to a newer Canonical starter pack version (`sp-updated/`). The upgrade must preserve local customizations while proactively identifying and resolving breaking changes in dependencies, configuration, and directive syntax (e.g., deprecated options in MyST or Sphinx extensions).

Context:
- `docs/`: Existing documentation project with customizations (conf.py, extensions, themes).
- `sp-updated/`: New starter pack reference implementation.
- Common pitfalls in this upgrade path include:
  - "Unbundling" of extensions (extensions previously included in a meta-package must now be listed explicitly).
  - Syntax changes in directives (e.g., `sphinx-terminal` changing how inputs are defined).
  - Build failures due to stricter warning policies in newer Makefiles.

Task Requirements:
1. **Mandatory Backup**: Create a full backup of `docs/` before applying changes.
2. **Dependency Reconciliation**: Explicitly check if the new starter pack requires listing extensions that were previously implicit.
3. **Syntax Migration**: Proactively scan for and migrate deprecated directive syntax by comparing existing usage against new starter pack examples.
4. **Robust Tooling**: Use Python scripts for complex multi-line text replacements or migrations, rather than fragile shell one-liners (sed/awk).
5. **Clean Build**: Ensure `make html` passes with zero warnings.

Process / Steps:
1. **Initial Assessment & Backup**:
   - Identify project root, `docs/`, and `sp-updated/`.
   - **CRITICAL**: Create a recursive backup of `docs/` (e.g., `cp -r docs docs_backup`).
   - List active extensions in `docs/conf.py` and dependencies in `docs/requirements.txt`.

2. **Dependency & Configuration Analysis**:
   - Compare `sp-updated/docs/requirements.txt` with `docs/requirements.txt`.
   - **Crucial Check**: If `canonical-sphinx` is updated, check if it has "unbundled" extensions. You will likely need to explicitly add packages like `sphinx-design`, `sphinx-copybutton`, `sphinx-terminal`, etc., to `docs/requirements.txt` and `docs/conf.py` even if they weren't there before.
   - Create a new `docs/conf.py` by merging:
     - The *new* structure and defaults from `sp-updated/`.
     - The *existing* project metadata (`project`, `copyright`, `html_context`, `html_theme_options`) and custom extensions from the old `conf.py`.

3. **Structure Synchronization**:
   - Update `docs/Makefile` to the new version.
   - Copy new or updated assets from `sp-updated/docs/reuse/` to `docs/reuse/`.
   - Update `_static` and `_templates` only if they don't contain project-specific overrides.

4. **Syntax Compatibility Scan**:
   - Before building, compare the usage of key directives (e.g., `{terminal}`, `{tabs}`, `{note}`) in `docs/` against the reference examples in `sp-updated/docs/reference/`.
   - **Action**: If syntax has changed (e.g., `:input:` option deprecated in favor of body content), write a Python script to automate the migration across all `.md` and `.rst` files. Do not rely on manual edits or simple regex for structural changes.

5. **Iterative Build & Fix**:
   - Run `make html` in `docs/`.
   - **Phase 1 - Dependencies**: Fix `ModuleNotFoundError` by adding missing packages to `requirements.txt`.
   - **Phase 2 - Configuration**: Fix configuration errors in `conf.py`.
   - **Phase 3 - Syntax/Content**: Fix warnings (treated as errors) related to directive usage. Use the Python script approach for batch fixes.

6. **Validation**:
   - Verify the build completes successfully.
   - Manually inspect generated HTML for complex directives (terminals, tabs) to ensure they render correctly.
   - Ensure custom extensions (e.g., Mermaid, specific roles) still function.

7. **Cleanup & Reporting**:
   - Remove `docs_backup`, `sp-updated/`, and any temporary migration scripts.
   - Generate a report (`upgrade_report.md`) detailing:
     - Configuration changes.
     - Dependency updates (specifically unbundled extensions).
     - Syntax migrations performed (e.g., "Converted terminal directive from :input: style to body style").

Constraints & Guardrails:
- **Never** overwrite `conf.py` blindly; always merge.
- **Never** leave the repository in a broken build state.
- **Prefer** Python scripts for migration logic to ensure handling of newlines and indentation is correct.
- **Maintain** the `docs/` directory as the source of truth; do not switch to `sp-updated/`.

Output Specification:
- Produce the final upgraded `docs/` directory.
- Produce `upgrade_report.md`.
