""" Comparing `array.array` with `list` for some common operations, including:
    append, concatenation, in-place concatenation, contain, count, remove, extend,
    get, index, insert, repleated concatenation, im-place repeated concatenation,
    reversed repeated concatenation, pop, remove, reverse."""

import random, array

# append
li = []
arr = array.array('d', [])

for i in range(10000):
    li.append(random.random())

for i in range(10000):
    arr.append(random.random())


