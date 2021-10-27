#!/usr/bin/python3

import os
import gzip
import csv
import bitcoin
import ethereum
import rlp
from ethereum import transactions
import sqlite3
import sys

value_distribution = [0, 0, 0, 0, 0, 0, 0, 0, 0]
fee_distribution = [0, 0, 0, 0, 0, 0, 0, 0, 0]
gas_used_distribution = [0, 0, 0, 0, 0, 0, 0, 0, 0]

count = 0

csv.field_size_limit(sys.maxsize)

sample = os.listdir("./sample")

for file in sorted(sample):
    print('Processing ' + file)
    with gzip.open('./sample/'+file, 'rt') as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if not row[5] in ['synthetic_coinbase', 'type']:
                # Take the first digit of the value
                value_first_digit = int(row[9][0])
                if value_first_digit != 0:
                    count += 1
                    value_distribution[value_first_digit-1] = value_distribution[value_first_digit-1] + 1

                    fee_first_digit = int(row[13][0])
                    if fee_first_digit != 0:
                        fee_distribution[fee_first_digit-1] = fee_distribution[fee_first_digit-1] + 1
                    else:
                        print("fee is 0 ?")

                    gas_used_first_digit = int(row[15][0])
                    if gas_used_first_digit != 0:
                        gas_used_distribution[gas_used_first_digit-1] = gas_used_distribution[gas_used_first_digit-1] + 1
                    else:
                        print("gas used is 0 ?")



print("\n\n\nTotal count : {}".format(count))

print("""
Transaction `value` first digit distribution

    1 : {} ({}%)
    2 : {} ({}%)
    3 : {} ({}%)
    4 : {} ({}%)
    5 : {} ({}%)
    6 : {} ({}%)
    7 : {} ({}%)
    8 : {} ({}%)
    9 : {} ({}%)

""".format(
    value_distribution[0], round(value_distribution[0]/count * 100, 2),
    value_distribution[1], round(value_distribution[1]/count * 100, 2),
    value_distribution[2], round(value_distribution[2]/count * 100, 2),
    value_distribution[3], round(value_distribution[3]/count * 100, 2),
    value_distribution[4], round(value_distribution[4]/count * 100, 2),
    value_distribution[5], round(value_distribution[5]/count * 100, 2),
    value_distribution[6], round(value_distribution[6]/count * 100, 2),
    value_distribution[7], round(value_distribution[7]/count * 100, 2),
    value_distribution[8], round(value_distribution[8]/count * 100, 2)
))

print("""
Transaction `fee` first digit distribution

    1 : {} ({}%)
    2 : {} ({}%)
    3 : {} ({}%)
    4 : {} ({}%)
    5 : {} ({}%)
    6 : {} ({}%)
    7 : {} ({}%)
    8 : {} ({}%)
    9 : {} ({}%)

""".format(
    fee_distribution[0], round(fee_distribution[0]/count * 100, 2),
    fee_distribution[1], round(fee_distribution[1]/count * 100, 2),
    fee_distribution[2], round(fee_distribution[2]/count * 100, 2),
    fee_distribution[3], round(fee_distribution[3]/count * 100, 2),
    fee_distribution[4], round(fee_distribution[4]/count * 100, 2),
    fee_distribution[5], round(fee_distribution[5]/count * 100, 2),
    fee_distribution[6], round(fee_distribution[6]/count * 100, 2),
    fee_distribution[7], round(fee_distribution[7]/count * 100, 2),
    fee_distribution[8], round(fee_distribution[8]/count * 100, 2)
))

print("""
Transaction `gas_used` first digit distribution

    1 : {} ({}%)
    2 : {} ({}%)
    3 : {} ({}%)
    4 : {} ({}%)
    5 : {} ({}%)
    6 : {} ({}%)
    7 : {} ({}%)
    8 : {} ({}%)
    9 : {} ({}%)

""".format(
    gas_used_distribution[0], round(gas_used_distribution[0]/count * 100, 2),
    gas_used_distribution[1], round(gas_used_distribution[1]/count * 100, 2),
    gas_used_distribution[2], round(gas_used_distribution[2]/count * 100, 2),
    gas_used_distribution[3], round(gas_used_distribution[3]/count * 100, 2),
    gas_used_distribution[4], round(gas_used_distribution[4]/count * 100, 2),
    gas_used_distribution[5], round(gas_used_distribution[5]/count * 100, 2),
    gas_used_distribution[6], round(gas_used_distribution[6]/count * 100, 2),
    gas_used_distribution[7], round(gas_used_distribution[7]/count * 100, 2),
    gas_used_distribution[8], round(gas_used_distribution[8]/count * 100, 2)
))