install:
		poetry install

gendiff-help:
		poetry run gendiff -h

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl

lint:
		poetry run flake8 gendiff

run-tests:
		poetry run pytest -v --cov=gendiff --cov-report term-missing
