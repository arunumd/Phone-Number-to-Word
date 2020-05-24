[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# Phone-Number-to-Word
This repository contains simple functions for conversion between phone numbers and alpha numeric encoding. The encoding comprises of a combination of meaningful a English word and numbers. The algorithm first generates all permutations and combinations of words irrespective of whether or not they may be meaningful words. The words generation is done using Dynamic Programming (DP) algorithm, wherein a whole input phone number is converted into many sequences of all possible permutations and combinations first. Later, the generated sequences are fractured into all possible subsets of words. Later,the generated subset of words are filtered by cross checking with an English dictionary, by multiple Python threads. Finally, only those subset of words which are present in the dictionary are retained and the new phone number is reconstructed by patching up for the remaining segments from the input phone number.

The conversion from alpha-numeric phone number to all numerics is done very easily, by looking up at an alphabets to numbers mapping table.

## About the Author
Arun Kumar Devarajulu is a Robotics Software developer with interests in Computer Vision, Machine Learning, and Motion Planning. 
He is an *M. Eng Robotics* graduate from the *University of Maryland, College Park*.

## License
This project is released under the [MIT License](LICENSE)

## About the project
This project is related to converting phone numbers into words and vice versa. To be more specific, all phone
devices (mobile phones and landlines) come with alphabets corresponding to numbers. For instance, the alphabets `A, B, C`
correspond to the number `2`. Similarly the alphabets `P, Q, R, S` correspond to the number `7`. 

Thus if we are given a number `72227727`, there could be many ways we can generate words from this sequence.
The following are some possibilities :
- `PBACRQAS`
- `QCABSPCP`
- `SAAAPRAQ`
and many more such possibilities.

Even though we can randomly keep generating such different permutations, not all of them represent meaningful
English words. In our examples, we can see that only the second permutation `QCABSPCP` has a meaningful word `CAB`
embedded in it. 

So, the primary goal of this project is to identify all those output sequences which have meaningful English words and 
discard the remaining.

Thus our meaningful output phone number in the alpha-numeric format would be `7CAB7727`. We arrived at this number by retaining
`CAB` from `QCABSPCP` and patching up for the missing segments from the input phone number `72227727`.

## Functions usage
The module *NumberConverter.py* has the functions `all_wordifications`, `number_to_words` and `words_to_number` for the following
purposes (listed below corresponding to the function names in the same sequence):
- `all_wordifications` - returns a list of all possible alpha-numeric US phone numbers with valid English words. The input is
a US phone number in all-numeric format passed in as a string

- `number_to_words` - returns exactly one alpha-numeric phone number with a valid English word in it. The input parameter is 
a US phone number in all-numeric format passed in as a string

- `words_to_number` - returns an all-numeric US phone number corresponding to an input alpha-numeric US phone number. The input
parameter is an alpha-numeric US phone number passed in as a string

  
