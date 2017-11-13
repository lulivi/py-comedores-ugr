#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Test ComedoresUgrApi class.

Copyright 2017, Luis Liñán (luislivilla@gmail.com)

This program is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, version 3.

This program is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>
"""

# External imports
import unittest
import json

# Local imports
import __init__ as init
from comedores_api import ComedoresUgrApi

assert init


menu_object = None
test_menu_path = None
test_menu = None


# === Clase test ===
class TestComedoresUgrApi(unittest.TestCase):
    """Comedores ugr api test class."""

    def test_load_week_json(self):
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
    global test_menu_path
    global test_menu
    global comedores_ugr_api

    test_menu_path = '../data/test_menu_semanal.json'

    with open(test_menu_path, 'r') as file:
        test_menu = json.loads(file.read())

    menu_object = ComedoresUgrApi()
    menu_object.load_week_json(test_menu_path)


if __name__ == '__main__':
    unittest.main()
