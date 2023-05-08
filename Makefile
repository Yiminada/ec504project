.venv/Scripts/activate: code/requirements.txt
	python -m venv .venv
	# .venv/Scripts/python -m pip install --upgrade pip
	# .venv/Scripts/pip install -r code/requirements.txt
	ls -lta
	ls .venv/Scripts
	source .venv/Scripts/activate

clean: 
	rm -rf .venv

.PHONY: clean