PYTHON = $(ENV)/bin/python
ENV = $(CURDIR)/env

env:
	virtualenv --python=$(shell which python2.7) $(ENV)

deps: env
	$(ENV)/bin/pip install -U pip setuptools
	$(ENV)/bin/pip install -Ur requirements.txt

shell:
	$(ENV)/bin/bpython

run start: deps
	$(ENV)/bin/tmuxp load tmuxp-advent.yaml

clean:
	rm -rf $(ENV)
	find . -iname '*.pyc' -exec rm {} \;


.PHONY: shell clean
