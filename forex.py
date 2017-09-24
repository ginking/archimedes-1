# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes

c = CurrencyRates()
d = CurrencyCodes()

print(c.convert('USD', 'INR', 10))
print d.get_symbol('INR')