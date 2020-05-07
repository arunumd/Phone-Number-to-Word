#!/usr/bin/env python3
import re
import time
import random
import logging
import threading
import concurrent.futures
from itertools import combinations

from PhoneNumbers import AlphaNumeric


def convert_to_alpha_num(number='984ABC&/]?786'):
    """
    Description
    -----------
    Helper function for removing characters that are neither alphabets nor numbers, from a sequence
    :param number: Input sequence as a string
    :return: Sequence with only digits and alphabets
    """
    return ''.join([c for c in number if c.isalnum()])


def is_all_num(number='989592KJABGV8'):
    """
    Description
    -----------
    Trivial function to check if an input string contains all numbers
    :param number: Input phone number as a string
    :return: True if all numbers, False if not
    """
    return number.isdigit()


def check_format(number='1989592KJAB'):
    """
    Description
    -----------
    Function to check format compliance of US phone numbers, namely the length should be exactly 11 digits, and
    the first digit must be with 1
    :param number: Input phone number as a string
    :return: True if valid format, false if not
    """
    return number[0] == '1' and len(number) == 11


def fracture_number(number='1989592KJAB'):
    length = len(number)
    """
    Description
    -----------
    This function returns a list of slicing indices for generating sub-strings from the generated phone numbers, 
    which will then be used to search through an English dictionary.
    :param number: Input phone number as a string
    :return: A list of slice indices of the format ((start1, end1), (start2, end2), ....)
    """
    return ((x, y) for x, y in combinations(range(length), r=2))


def get_good_prospects(combs=([1, 2], [5, 6])):
    """
    Description
    -----------
    Words with just one or two letters are usually articles, prepositions, etc. Since these are not words with a
    significant meaning, they will be omitted. Hence, this function returns a curated slice list where the distance
    between the start point and end point of slice is at least 2 units
    :param combs: Raw list of indices for slicing the input phone number
    :return A curated list where the difference between end and start are at least 2 units
    """
    return [(num[0], num[1]) for num in combs if num[1] - num[0] > 2]

