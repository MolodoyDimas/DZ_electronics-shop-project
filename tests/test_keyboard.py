from src.keyboard import Keyboard, MixinLanguage
from src.item import Item
import pytest

class TestKeyboard:

    keyb = Keyboard('MI', 5000, 2)
    keyb.change_lang()
    assert keyb.language == 'RU'
    keyb.change_lang()
    assert keyb.language == 'EN'