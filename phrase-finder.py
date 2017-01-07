#!/usr/bin/env python
# python 2.7

'''
USAGE: 
DESCRIPTION: This script will find common phrases in a text document

'''

# ~~~~ LOAD PACKAGES ~~~~~~ #
import sys
import os
import argparse

text_file="txt/Dracula-Bram_Stoker.txt"

print text_file

with open(text_file, 'r') as myfile:
    data=myfile.read()

# split on sentences

print data.split('.')