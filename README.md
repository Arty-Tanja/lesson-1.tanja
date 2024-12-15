#Описание работы с проектом
##Запуск тестов для формирования отчёта

Запуск тестов в командной строке:
C:\Users\Tanechka\Desktop\AutoLessons\ProAuto> python -m pytest --alluredir allure-result

где .\ProAuto имя папки; параметр --alluredir задаёт путь к каталогу, в котором будут сохранены результаты тестирования.

##Просмотр сформированных отчётов

Для просмотра сформированных отчётов в командной строке выполнить:

C:\Users\Tanechka\Desktop\AutoLessons\ProAuto> allure serve allure-result
