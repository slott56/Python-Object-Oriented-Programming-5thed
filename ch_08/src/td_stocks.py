"""
Python 3 Object-Oriented Programming

Chapter 8. Python Data Structures
"""

test_syntax = """
>>> s_1 = {
...     'symbol': 'GOOG',
...     'current': 1245.21,
...     'range': (1252.64, 1245.18)
... }
>>> s_2 = dict(
...     symbol='GOOG',
...     current=1245.21,
...     range=(1252.64, 1245.18)
... )

"""

from typing import TypedDict

class Range(TypedDict):
    low: float
    high: float

class Stock(TypedDict):
    symbol: str
    current: float
    range: Range

test_td_syntax = """
>>> s_td = Stock(
...     symbol='GOOG',
...     current=1245.21,
...     range=Range(low=1252.64, high=1245.18)
... )

"""

import datetime
from typing import TypedDict, NotRequired

class StockN(TypedDict):
    symbol: str
    name: NotRequired[str]
    current: float
    range: Range
    date: NotRequired[datetime.date]

test_not_required = """
>>> s = StockN(symbol="RIMM", name=None, current=123.45,
...     range=Range(low=1, high=10))
>>> s
{'symbol': 'RIMM', 'name': None, 'current': 123.45, 'range': {'low': 1, 'high': 10}}
"""

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
