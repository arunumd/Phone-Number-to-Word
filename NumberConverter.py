#!/usr/bin/env python3
import re
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


def convert_num_to_words(number='19883642228'):
    """
    Description
    -----------
    Function for converting an input all-numeric phone number into a list of possible alpha-numeric
    phone numbers. The process is done by utilizing another function(find_permutations_num_alpha()) which
    first generates a list of all possible alpha-numeric sentences from the input phone number. Later, this
    function sets-off a number of worker threads that go and crawl on all the generated alpha-numeric sentences
    and verify whether the sub-string withing the slice range is a valid English word. If it is a valid word,
    then the output is packed by patching the missing segments from the input phone number.
    :param number: Input phone number as a string
    :return: A list of all possible phone numbers with meaningful English words
    """
    display_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=display_format, level=logging.INFO, datefmt="%H:%M:%S")
    NumAlpha = AlphaNumeric(number)
    logging.info("Initiated all combinations search")
    NumAlpha.find_permutations_num_alpha()
    logging.info("Finished all combinations search")
    num_combs = get_good_prospects(fracture_number(number))
    logging.info("Initiated meaningful words search")
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(num_combs)) as executor:
        executor.map(NumAlpha.accumulate_valid_numbers, num_combs)
        logging.info("Total no of workers, with divide and conquer : %d", threading.active_count())
    logging.info("Finished meaningful words search")
    return NumAlpha.get_all_num_to_text()


def all_wordifications(number='19883642228'):
    """
    Description
    -----------
    Function for creating output phone numbers with meaningful English words. This function also takes care of the
    aesthetic appeal requirements of the generated phone numbers. Necessary hyphen (-) symbols are added at
    appropriate places in the output phone numbers
    :param number: Input phone number as a string
    :return: Output phone numbers in the expected format
    """
    number = convert_to_alpha_num(number)
    if check_format(number) and is_all_num(number):
        all_words = convert_num_to_words(number)
        concat_nums = set()
        for words in all_words:
            concat_nums = concat_nums.union(words)
        us_format = []
        pattern = r"([A-Z]-(?=[A-Z]))|([A-Z](?=[0-9])|[0-9](?=[A-Z]))"
        for num in concat_nums:
            clean_num = (num[0] + "-" + num[1:4] + "-" + num[4:7] + "-" + num[7:])
            us_format.append(re.sub(pattern, lambda x: x.group(1)[:-1] if x.group(1) else x.group(2) + "-", clean_num))
        return us_format
    else:
        return ["Invalid input"]


def number_to_words(number='19883642228'):
    """
    Description
    -----------
    Function for returning exactly one transformation of an input US phone number into an output phone number
    with meaningful English words. Since the probability of a random generated sequence being a meaningful
    English word is quite low, this function first calls the all_wordifications() function to generate all
    possible meaningful words and then return a random output phone number from the list
    :param number: Input phone number as a string
    :return: Exactly one output transformation of input phone number, which has a meaningful English word
    """
    num = all_wordifications(number)
    if num[0] != "Invalid input":
        return [num[random.randint(0, len(num) - 1)]]
    else:
        return ["Invalid input"]


def words_to_number(number="1987ABC7652"):
    """
    Description
    -----------
    A simple function to convert an input alpha-numeric US phone number into an all-numeric US phone number. The
    function does some sanity checks for input format compliance and then uses another function that changes individual
    alphabets into numbers by referring to a lookup table
    :param number: Input alpha-numeric phone number
    :return: An all-numeric US phone number
    """
    number = convert_to_alpha_num(number)
    if check_format(number):
        NumAlpha = AlphaNumeric(number)
        phone_num = NumAlpha.convert_alpha_to_num()
        return [phone_num[0] + "-" + phone_num[1:4] + "-" + phone_num[4:7] + "-" + phone_num[7:]]
    else:
        return ["Invalid input"]
