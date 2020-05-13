# Запуск тестов
Тесты запускаются из корня проекта:

```bash
sh ./test.sh
```

или

```bash
PYTHONPATH=${PWD} pytest -v tests/*
```

## Необходимые пакеты:

* `PyHamcrest`
* `pylint`
* `pytest`
* `python-dateutil`
* `requests`
