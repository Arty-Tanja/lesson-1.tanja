from address import Address
from mailing import Mailing

from_address = Address('393570', 'Tambov', 'Oktyabrskaya', '5', '345')
to_address = Address('125599', 'Moscow', 'Izhorskaya', '6', '444')
mailing1 = Mailing(from_address, to_address, '350', '12998576589')

print(
    f'Отправление {mailing1.track} из {mailing1.from_address}'
    f' в {mailing1.to_address}.'
    f'Стоимость {mailing1.cost} рублей.'
)
