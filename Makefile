env:
	virtualenv env

bpython: env
	env/bin/pip install bpython
	env/bin/bpython
