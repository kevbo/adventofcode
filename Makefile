deps:
	pipenv install --dev

shell: deps
	pipenv run bpython

run start: deps
	pipenv run tmuxp load tmuxp-advent.yaml

clean:
	pipenv --rm
	find . -iname '*.pyc' -exec rm {} 
	rm -rf __pycache__

ci-install:
	pip install pipenv
	pipenv install --dev --ignore-pipfile

test:
	pipenv run coverage run -m unittest
	pipenv run coverage report -m
	pipenv run coverage xml
	pipenv check
	pipenv check --style *.py

.PHONY: shell clean test ci-install run start deps
