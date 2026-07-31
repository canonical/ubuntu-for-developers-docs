---
orphan: true
---

# Ubuntu for developers docs – structure & design decisions

> Reference for anyone (human or agent) adding or reorganizing content.
> Captures the filesystem hierarchy, navigation philosophy, and the rationale
> behind each structural decision. Last updated: 2026-07-26.

## 1. The dual-axis design (intentional, not a flaw)

The docs set uses **two axes** by design:

- **Sidebar navigation (toctree): Diátaxis-first.** Top-level directories are
  `tutorials/`, `howto/`, `reference/`, `explanation/`. The sidebar organizes
  content by *activity type* (learning, doing, looking up, understanding).
  This is the primary filesystem structure.
- **Homepage view: lifecycle-first.** The homepage (`docs/index.md`) "In this
  documentation" section organizes content by *workflow stage* (Introduction →
  Language toolchains → Packaging), with Diátaxis described separately as the
  underlying paradigm.

These two views are **intentionally different** and serve different reader
needs. Diátaxis is excellent for delineating learning phases but poor at
giving readers a map of where content lives. The lifecycle homepage counters
that.

**Do not "fix" the divergence by collapsing the two** – both axes carry
weight. The sidebar answers "I want to learn / do / look up / understand";
the homepage answers "where am I in my workflow and what's relevant now".

**Implication for new content:** place files in the Diátaxis quadrant matching
their *type*. Surface them for discovery via the homepage lifecycle section
and, where applicable, a toolchain landing page (§4).

## 2. Filesystem hierarchy

```text
docs/
├── index.md                  Homepage (lifecycle view)
├── tutorials/                Diátaxis: Tutorials
│   ├── index.md              Grouped toctree (first-program flat; advanced sub-toctrees)
│   ├── {lang}-use.md         First-program tutorials (flat)
│   ├── {topic}.md            Advanced tutorials (flat or in sub-toctree groups)
│   └── _{series}-series.md   Article-series manifests (included via {include})
├── howto/                    Diátaxis: How-to guides
│   ├── index.md
│   ├── {lang}-setup.md       Toolchain setup howtos
│   └── contribute-docs.md
├── reference/                Diátaxis: Reference
│   ├── index.md
│   ├── ides.md
│   └── availability/         Per-toolchain version reference
├── explanation/              Diátaxis: Explanation
│   ├── index.md              Grouped toctree (sub-headings per topic)
│   ├── install-ubuntu.md     Cross-toolchain concepts
│   ├── use-vcs.md
│   ├── packaging.md
│   └── {topic}.md            Toolchain-specific background
├── toolchains/               Landing pages (cross-link hubs, NOT in quadrant toctrees)
│   └── {lang}.md             "Little homepage" per toolchain
└── reuse/                    Internal include-library (snippets, NOT external content)
```

### Naming conventions

- **Articles:** short, no quadrant or namespace prefix (`java-use.md`, not
  `tutorial-java-use.md`).
- **Devpack articles:** `devpack-for-{name}.md` (e.g., `devpack-for-spring.md`).
- **Article-series manifests:** `_{series-name}-series.md` (underscore prefix
  keeps them out of toctrees).
- **Landing pages:** `{lang}.md` in `docs/toolchains/`.

## 3. Sub-toctree grouping within quadrant indexes

When a quadrant accrues multiple articles for one toolchain/topic, group them
under a named sub-heading with a sub-toctree in that quadrant's `index.md`.
Precedent: `explanation/index.md` has ".NET basics" and "GraalVM native image"
sub-headings.

**Rule:** a sub-toctree forms only when a toolchain has **≥2 advanced
articles** in that quadrant. A lone advanced article sits flat until it has a
peer. This prevents empty sub-headings.

First-program tutorials stay **flat** at the top of `tutorials/index.md` – no
"First programs" sub-heading.

Current sub-toctrees:

- `explanation/index.md`: ".NET basics", "GraalVM native image", "Devpacks"
- `tutorials/index.md`: "Java – Advanced" (graalvm-use, crac-use,
  devpack-for-spring, springai-basic, springai-rag, spring-ai-tool-calling),
  "Rust – Advanced" (devpack-for-rust)

## 4. Toolchain landing pages ("little homepages")

Each toolchain gets a landing page at `docs/toolchains/{lang}.md` – a
cross-link hub, **not** part of any quadrant toctree. Reached from:

- The homepage "Language toolchains and support" section (the toolchain name
  links here)
- Direct URL

Contents: "Get started" links (install howto + first-program tutorial +
version reference), "Advanced" links (grouped by topic), and any
article-series references for that toolchain. The landing page is a navigation
aid, not a content page – it links out to the Diátaxis-quadrant articles.

**When to create a landing page:** when a toolchain has ≥3 articles across the
docs set (install + tutorial + at least one advanced).

## 5. Article series

For tightly related article sequences (e.g., Spring AI: chat-client →
tool-calling → RAG), use the **article-series pattern** (adapted from
`ubuntu-project-docs`):

- Create `docs/tutorials/_{series-name}-series.md` containing an admonition
  box listing the series articles in order, plus any prerequisites.
- Include it at the top of each article in the series:

  ````markdown
  ```{include} _{series-name}-series.md
  ```
  ````

- Series can overlap (e.g., a "Java advanced" series and a "Spring AI"
  sub-series both reference the Spring AI articles). This is intentional –
  readers may arrive at any article and need both its immediate series and the
  broader toolchain context.

A series binds related articles *wherever they live in the filesystem* – no
directory moves required.

Current series:

