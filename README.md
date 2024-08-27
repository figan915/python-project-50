# Вычислитель отличий (gendiff)

***
 Hexlet tests and linter status:
[![Actions Status](https://github.com/figan915/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/figan915/python-project-50/actions)

### Github Action:
[![gendiff_actions](https://github.com/figan915/python-project-50/actions/workflows/test_gendiff.yml/badge.svg)](https://github.com/figan915/python-project-50/actions/workflows/test_gendiff.yml)

### Codeclimat bages:
[![Maintainability](https://api.codeclimate.com/v1/badges/27eeae5c397c3a911be0/maintainability)](https://codeclimate.com/github/figan915/python-project-50/maintainability)

### [![Test Coverage](https://api.codeclimate.com/v1/badges/27eeae5c397c3a911be0/test_coverage)](https://codeclimate.com/github/figan915/python-project-50/test_coverage)


__"Вычислитель отличий" (gendiff)__ - второй проект, разработанный в рамках обучения на курсе Хекслет. Это инструмент командной строки для поиска различий между двумя файлами.

***

## Установка
Для установки и запуска проекта вам потребуется Python версии  3.10 и выше и инструмент для управления зависимостями Poetry.

1. Склонируйте репозиторий с проектом на ваше локальное устройство:
```
git clone git@github.com:figan915/python-project-50.git
```
2. Перейдите в директорию проекта:
```
cd python-project-50
```
3. Установите необходимые зависимости с помощью Poetry:
```
poetry install
```
#### Поддерживаемые форматы файлов
Проект поддерживает следующие форматы файлов для поиска отличий:

- YAML (.yaml, .yml)
- JSON (.json)
***
## Как найти различия между двумя файлами:
1. Поместите два файла, которые вы хотите сравнить, в папку tests/fixtures.
2. Выполните команду для поиска различий:
```
poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
```
3. Замените file1.json и file2.json на названия ваших файлов
4. В корне проекта выполните package-install, которая установит пакет gendiff.
5. После установки пакета, выполните gendiff path_to_file1 path_to_file2, где path_to_file - путь до ваших файлов.
***
## Форматы вывода
Для выбора формата вывода различий, укажите флаг -f с названием форматтера. Возможные форматтеры:

- stylish (по умолчанию)
- plain
- json



### Вывод справки и сравнение плоских файлов .json:
[![asciicast](https://asciinema.org/a/8qYeZ5rUpL2baDSxJtVinYiYb.svg)](https://asciinema.org/a/8qYeZ5rUpL2baDSxJtVinYiYb)

### Сравнение файлов .yaml:
[![asciicast](https://asciinema.org/a/DRkbv8mPrnRfeQiJawmWQ7Mn8.svg)](https://asciinema.org/a/DRkbv8mPrnRfeQiJawmWQ7Mn8)

### Вывод в стиле stylish:
[![asciicast](https://asciinema.org/a/YLk4IdzBNwMi1VhPGARTCJQny.svg)](https://asciinema.org/a/YLk4IdzBNwMi1VhPGARTCJQny)

### Вывод в стиле plain:
[![asciicast](https://asciinema.org/a/2rTj5UmLsSTeOxvDKa4un9WBB.svg)](https://asciinema.org/a/2rTj5UmLsSTeOxvDKa4un9WBB)

### Вывод в формате json
[![asciicast](https://asciinema.org/a/gEKW0oeFxk9JlNyiN7WDRXkO3.svg)](https://asciinema.org/a/gEKW0oeFxk9JlNyiN7WDRXkO3)
