import pytest

from src.phone import Phone
from src.item import Item


phone1 = Phone('Nokia', 14999, 4, 2)
phone2 = Phone('Oppo', 9999, 1, 1)
assert repr(phone1) == 'Phone(\'Nokia\', 14999, 4, 2)'
assert phone1 + phone2 == 5
