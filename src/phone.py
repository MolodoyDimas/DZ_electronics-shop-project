from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        if number_of_sim > 0:
            self.number_of_sim = number_of_sim
        else:
            # Ошибка почему-то не вылезает
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self):
        return f'{self.__class__.__name__}(\'{self.name}\', {self.price}, {self.quantity}, {self.number_of_sim})'

    def __add__(self, other):
        if isinstance(other, Phone):
            return self.quantity + other.quantity
