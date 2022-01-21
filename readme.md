# Сортировки

Пузырьковая сортировка - bubble_sort.py

Сортировка выбором - choice_sort.py

Сортировка вставками - insert_sort.py

Сортировка слиянием - merge_sort.py

Быстрая сортировка - quick_sort_tony_hoar.py

# Скобочная последовательность

Необходимо решить задачу о скобочной последовательности, предлагаемую на собеседовании, с помощью рекурсии и стека. 
{{([([])])}}(){[]}
{{([])}}
{}

### Решения
в файле brackets_task.py

# Алерты

Сервис мониторинга следит за работой системы и выявляет критичесакие показатели утилизации дискового простраранста, CPU, количества скопившихся заданий в очереди и т.д.  Также система уведомляет разработчиков о достижении критических значений. Если на алерт не получено подтверждение о прочтении от разработчика, то алерт будет прислан еще раз.  Если на одно время запланировано срабатывание двух алертов, то приходит только одно. Для простоты вычислений все алерты срабатывают в целочисленные моменты времени. Известно, что разработчик Вася получает уведомления от разных метрик мониторинга и при накоплении N уведомлений прожимает кнопку о прочтении всех накопившихся сразу. 

Первая строка содержит следующие числа: 
- количество задач, на которые настроены алерты. 
- интервал, через который алерт отправляется повторно. 
- число N, количество накопленных алертов. 
Вторая строка содержит время, с которого алерт начал отправляться, для каждой задачи. 

Необходимо определить время, когда Вася прожмет кнопку о прочтении всех алертов. 

Примечание: все значения больше или равны 1 и принаджелат множеству целых чисел. 

Пример входных данных: 

6 5 10
1 2 3 4 5 6

Вывод: 10

5 7 12
5 22 17 13 8

Вывод: 27

Пример: разберем входные данные первого примера. Дано 6 задач, которые начинают отправлять уведомления в следующие временные единицы 1 2 3 4 5 6. Повтор уведомления возможен через единицу 5. Алерты могут звонить так:

1. 1 6 11 16 21 26 31 ...
2. 2 7 12 17 22 27 32 ...
3. 3  8 13 18 23 28 33 ...
4. 4 9 14 19 24 29 34 ...
5. 5 10 15 20 25 30 35 ...
6. 6 11 16 21 26 31 36 ...

Нам нужно определить последовательность срабатывания алертов и вывесли время 10го алерта. Получаем: 1 2 3 4 5 6 (вторую 6 убираем, так как известно, что два алерта, звонящие в одно и тоже время объединяются) 7 8 9 10

#Решение
в файле queue_task.py
