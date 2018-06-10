clean:
	rm -rf .pytest_cache
	rm -rf dist

.PHONY: build
build:
	pip install -r requirements.txt
	python setup.py bdist_wheel

upload:
	twine upload dist/*
