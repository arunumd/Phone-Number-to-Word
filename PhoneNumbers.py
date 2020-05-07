#!/usr/bin/env python3
import enchant
from collections import deque


class AlphaNumeric:
    def __init__(self, phone_number='9883642228'):
        """
        Class initializer function which sets up the basic infrastructure for the member functions like:
        alphabet-number lookup and number-alphabet lookup tables. This function also imports a standard
        English dictionary for valid words verification process
        :param phone_number: Input phone number for processing by the member functions
        """
        self.phone_number = phone_number
        self.num_alpha = {"1": ["NIL"], "2": ["A", "B", "C"],
                          "3": ["D", "E", "F"], "4": ["G", "H", "I"],
                          "5": ["J", "K", "L"], "6": ["M", "N", "O"],
                          "7": ["P", "Q", "R", "S"], "8": ["T", "U", "V"],
                          "9": ["W", "X", "Y", "Z"], "0": ["NIL"]}
        self.alpha_num = {"A": "2", "B": "2", "C": "2", "D": "3", "E": "3",
                          "F": "3", "G": "4", "H": "4", "I": "4", "J": "5",
                          "K": "5", "L": "5", "M": "6", "N": "6", "O": "6",
                          "P": "7", "Q": "7", "R": "7", "S": "7", "T": "8",
                          "U": "8", "V": "8", "W": "9", "X": "9", "Y": "9", "Z": "9"}
        self.comb_dict = {}
        self.valid_numbers = deque([], 60)
        self.words = enchant.Dict("en_US")

    def find_permutations_num_alpha(self):
        """
        Description
        -----------
        Function to convert an input number into all possible strings using the keypad combinations for
        individual digits. This method uses dynamic programming (DP) to recursively solve sub-problems of
        increasing number of digits. The results of the previous sub-problem is used as input for the next
        sub-problem higher up in the hierarchy level. The results of every sub-problem are stored in a dictionary
        """
        counter = 0
        interim_combs = [self.phone_number[0]]
        self.comb_dict[counter] = tuple(interim_combs)
        while counter < len(self.phone_number) - 1:
            interim_combs.clear()
            temp_combs = list(self.comb_dict[counter])
            for each_comb in temp_combs:
                next_combs = self.num_alpha[self.phone_number[counter + 1]]
                if self.phone_number[counter + 1] == "7" or self.phone_number[counter + 1] == "9":
                    interim_combs.extend((each_comb + next_combs[0], each_comb + next_combs[1],
                                          each_comb + next_combs[2], each_comb + next_combs[3]))
                elif self.phone_number[counter + 1] == "1" or self.phone_number[counter + 1] == "0":
                    interim_combs.append(each_comb + self.phone_number[counter + 1])
                else:
                    interim_combs.extend((each_comb + next_combs[0], each_comb + next_combs[1],
                                          each_comb + next_combs[2]))
                self.comb_dict[counter + 1] = tuple(interim_combs)
            counter += 1

    def convert_alpha_to_num(self):
        """
        Description
        -----------
        A simple function which uses a lookup dictionary to find the corresponding numbers for given alphabets
        in a phone number. The numbers are replaced with the alphabets and returned as an output string
        :return: Phone number in numerical format
        """
        converted_num = ""
        for each_char in self.phone_number:
            if each_char.isalpha():
                converted_num += self.alpha_num[each_char]
            else:
                converted_num += each_char
        return converted_num

    def accumulate_valid_numbers(self, num_range=(6, 10)):
        """
        Description
        -----------
        Function which iteratively slices the string between the given index range 'num_range' and checks whether
        the sliced string is a valid English word by looking up in an English dictionary. If the word is a valid
        English word, then the whole phone number is packed with the missing segments and returned
        :param num_range: index for slicing the string into a sub-string for valid word search
        :return: Converted phone numbers which have valid English words
        """
        temp_set = set()
        for each_word in self.comb_dict[9]:
            temp_set.add(str(each_word[num_range[0]: num_range[1]]).lower())
        unique_set = set()
        for unique_name in temp_set:
            if self.words.check(unique_name):
                unique_set.add(self.phone_number[:num_range[0]] + unique_name.upper() +
                               self.phone_number[num_range[1]:])
        if unique_set != set():
            self.valid_numbers.append(unique_set)

    def print_all_combinations(self):
        """
        Description
        -----------
        Trivial function to print all possible phone numbers with valid English words
        """
        print(self.valid_numbers)

    def get_all_num_to_text(self):
        """
        Description
        -----------
        Trivial getter function for retrieving all possible phone numbers with valid English words
        :return: All possible phone numbers with valid English words
        """
        return self.valid_numbers
