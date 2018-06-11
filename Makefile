clean:
	rm -rf .pytest_cache
	rm -rf dist

pip-clean:
	pip freeze | xargs pip uninstall -y

.PHONY: build
build:
	pip install -r requirements.txt
	python setup.py bdist_wheel

upload:
	twine upload dist/*
