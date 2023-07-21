repl:
	poetry run ipython

install:
	poetry install

run:
	poetry run gendiff

build: check
	rm -rf dist/
	poetry build

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff/

test-cov:
	poetry run pytest --cov=gendiff --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

package-install:
	python3 -m pip uninstall hexlet-code -y
	python3 -m pip install --user dist/*.whl

.PHONY: install test lint selfcheck check build
