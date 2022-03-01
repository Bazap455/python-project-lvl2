install:
		poetry install

gendiff-help:
		poetry run gendiff -h

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python -m pip install --user dist/*.why

lint:
		poetry run flake8 gendiff
