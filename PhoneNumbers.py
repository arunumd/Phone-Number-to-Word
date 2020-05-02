#!/usr/bin/env python3
import pprint
import enchant
import time


class AlphaNumeric:
    def __init__(self, phone_number='9883642228'):
        self.phone_number = phone_number
        self.num_alpha = {"1": ["NIL"], "2": ["A", "B", "C"],
                          "3": ["D", "E", "F"], "4": ["G", "H", "I"],
                          "5": ["J", "K", "L"], "6": ["M", "N", "O"],
                          "7": ["P", "Q", "R", "S"], "8": ["T", "U", "V"],
                          "9": ["W", "X", "Y", "Z"], "0": ["NIL"]}
        self.alpha_num = {"A": "2", "B": "2", "C": "2", "D": "3", "E": "3", "F": "3",
                          "G": "4", "H": "4", "I": "4", "J": "5", "K": "5", "L": "5",
                          "M": "6", "N": "6", "O": "6", "P": "7", "Q": "7", "R": "7",
                          "S": "7", "T": "8", "U": "8", "V": "8", "W": "9", "X": "9",
                          "Y": "9", "Z": "9"}
        self.comb_dict = {}
        self.valid_numbers = {}
        self.words = enchant.Dict("en_US")

    def find_permutations_num_alpha(self):
        counter = 0
        interim_combs = []
        if self.num_alpha[self.phone_number[0]] is "NIL":
            interim_combs.append(self.phone_number[0])
        else:
            for each_alpha in self.num_alpha[self.phone_number[0]]:
                interim_combs.append(each_alpha)
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
        return self.comb_dict[9]

    def convert_alpha_to_num(self):
        converted_num = ""
        for each_char in self.phone_number:
            if each_char.isalpha():
                converted_num += self.alpha_num[each_char]
            else:
                converted_num += each_char
        return converted_num

    def accumulate_valid_numbers(self, num_range=(6, 10)):
        temp_set = set()
        for each_word in self.comb_dict[9]:
            temp_set.add(str(each_word[num_range[0]: num_range[1]]).lower())
        unique_set = set()
        for unique_name in temp_set:
            if self.words.check(unique_name):
                unique_set.add(self.phone_number[:num_range[0]] + unique_name.upper() +
                               self.phone_number[num_range[1]:])
        if unique_set == set():
            unique_set.add("NIL")
        self.valid_numbers[num_range] = unique_set

    def print_all_combinations(self):
        pprint.pprint(self.valid_numbers)

    def get_all_num_to_text(self):
        return self.valid_numbers


if "__main__":
    start = time.time()
    NumAlpha = AlphaNumeric()
    NumAlpha.find_permutations_num_alpha()
    NumAlpha.convert_alpha_to_num()
    NumAlpha.accumulate_valid_numbers()
    end = time.time()
    NumAlpha.print_all_combinations()
    print("Total time taken : ", end - start)
