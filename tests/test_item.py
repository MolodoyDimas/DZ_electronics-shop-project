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