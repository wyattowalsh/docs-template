# docs

- [pydata-sphinx-theme.readthedocs.io](https://pydata-sphinx-theme.readthedocs.io/)
-

-
-

-
-
-
- https://cloudconvert.com/

```zsh

```

```zsh
poetry init
```

```zsh
pyenv local 3.11
poetry env use python3.11
```

```zsh
poetry add sphinx@^6 pydata-sphinx-theme sphinx-design myst-parser sphinxcontrib-mermaid sphinx-copybutton sphinx-markdown-builder sphinx-git  sphinx-autobuild sphinx-hoverxref  sphinx-sitemap sphinx-togglebutton sphinx-favicon sphinxcontrib-jquery linkify-it-py -G docs
```

```zsh
sphinx-quickstart docs
```

add to docs/conf.py

```python
html_theme = "pydata_sphinx_theme"
```
