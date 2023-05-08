.venv/bin/activate: code/requirements.txt
	python -m venv .venv
	.venv/bin/python -m pip install --upgrade pip
	.venv/bin/pip install -r code/requirements.txt

run: .venv/bin/activate
	.venv/bin/python code/testingORtools.py
	.venv/bin/python code/VRP_alg.py

clean: 
	rm -rf .venv

all: run

.PHONY: clean run all