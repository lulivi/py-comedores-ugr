"""Help tests to find modules to test."""

import sys
import os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../py_comedores_ugr')
sys.path.insert(0, myPath + '/../csu_scraping')
