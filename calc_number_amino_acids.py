#!/usr/bin/env python3
# calc_number_amino_acids.py

'''Report average weight of a user-fed protein sequence'''
import sys

DNA = str(input('Please enter a name for the DNA sequence: '))
print(f'Your sequence name is: {DNA}')

DNA_LEN = int(input('Please enter the length of the sequence: '))
print(f'The length of the DNA sequence is: {DNA_LEN}')

AVG_AA_WT = 110


if DNA_LEN%3 == 0:
    print(f'The length of decoded protein is: {DNA_LEN/3}')
    print(f'The average weight of the protein sequence is: {((DNA_LEN/3) * 110) / 1000}')

else:
    # print to STDERR
    print('\n\nError: the DNA sequence is not a multiple of 3', file=sys.stderr)

    # give it to a non-zero exit value
    sys.exit(1)
