.venv/bin/activate: code/requirements.txt
	python -m venv .venv
	.venv/bin/python -m pip install --upgrade pip
	.venv/bin/pip install -r code/requirements.txt

clean: 
	rm -rf .venv

.PHONY: clean