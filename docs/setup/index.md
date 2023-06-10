(setup)=

# Setup

````{note}
This section is intended to provide setup instructions for a launching docs site within your own projects.

```{seealso}
For this project's particular setup instructions (most likely for development purposes), see {ref}`development <development>`.
```
````

```{warning}
These setup docs are intended for use with **MacOS**
```

---

## Useful Links

- [**pyenv** GitHub Homepage](https://github.com/pyenv/pyenv)
- [**Poetry** Docs Site](https://python-poetry.org/docs/)
- [**Sphinx** Docs Site](https://www.sphinx-doc.org)
- [**PyData Sphinx Theme** Docs Site](https://pydata-sphinx-theme.readthedocs.io/)

---

## Prerequisites

- [**Homebrew**](https://brew.sh/)
- **pyenv**
  - ```zsh
    brew install pyenv
    ```
- **Poetry**
  - ```zsh
    brew install poetry
    ```

---

## Setup Steps

### 1. Clone the Repository, Copy the Docs Directory, and Cleanup

```{tip}
use `cd` to navigate to your project's root directory
```

```zsh
git clone https://github.com/wyattowalsh/docs-template.git && mv docs-template/docs/ . && rm -rf docs-template
```

### 2. Configure `pyproject.toml`

Add the following to your `pyproject.toml` file below your current dependencies:

```toml
[tool.poetry.group.docs]
optional = true

[tool.poetry.group.docs.dependencies]
sphinx = "^6"
pydata-sphinx-theme = "^0.13.3"
sphinx-design = "^0.4.1"
myst-parser = "^1.0.0"
sphinxcontrib-mermaid = "^0.9.2"
sphinx-copybutton = "^0.5.2"
sphinx-markdown-builder = "^0.5.5"
sphinx-git = "^11.0.0"
sphinx-autobuild = "^2021.3.14"
sphinx-hoverxref = "^1.3.0"
sphinx-sitemap = "^2.5.0"
sphinx-togglebutton = "^0.3.2"
sphinx-favicon = "^1.0.1"
sphinxcontrib-jquery = "^4.1"
linkify-it-py = "^2.0.2"
```

To install these dependencies, run:

```zsh
poetry install --with docs
```

### 3. Configure `docs/conf.py`

Change the following fields:

- [line 13] `project` -- change to your project name
- [line 21] `copyright` -- change name and contact
- [line 22] `author` -- change name and contact
- [line 77] `icon_links`/`url` -- change to your project's GitHub repo
