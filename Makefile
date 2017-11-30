deps:
	pipenv install --dev

shell: deps
	pipenv run bpython

run start: deps
	pipenv run tmuxp load tmuxp-advent.yaml

clean:
	pipenv --rm
	find . -iname '*.pyc' -exec rm {} \;


.PHONY: shell clean
