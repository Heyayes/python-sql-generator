## Генератор случайных сущностей

Целью скрипта является генерация большого числа случайных сущностей заказов. Настоящий скрипт создаёт файл с запросом sql, который является специфичным для другого [проекта].

Находясь в папке проекта нужно исполнить
````bash
user@host$ python generator.py 

````

* В папках boys и girls содержаться файлы со списками имен, фамилий и отчеств
* Файл city содержит список городов
* Файл street содержит список улиц

Генерация записей полей происходит с помощью функций:
* ADRESS = get_address()
* RECIPIENT = get_person() - Случайная личность. Женщина или мужчина
* PHONE = phonegen() - Случайный телефон формата 79042881111
* DELIVERYTYPE_ID = getRand(delivery_count)
* ORDERSTATE = getordestate() - Случайны статус
* SUMM = ri(1000,3000) - Сумма от 1000 до 3000
* HAVEPATCH = getTrueOrFalse()
* ORDER_DATE = get_date() - Случайная дата от 01.01.2017 до настоящей даты
* CANVAS_ID = getRand(canvas_count)
* PAYED = getTrueOrFalse()
* SACHE_ID = getRand(saches_count)
* COVER_ID = getRand(cover_count)

Скрипт был создан из-за неудачного поиска генераторов сущностей для spring boot.
Если вы знаете как можно найти генератор, то буду признателен, если поделитесь

[проекта]: https://github.com/Heyayes/sleepAndTrip
