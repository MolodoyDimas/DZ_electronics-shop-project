"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

class TestItem:

    @pytest.fixture
    def item(self):
        return Item('молоко', 100, 3)

    def test_calculate_total_price(self, item):
        assert item.calculate_total_price() == 300
    def test_apply_discount(self, item):
        item.pay_rate = 0.5
        item.apply_discount()
        assert item.price == 50

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
    assert repr(item1) == "Item('Mac', 100000, 3)"
    assert str(item1) == 'Mac'