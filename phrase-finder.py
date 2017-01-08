#!/usr/bin/env python
# python 2.7

'''
USAGE:
DESCRIPTION: This script will find common phrases in a text document

'''

# ~~~~ LOAD PACKAGES ~~~~ #
import sys
import os
import re
import string
from collections import defaultdict
# import argparse

# ~~~~ FUNCTIONS ~~~~ #
def groom_line(line):
    # remove weird dashes
    line = line.replace("_", " ")
    line = line.replace("--", " ")
    # remove misc punctuation marks
    line = ' '.join(word.strip(string.punctuation) for word in line.split())
    # remove excess whitespace
    line = re.sub('\s+', ' ', line).strip()
    return(line)

def print_doc(text_file):
    phrase_dict = defaultdict(int)
    phrase_list = []
    # read in the text
    with open(text_file, 'r') as myfile:
        data=myfile.read()

    # split on sentences
    sentences_list = split_sentences(data)

    # print the entire document
    for sentence in sentences_list:
        sentence = groom_line(sentence)
        sentence_phrases = make_chunk_list(sentence, 9, ' ')
        if len(sentence_phrases) > 0:
            for phrase in sentence_phrases:
                phrase_dict[phrase] += 1
    for key, value in phrase_dict.items():
        print value, '\t', key

def split_words(sentence):
    # split line into words
    words = groom_line(sentence).split()
    return(words)

def split_sentences(line):
    sentences = line.split('.')
    return sentences

def remove_caps(string):
    string = string.split()
    string[0] = string[0].lower()
    string = ' '.join(word for word in string)
    return string

def make_chunk_list(line, chunk_size, split_char):
    index = 0
    breakpoint = 0
    chunk_list = []
    for m in re.finditer(split_char, line):
        if len(line[breakpoint:].split(split_char)) < chunk_size:
            chunk_list.append(remove_caps(line[breakpoint:].strip()))
            break
        if index < chunk_size:
            index += 1
            continue
        else:
            chunk_list.append(remove_caps(line[breakpoint:m.end()].strip()))
            index = 0
            breakpoint = m.end()
    return chunk_list

# ~~~~ DO A THING ~~~~ #
text_file="txt/Dracula-Bram_Stoker.txt"

line1 = "So much so that all the rest seemed to take courage as if infected somewhat with her gaiety as a result even I myself felt as if the pall of gloom which weighs us down were somewhat lifted"

line2 = "All day long we seemed to dawdle through a country which was full of beauty of every kind. Sometimes we saw little towns or castles on the top of steep hills such as we see in old missals; sometimes we ran by rivers and streams which seemed from the wide stony margin on each side of them to be subject to great floods. It takes a lot of water, and running strong, to sweep the outside edge of a river clear. At every station there were groups of people, sometimes crowds, and in all sorts of attire."



# print split_sentences(line = line2)
print_doc(text_file = text_file)
