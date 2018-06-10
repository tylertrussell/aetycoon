clean:
	rm -rf .pytest_cache
	rm -rf dist

.PHONY: build
build:
	python setup.py bdist_wheel

upload:
	twine upload dist/*
