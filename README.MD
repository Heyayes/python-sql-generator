Целью скрипта является генерация большого числа случайных сущностей заказов

Настоящий скрипт создаёт файл с запросом sql, который является специфичным для моего другого проекта.

В папках boys и girls содержаться файлы со списками имен, фамилий и отчеств
Файл city содержит список городов русских
Файл street содержит список улиц


Генерация записей полей происходит с помощью функций:
*ADRESS = get_address()
*RECIPIENT = get_person()
*PHONE = phonegen()
*DELIVERYTYPE_ID = getRand(delivery_count)
*ORDERSTATE = getordestate()
*SUMM = ri(1000,3000)
*HAVEPATCH = getTrueOrFalse()
*ORDER_DATE = get_date()
*CANVAS_ID = getRand(canvas_count)
*PAYED = getTrueOrFalse()
*SACHE_ID = getRand(saches_count)
*COVER_ID = getRand(cover_count)

Скрипт был создан из-за неудачного поиска генераторов сущностей для spring boot.
Если вы знаете как можно найти генератор, то буду признателен, если поделитесь
