install:
	poetry install

diff:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

diff_plain:
	poetry run gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml -f plain

diff_json:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json -f json

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall --yes dist/*.whl

lint:
	poetry run flake8 gendiff

lint_test:
	poetry run flake8 tests
test:
	poetry run pytest

test-coverage:
	poetry run coverage run -m pytest --cov-report xml
	poetry run coverage lcov -o coverage/lcov.info