- `_java-advanced-series.md` – binds GraalVM, CRaC, devpack-for-spring,
  Spring AI
- `_spring-ai-series.md` – binds the three Spring AI tutorials (sub-series of
  Java advanced)

## 6. Devpack content

Devpacks are toolchain-scoped developer automation tools (snap-packaged). Each
devpack gets **one article** filed under `tutorials/` in its toolchain's
advanced cluster (or flat if no cluster yet). The single article covers:
install (`snap install`), the `setup` command's config surface, scaffolding,
library management, and build plugins.

**No separate devpack-setup howto.** Bunching all devpack content in one
tutorial article keeps the `howto/` list from growing linearly with devpack
count. The Diátaxis impurity (config content in a tutorial) is an accepted
trade-off – the devpack's `setup` is self-contained, and the article-series +
landing page provide surrounding context. If a devpack's `setup` surface later
grows too deep, extract a howto at that point – don't pre-build the slot.

A general, cross-toolchain devpack explainer lives at
`explanation/devpacks.md` – written once, covering the snap-distribution model
conceptually. Each per-toolchain devpack tutorial cross-links to it rather than
re-explaining. The layered-snap architecture (devpack + content + runtime
snaps) is one possible implementation pattern, not a universal devpack model –
keep the explanation generic and mention specific layering as examples only.

## 7. Navigation depth constraint

Sidebar nav depth: **≤3 levels** (quadrant → sub-group → article). Toolchain
landing pages add a *content* layer (cross-links) but not a *nav* layer –
they're not in the sidebar toctree.

## 8. URL stability & redirects

Existing URLs are preserved where possible. When files move, redirects are
configured via [rediraffe](https://github.com/sphinx-doc/sphinxext-rediraffe), a
Sphinx extension that generates HTML redirect pages.

### Configuration (in `docs/conf.py`)

```python
extensions = [..., "sphinx_rerediraffe"]

rediraffe_branch = "main"
rediraffe_redirects = "redirects.txt"
rediraffe_dir_only = True
```

- `rediraffe_branch = "main"` – rediraffe compares the current branch against
  `main` to auto-detect removed files and generate redirects for them.
- `rediraffe_redirects = "redirects.txt"` – explicit redirect mappings in
  {file}`docs/redirects.txt` (one per line, format: `old/path new/path`,
  paths relative to the docs source dir, no `.md` suffix).
- `rediraffe_dir_only = True` – only auto-generate redirects for removed
  *directories*, not individual files. File-level redirects must be added
  manually to {file}`redirects.txt`.

### When to add redirects

Add an entry to {file}`docs/redirects.txt` whenever an existing page moves to
a new URL. The current structure keeps files in place – the Diátaxis
quadrant dirs stay, and re-grouping happens via toctree edits, not file moves.
Redirects are therefore rarely needed, but the mechanism is in place for
future restructuring.

## 9. Cross-toolchain content

Topics that apply across all toolchains (Ubuntu installation, Git, packaging,
IDEs, contributing) live in their natural Diátaxis quadrant:
`explanation/install-ubuntu.md`, `explanation/use-vcs.md`,
`explanation/packaging.md`, `reference/ides.md`, `howto/contribute-docs.md`.
They are *not* duplicated per toolchain; toolchain landing pages cross-link to
them where relevant.

## 10. The `reuse/` directory

`docs/reuse/` holds **snippets and content fragments** that are included into
other articles via MyST `{include}` directives. It exists to keep source files
navigable – shared blocks (setup steps, configuration snippets, repeated
warnings) live here and are pulled into the articles that need them, rather
than duplicated across the Diátaxis quadrant directories.

**Not external content.** Despite the name, `reuse/` does *not* hold content
mirrored from other Canonical docs sets. It is an internal include-library.
When adding a snippet that appears in two or more articles, place it here and
`{include}` it from each consumer. Keep the directory organized by topic
(`reuse/howto/`, `reuse/tutorials/`, `reuse/reference/`).

## 11. Decision checklist for new content

1. **What Diátaxis type is it?**

   - Tutorial (learning, hands-on, "Hello world"-ish) → `tutorials/`
   - How-to (configuring, installing, task-oriented) → `howto/`
   - Reference (lookup, versions, catalogs) → `reference/`
   - Explanation (background, concepts, why) → `explanation/`

2. **Is it toolchain-specific?** If yes, name it with the toolchain as
   prefix/identifier (`java-use.md`, `devpack-for-spring.md`). If
   cross-toolchain, file under the relevant quadrant with a general name
   (`install-ubuntu.md`).

3. **Does it belong to an article series?** If part of a sequence, ensure the
   series manifest exists (or create it) and `{include}` it at the top.

4. **Does its toolchain have ≥2 advanced articles in this quadrant?** If yes,
   ensure a named sub-toctree group exists in the quadrant's `index.md`. If
   no, leave it flat.

5. **Does the toolchain have a landing page?** If yes, add a cross-link to the
   new article. If no and the toolchain has ≥3 articles across the docs set,
   create `docs/toolchains/{lang}.md`.

6. **Update the homepage?** If the new article is a primary toolchain resource
   (install/tutorial/reference), add it to the "Language toolchains and
   support" line for that toolchain in `docs/index.md`. If it's advanced
   content, the landing page handles discovery – the homepage line stays
   concise.

7. **Nav depth check?** Ensure adding the article doesn't push any toctree
   beyond 3 levels.

8. **Is it a devpack?** One article per devpack, filed under `tutorials/`.
   Cover install + setup + usage in the single article. Cross-link to
   `explanation/devpacks.md`. No separate howto.
