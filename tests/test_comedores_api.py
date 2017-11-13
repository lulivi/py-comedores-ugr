#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
rest api reminder test python module.

Tests functions from the reminder rest api.
"""

# External imports
import unittest
import json

# Local imports
import __init__ as init
from comedores_api import ComedoresApi
assert init

mock_menu_path = None
mock_menu = None


# === Clase test ===
class TestComedoresUgrApi(unittest.TestCase):
    """Reminder api rest test class."""

    def test_get_menu(self):
        pass

    def test_lunes(self):
        pass

    def test_martes(self):
        pass

    def test_miercoles(self):
        pass

    def test_jueves(self):
        pass

    def test_viernes(self):
        pass

    def test_sabado(self):
        pass

    def test_semana(self):
        pass


def setUpModule():
    """Set up Module method."""
    global mock_menu_path
    global mock_menu

    mock_menu_path = '../data/mock_menu.json'

    with open(mock_menu_path, 'r') as file:
        mock_menu = json.loads(file.read())


if __name__ == '__main__':
    unittest.main()
