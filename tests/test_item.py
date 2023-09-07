"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import csv

from src.item import Item, InstantiateCSVError
from src.phone import Phone

class TestItem:

    @pytest.fixture
    def item(self):
        return Item('MI', 10000, 3)

    def test_calculate_total_price(self, item):
        assert item.calculate_total_price() == 30000
    def test_apply_discount(self, item):
        item.pay_rate = 0.5
        item.apply_discount()
        assert item.price == 5000

    def test_name(self, item):
        item.name = 'Смартфон'
        assert item.name == 'Смартфон'
        item.name = '1234567890123'
        assert item.name == '1234567890'

    @staticmethod
    def test_string_to_number():
        assert Item.string_to_number('10.0') == 10
        assert Item.string_to_number('10.9') == 10

    item1 = Item("Mac", 100000, 3)
    item2 = Item("DEXP", 15000, 10)
    test_phone = Phone('Nokia', 14999, 4, 2)
    assert repr(item1) == "Item('Mac', 100000, 3)"
    assert str(item1) == 'Mac'
    assert item1 + item2 == 13

    def test_instantiate_from_csv_error():
        with pytest.raises(FileNotFoundError):
            Item.instantiate_from_csv()

    def test_instantiate_from_csv_damaged():
        with pytest.raises(InstantiateCSVError):
            Item.instantiate_from_csv()

