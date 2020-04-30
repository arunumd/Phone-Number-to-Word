#!/usr/bin/env python3


class AlphaNumeric:
    def __init__(self, lib_location='words.txt'):
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
        with open(lib_location, 'r') as lib_file:
            self.words = lib_file.read().splitlines()

    def find_permutations_num_alpha(self, number='9880042436'):
        counter = 0
        interim_combs = []
        if self.num_alpha[number[0]] is "NIL":
            interim_combs.append(number[0])
        else:
            for each_alpha in self.num_alpha[number[0][:]]:
                interim_combs.append(each_alpha)
        self.comb_dict[counter] = tuple(interim_combs)
        while counter < len(number) - 1:
            interim_combs.clear()
            temp_combs = list(self.comb_dict[counter])
            for each_comb in temp_combs:
                next_combs = self.num_alpha[number[counter + 1]]
                if number[counter + 1] == "7" or number[counter + 1] == "9":
                    interim_combs.extend((each_comb + next_combs[0], each_comb + next_combs[1],
                                          each_comb + next_combs[2], each_comb + next_combs[3]))
                elif number[counter + 1] == "1" or number[counter + 1] == "0":
                    interim_combs.append(each_comb + number[counter + 1])
                else:
                    interim_combs.extend((each_comb + next_combs[0], each_comb + next_combs[1],
                                          each_comb + next_combs[2]))
                self.comb_dict[counter + 1] = tuple(interim_combs)
            counter += 1
        return self.comb_dict[9]

    def convert_alpha_to_num(self, number='985AHT7782'):
        converted_num = ""
        for each_char in number:
            if each_char.isalpha():
                converted_num += self.alpha_num[each_char]
            else:
                converted_num += each_char
        return converted_num


if "__main__":
    NumAlpha = AlphaNumeric()
    print(NumAlpha.find_permutations_num_alpha())
    print(NumAlpha.convert_alpha_to_num())
