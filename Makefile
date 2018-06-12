clean:
	rm -rf .pytest_cache
	rm -rf dist

.PHONY: docs
docs:
	pip install --upgrade catnado-docgen mkdocs mkdocs-material
	docgen build catnado mkdocs.yml --update-pages
	mkdocs build

pip-clean:
	pip freeze | xargs pip uninstall -y

.PHONY: build
build:
	pip install -r requirements.txt
	python setup.py bdist_wheel

upload:
	pip install --upgrade twine
	twine upload dist/*
