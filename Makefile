install:
	python -m pip install --upgrade pip
	python -m pip install pytest

test:
	python -m pytest -v

run:
	python main.py