#!/usr/bin/env python3

"""
Helper script to find merchants close to one another.
"""

from fuzzywuzzy import fuzz
from itertools import combinations
from subprocess import check_output

# tuples to exclude as valid
valid = [
    ('Proper Grounds', 'Higher Grounds'),
]

merchants = check_output(['bean-query', '-q', 'mwt.beancount', 'select distinct(payee)']).decode('utf-8')
merchants = [a.strip() for a in merchants.splitlines()]

for pair in combinations(merchants, 2):
    ratio = fuzz.ratio(*pair)
    if ratio > 70 and pair not in valid:
print("'{}' is close to '{}'".format(*pair))
