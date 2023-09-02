from src.item import Item


class MixinLanguage:

    LANGUAGE = 'EN'

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = self.LANGUAGE

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'
        return self


class Keyboard(MixinLanguage, Item):
    '''Класс для клавиатуры'''

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        pass
