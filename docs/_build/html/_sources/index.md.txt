---
notoc: true
---

<div align='center'>
    <h1 class="landing-title">docs-template</h1>
    <h3>An Advanced <a href="https://www.sphinx-doc.org"><b><i>Sphinx</i></b></a>-based Docs Site Template</h3>
</div>

---

```{raw} html
<form class="bd-search align-items-center" action="search.html" method="get">
    <input type="search" class="form-control search-front-page" name="q" id="search-input" placeholder="🔍 Search the docs site here..." aria-label="Search the docs site..." autocomplete="on">
</form>
```

---

```{image} ./_static/img/landing.webp
:align: center
:class: hero-image
```

```{raw} html
<hr class="site-hr"/>
```

## Site Contents

````{grid} 1
:margin: 1
```{grid-item-card} Setup
:link: setup
:link-type: ref
:img-top: ./_static/img/icons/setup.svg
:padding: 2
:shadow: lg
:columns: 6
{mod}`docs-template` setup instructions.
```
```{grid-item-card} Usage
:link: usage
:link-type: ref
:img-top: ./_static/img/icons/usage.svg
:padding: 2
:shadow: lg
:columns: 6
Learn how to use the template to **create**, ***personalize***, and <u><b>manage</b></u> your own docs site.
```
```{grid-item-card} Resources
:link: resources
:link-type: ref
:img-top: ./_static/img/icons/reference.svg
:padding: 2
:shadow: lg
:columns: 6
Useful reference information including helpful links to design, color, icon, and other resources.
```
```{grid-item-card} Development
:link: development
:link-type: ref
:img-top: ./_static/img/icons/development.svg
:padding: 2
:shadow: lg
:columns: 6
Notes for future {mod}`docs-template` development.
```
````

```{raw} html
<hr class="site-hr"/>
```

```{include} ./usage/features.md

```

```{raw} html
<hr class="site-hr"/>
```

## Indices and tables

- {ref}`genindex`
- {ref}`modindex`
- {ref}`search`

```{raw} html
<hr class="site-hr"/>
```

## Change Log

```{git_changelog}

```

```{toctree}
:maxdepth: 1
:titlesonly:
:hidden:

setup/index
usage/index
resources/index
development/index
```
