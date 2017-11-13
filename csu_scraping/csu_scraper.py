"""
Perform scraping to the scu web page.

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


class ScuScraper(object):
    """Represent a scraper to get information from scu.ugr.es."""

    def __init__(self):
        """Initialize by default value all variables."""
        self._PAGE_URL = 'http://scu.ugr.es/'
        self.__week_menu = dict()

    def get_week_menu(self):
        pass

    def save_week_menu(self):
        pass

    def update_week_menu(self):
        pass
