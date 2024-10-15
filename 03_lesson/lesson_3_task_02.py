from smarthpone import Smartphone

catalog = [
    Smartphone('Honor', 'P20Light', '+79251987643'),
    Smartphone('Samsung', 'A55', '+79997008504'),
    Smartphone('Xiaomi', 'Note13Pro', '+79237008705'),
    Smartphone('Vivo', 'V30E', '+79851154312'),
    Smartphone('Tecno', 'SparkGo', '+79153329812')
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} . {smartphone.phone_number}")