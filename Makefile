# bot project Makefile

.ONESHELL:

# https://www.gnu.org/prep/standards/html_node/Makefile-Basics.html#Makefile-Basics
SHELL = /bin/bash

help:           ## Show this help.
	fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

docs build html:  ## build docs as html
	echo "Building docs..."
	poetry shell && poetry install --with docs
	cd docs/ && poetry run make html
	echo "Docs built in docs/build/html"

docs server: ## launch docs server
	echo "Starting docs server..."
	poetry shell && poetry install --with docs
	poetry run sphinx-autobuild docs docs/_build/html --port 7777 --open-browser -a --watch docs/_static