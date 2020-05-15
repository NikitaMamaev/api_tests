# О проекте

Данный проект - результат выполнения тестового задания по написанию API-автотестов к сервису подписок.

# Запуск тестов
> Тесты запускаются из корня проекта:

```bash
sh ./test.sh
```

или

```bash
PYTHONPATH=${PWD} pytest -v tests/*
```

### Необходимое ПО:

* `PyHamcrest`
* `pylint`
* `pytest`
* `python-dateutil`
* `requests`

# Результаты тестирования

Во время тестирования сервис подписок был доступен по IP-адресу `192.168.0.3`, сам же адрес для удобства вынесен в настройки (файл `settings.py`, константа `LOCAL_IP`).

Представленные в проекте тесты можно разделить на позитивные и негативные.

### Позитивные тесты

Позитивные тесты находятся в файлах `tests/test/test_deleting.py` и `tests/test/test_positive_creating.py`. Список тестов:

* Удаление подписок (`test_subscriptions_deleting`):

Перед тестированием создаётся подписка, в самом же тесте происходит DELETE-запрос к `http://192.168.0.3:4000/subscriptions`, после чего проверяется, что GET-запрос к `http://192.168.0.3:4000/subscriptions`возвращает пустой список.

* Создание подписки с корректными данными (`test_creating_with_correct_data`):

В тесте происходит POST-запрос к `http://192.168.0.3:4000/subscriptions`, в теле которого отправляются *корректные** данные, после чего проверяется, что GET-запрос к `http://192.168.0.3:4000/subscriptions` возвращает список, содержащий запись с ранее введёнными данными.

> \* Поскольку к данным не предъявляется явных требований (за исключением валидации поля `email` при добавлении подписки), было принято решение считать корректными данные, подходящие под следующие регулярные выражения:
>
> Для я `email`: "`^\w+@[a-z]+.[a-z]{2,3}`"
>
> Для `name`: "`^[A-Z][a-z]+ [A-Z][a-z]+$`"
>
> Для `time`: "`^(\d+d)? *(\d+h)? *(\d+m)? *(\d+s)? *$`"
>
> Также предполагается, что вводимые значения должны валидироваться.

* Создание шестой подписки в списке (`test_sixth_subscription_creating`):

Перед тестированием заполняется список подписок (создаётся 5 записей), в самом же тесте с помощью POST-запроса к `http://192.168.0.3:4000/subscriptions` создаётся шестая запись, а затем проверяется, что, во-первых, эта запись есть в списке (результат GET-запроса к `http://192.168.0.3:4000/subscriptions`), и во-вторых, что в списке нет записи, которая создавалась первой.

### Негативные тесты

Негативные тесты находятся в файле `tests/test/test_negative_creating.py`. Список тестов:

* Создание подписки с существующим `email` (`test_creating_existing_subscription`)

Создание двух подписок с одинаковыми параметрами. Предполагается, что вторая запись не создастся.

* Создание подписки с пустым `email` (`test_creating_with_empty_email`)

Предполагается, что нельзя создать подписку с пустым полем `email`. Предположение основано на тексте в баннере:

> "Для подписки необходимо указать: Email, Имя пользователя и время на которое оформляем подписку"

Данный текст можно интерпретировать как условие, что поля не должны быть пустыми.

* Создание подписки с пустым `name` (`test_creating_with_empty_name`)

Предполагается, что нельзя создать подписку с пустым полем `name`.

* Создание подписки с пустым `time` (`test_creating_with_empty_time`)

Предполагается, что нельзя создать подписку с пустым полем `time`.

* Создание подписки с некорректным `email` (`test_creating_with_incorrect_email`)

Предполагается, что нельзя создать подписку с некорректным `email`.

* Создание подписки с некорректным `name` (`test_creating_with_incorrect_name`)

Предполагается, что нельзя создать подписку с некорректным `name`.

