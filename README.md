<h1>Тестовое задание - телефонный справочник</h1>

<h3>Запуск:</h3>

1. Вывод записей из справочника: `python -m src.presentation.main read`

2. Добавление новой записи в справочник: `python -m src.presentation.main create`

3. Обновление записи по номеру раб. телефона: `python -m src.presentation.main update`

4. Поиск записи по одной или нескольким характеристикам: `python -m src.presentation.main find`

<hr>

По умолчанию используется файловое хранилище в формате json. Для изменения формата необходимо изменить зависимость
`json_storage` на `csv_storage` в файле `src.presentation.di.services`

<hr>
