# Phone-Number-to-Text
This repository contains simple functions for converting between phone numbers and alpha numeric encoding

## About the Author
Arun Kumar Devarajulu is a Robotics Software developer with interests in Computer Vision, Machine Learning, and Motion Planning. 
He is an *M. Eng Robotics* graduate from the *University of Maryland, College Park*.

## About the project
This project is related to converting phone numbers into words and vice versa. To be more specific, all phone
devices (mobile phones and landlines) come with alphabets corresponding to numbers. For instance, the alphabets `A, B, C`
correspond to the number `2`. Similarly the alphabets `P, Q, R, S` correspond to the number `7`. 

Thus if we are given a number `72227727`, there could be many ways we can generate words from this sequence.
The following sre some possibilities :
- `PBACRQAS`
- `QCABSPCP`
- `SAAAPRAQ`
and many more such possibilities.

Even though we can randomly keep generating such different permutations, not all of them represent meaningful
English words. In our examples, we can see that only the second permutation `QCABSPCP` has a meaningful word `CAB`
embedded in it. 

So, the primary goal of this project is to identify all those output sequences which have meaningful English words and 
discard the remaining.

Thus out meaningful output phone number in the alpha-numeric format would be `7CAB7727`. We arrived at this number by retaining
`CAB` and patching up for the missing segments from the input phone number `72227727`.

## Functions usage
The module *NumberConverter.py* has the functions `all_wordifications`, `number_to_words` and `words_to_number` for the following
purposes (listed below corresponding to the function names in the same sequence):
- `all_wordifications` - returns a list of all possible alpha-numeric US phone numbers with valid English words. The input is
a US phone number in all-numeric format passed in as a string

- `number_to_words` - returns exactly one alpha-numeric phone number with valid English word in it. The input parameter is 
a US phone number in all-numeric format passed in as a string

- `words_to_number` - returns an all-numeric US phone number corresponding to an input alpha-numeric US phone number. The input
parameter is an alpha-numeric US phone number passed in as a string

  