#!/usr/bin/env python3

import re
import time
import pprint
import logging
import argparse
import threading
from itertools import combinations

from PhoneNumbers import AlphaNumeric

parser = argparse.ArgumentParser(description='A tool for conversion between Phone Number and Text')
parser.add_argument('--mode', action="store", dest="mode",
                    default="num_to_text", help="Specify the action here.\n" "Example : \n"
                                                "num_to_text\n" "text_to_num\n" "num_to_all_text\n")
parser.add_argument('--log', action="store", dest="log", default="output.txt", help="Specify the action here.")
options = parser.parse_args()


def convert_to_alpha_num(number='984ABC&/]?786'):
    return ''.join([c for c in number if c.isalnum()])


def is_all_num(number='989592KJABGV8'):
    return number.isdigit()


def check_format(number='1989592KJAB'):
    return number[0] == '1' and len(number) == 11


def fracture_number(number='989592KJAB'):
    length = len(number) + 1
    return [[x, y] for x, y in combinations(range(length), r=2)]


def get_good_prospects(combs=([1, 2], [5, 6])):
    return [[num[0], num[1]] for num in combs if num[1] - num[0] > 2]


if '__main__':
    print(convert_to_alpha_num())
    print(check_format())
    print("The number of combinations is : ", len(fracture_number()))
    print("The no. of workers is : ", len(get_good_prospects(fracture_number())))
