"""Compare memory usage between `list` and `array.array`"""

from collections import namedtuple
import random, string, array, sys, csv

MemUsage = namedtuple('MemUsage', ['case', 'list', 'array'])
memusages = []

for power in range(7):
    elem_len = 10 ** power
    c_list = [ord(random.choice(string.ascii_letters)) for i in range(elem_len)]
    c_arr = array.array('b', c_list)
    memusages.append(MemUsage(str(elem_len) + ' characters', sys.getsizeof(c_list), sys.getsizeof(c_arr)))

    int_list = [random.randrange(10) for i in range(elem_len)]
    int_arr = array.array('i', int_list)
    memusages.append(MemUsage(str(elem_len) + ' integers', sys.getsizeof(int_list), sys.getsizeof(int_arr)))

    double_list = [random.random() for i in range(elem_len)]
    double_arr = array.array('d', double_list)
    memusages.append(MemUsage(str(elem_len) + ' doubles', sys.getsizeof(double_list), sys.getsizeof(double_arr)))
    
with open('memory-usage.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Case', 'List', 'Array'])
    for memusage in memusages:
        writer.writerow([memusage.case, memusage.list, memusage.array])
