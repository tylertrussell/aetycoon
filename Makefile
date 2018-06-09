clean:
    rm -r .pytest_cache
    rm -r dist

build:
    python setup.py bdist_wheel

upload:
    twine upload dist/*
