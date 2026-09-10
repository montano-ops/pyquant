.PHONY: setup nbs check

setup:            ## install everything (run once)
	pip install -r requirements.txt
	pip install -e .

nbs:              ## (re)generate all .ipynb from tools/nbsrc/**/*.mdnb
	python tools/nbgen.py

check:            ## run package tests
	python -m pytest tests -q