* Создание подписки с некорректным `time` (`test_creating_with_incorrect_time`)

Предполагается, что нельзя создать подписку с некорректным `time`.

* Создание подписки с нулевым `time` (`test_creating_with_zero_time`)

Предполагается, что нельзя создать подписку с нулевым `time`.

### Результаты запуска тестов:

![tests-results](https://i.ibb.co/pWwnFP8/2020-05-15-21-08-20.png)

Описание полученных ошибок (вывод `pytest`):

```sh
====================================================================== FAILURES =======================================================================
_________________________________________________________ test_creating_existing_subscription _________________________________________________________

create_correct_subscription = None

    @pytest.mark.creating
    @pytest.mark.negative
    def test_creating_existing_subscription(create_correct_subscription):
        """
        Try to create subscription with existing email
        """
    
        create_subscription(positive)
    
        hc.assert_that(
            actual=send_request(),
            matcher=hc.has_length(1),
>           reason="Subscription with existing email should not be created!"
        )
E       AssertionError: Subscription with existing email should not be created!
E       Expected: an object with length of <1>
E            but: was <[{'email': 'positive@example.com', 'name': 'Positive Name', 'expired_at': '2020-05-16T15:27:46.412000', 'created_at': '2020-05-15T15:27:46.412000', 'id': '5ebeb4f2da48042b70712ac8'}, {'email': 'positive@example.com', 'name': 'Positive Name', 'expired_at': '2020-05-16T15:27:46.402000', 'created_at': '2020-05-15T15:27:46.402000', 'id': '5ebeb4f2da48042b70712ac7'}]> with length of <2>

tests/test/test_negative_creating.py:27: AssertionError
____________________________________________________________ test_creating_with_empty_name ____________________________________________________________

clean = None

    @pytest.mark.creating
    @pytest.mark.negative
    def test_creating_with_empty_name(clean):
        """
        Try to create subscription with empty name
        """
    
        response = create_subscription(empty_name)
    
        hc.assert_that(
            actual=response,
            matcher=hc.has_entries({
                "error": hc.all_of(
                    hc.contains_string("ValidationError"),
                    hc.matches_regexp(r"Invalid.*name")
                )
            }),
>           reason="ValidationError was expected"
        )
E       AssertionError: ValidationError was expected
E       Expected: a dictionary containing {'error': (a string containing 'ValidationError' and a string matching 'Invalid.*name')}
E            but: no 'error' key in <{'id': '5ebeb4f2da48042b70712ac9'}>

tests/test/test_negative_creating.py:80: AssertionError
____________________________________________________________ test_creating_with_empty_time ____________________________________________________________

clean = None

    @pytest.mark.creating
    @pytest.mark.negative
    def test_creating_with_empty_time(clean):
        """
        Try to create subscription with empty time
        """
    
        response = create_subscription(empty_time)
    
        hc.assert_that(
            actual=response,
            matcher=hc.has_entries({
                "error": hc.all_of(
                    hc.contains_string("ValidationError"),
                    hc.matches_regexp(r"Invalid.*time")
                )
            }),
>           reason="ValidationError was expected"
        )
E       AssertionError: ValidationError was expected
E       Expected: a dictionary containing {'error': (a string containing 'ValidationError' and a string matching 'Invalid.*time')}
E            but: no 'error' key in <{'id': '5ebeb4f2da48042b70712aca'}>

tests/test/test_negative_creating.py:112: AssertionError
__________________________________________________________ test_creating_with_incorrect_name __________________________________________________________

clean = None

    @pytest.mark.creating
    @pytest.mark.negative
    def test_creating_with_incorrect_name(clean):
        """
        Try to create subscription with incorrect name
        """
    
        response = create_subscription(incorrect_name)
    
        hc.assert_that(
            actual=response,
            matcher=hc.has_entries({
                "error": hc.all_of(
                    hc.contains_string("ValidationError"),
                    hc.matches_regexp(r"Invalid.*name")
                )
            }),
>           reason="ValidationError was expected"
        )
E       AssertionError: ValidationError was expected
E       Expected: a dictionary containing {'error': (a string containing 'ValidationError' and a string matching 'Invalid.*name')}
E            but: no 'error' key in <{'id': '5ebeb4f2da48042b70712acb'}>

tests/test/test_negative_creating.py:176: AssertionError
__________________________________________________________ test_creating_with_incorrect_time __________________________________________________________

clean = None

    @pytest.mark.creating
    @pytest.mark.negative
    def test_creating_with_incorrect_time(clean):
        """
        Try to create subscription with incorrect time
        """
    
        response = create_subscription(incorrect_time)
    
        hc.assert_that(
            actual=response,
            matcher=hc.has_entries({
                "error": hc.all_of(
                    hc.contains_string("ValidationError"),
                    hc.matches_regexp(r"Invalid.*time")
                )
            }),
>           reason="ValidationError was expected"
        )
E       AssertionError: ValidationError was expected
E       Expected: a dictionary containing {'error': (a string containing 'ValidationError' and a string matching 'Invalid.*time')}
E            but: no 'error' key in <{'id': '5ebeb4f2da48042b70712acc'}>

tests/test/test_negative_creating.py:208: AssertionError
____________________________________________________________ test_creating_with_zero_time _____________________________________________________________

clean = None

    @pytest.mark.creating
    @pytest.mark.negative
    def test_creating_with_zero_time(clean):
        """
        Creating with zero time
        """
    
        response = create_subscription(zero_time)
    
        hc.assert_that(
            actual=response,
            matcher=hc.has_entries({
                "error": hc.all_of(
                    hc.contains_string("ValidationError"),
                    hc.matches_regexp(r"Invalid.*time")
                )
            }),
>           reason="ValidationError was expected"
        )
E       AssertionError: ValidationError was expected
E       Expected: a dictionary containing {'error': (a string containing 'ValidationError' and a string matching 'Invalid.*time')}
E            but: no 'error' key in <{'id': '5ebeb4f2da48042b70712acd'}>

tests/test/test_negative_creating.py:240: AssertionError
=============================================================== short test summary info ===============================================================
FAILED tests/test/test_negative_creating.py::test_creating_existing_subscription - AssertionError: Subscription with existing email should not be cr...
FAILED tests/test/test_negative_creating.py::test_creating_with_empty_name - AssertionError: ValidationError was expected
FAILED tests/test/test_negative_creating.py::test_creating_with_empty_time - AssertionError: ValidationError was expected
FAILED tests/test/test_negative_creating.py::test_creating_with_incorrect_name - AssertionError: ValidationError was expected
FAILED tests/test/test_negative_creating.py::test_creating_with_incorrect_time - AssertionError: ValidationError was expected
FAILED tests/test/test_negative_creating.py::test_creating_with_zero_time - AssertionError: ValidationError was expected
```

Следующие тесты выявили **ошибки**:

* Создание подписки с существующим `email`

При создании двух подписок с одинаковыми данными создаётся две записи вопреки предположению о том, что в таблице не может быть записей с двумя одинаковыми `email`.

* Создание подписки с пустым `name` (`test_creating_with_empty_name`)

Подписка с пустым полем `name` создаётся, несмотря на условие, указанное в баннере страницы.

* Создание подписки с пустым `time` (`test_creating_with_empty_time`)

Подписка с пустым полем `time` создаётся, несмотря на условие, указанное в баннере страницы.

* Создание подписки с некорректным `name` (`test_creating_with_incorrect_name`)

Подписка с некорректным значением `name` создаётся

* Создание подписки с некорректным `time` (`test_creating_with_incorrect_time`)

Подписка с некорректным значением `time` создаётся.

* Создание подписки с нулевым `time` (`test_creating_with_zero_time`)

Подписка с нулевым значением `time` создаётся
