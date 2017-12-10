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

new:
	touch day$(day).py
	touch tests/test_day$(day).py
	touch day$(day)_input.txt
	git checkout -b day$(day)

.PHONY: shell clean test ci-install run start deps new
