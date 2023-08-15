import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        #self.all.append({'name': self.__name, 'price': self.price, 'quantity': self.quantity})

    def __str__(self):
        return self.__name

    def __repr__(self):
        return f'{self.__class__.__name__}(\'{self.__name}\', {self.price}, {self.quantity})'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return float(self.price * self.quantity)

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.pay_rate * self.price

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        with open('../src/items.csv') as file:
            file = csv.DictReader(file)
            for x in file:
                a = cls(x['name'], float(x['price']), int(x['quantity']))
                cls.all.append(a)
            return cls.all


    @staticmethod
    def string_to_number(number):
        return int(float(number))

#Item.instantiate_from_csv()
#print(Item.all)
#print(len(Item.all))