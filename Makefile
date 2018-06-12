clean:
	rm -rf .pytest_cache
	rm -rf dist

.PHONY: docs
docs:
	catnado-docgen build mkdocs.yml --update-pages
	mkdocs build

pip-clean:
	pip freeze | xargs pip uninstall -y

.PHONY: build
build:
	pip install -r requirements.txt
	python setup.py bdist_wheel

upload:
	twine upload dist/*
