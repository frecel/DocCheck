#!/usr/bin/env python3
import hunspell #python3-hunspell in Ubuntu/Debian
import argparse
import string
import re
import os
import sys

#commandline arguments
parser = argparse.ArgumentParser()

#file to spellcheck
parser.add_argument("doc", help="A file to be procesed")

#log the spellcheck results in a file
parser.add_argument("-l", "--log", action="store_true", help="log the spell check output in a file")
parser.add_argument("-d", "--dirlog", action="store", help="logs the spell check output in a folder you point to")
parser.add_argument("-r", "--recursive", action="store_true", help="search a directory recursively")
args = parser.parse_args()

#dictionary, to be added as an optional cli arg later with the default being a modified en_US dict
hunspellObj = hunspell.HunSpell('./dictionary/en-KDE.dic', './dictionary/en-KDE.aff')



#run a spellcheck
def checker(document):
    if args.log:
        log = open(document + '-log.txt', 'w+')
    elif args.dirlog:
        if os.path.isdir(args.dirlog):
            log = open(args.dirlog + os.path.basename(document)p + '-log.txt', 'w+')
        else:
            sys.exit("follow -d argument with a directory")
    f = open(document).read()
    #remove all the XML entities from text
    f = re.sub('&[^;]*;', ' ', f)
    #remove XML/HTML tags
    f = re.sub('<[^>]*>', ' ', f)
    for word in f.split():
        word = word.strip(string.punctuation)
        if hunspellObj.spell(word) == False:
            suggestions = ' '.join(hunspellObj.suggest(word))
            if log:
                log.write(word + '\n' + 'Suggestions: ' + suggestions + '\n \n')
            else:
                print(word + '\n' + 'Suggestions: ' + suggestions + '\n')

#find and spell check documents
if os.path.isfile(args.doc): #if argument was a file
    checker(args.doc)
elif os.path.isdir(args.doc): #if argument was a directory
    if args.recursive: #recursive
        for dirs in os.walk(args.doc):
            files = dirs[2]
            for name in files:
                if os.path.splitext(name)[1] == '.docbook':
                    checker(dirs[0] + '/' + name)
    else: #single folder
        for files in os.listdir(args.doc):
            if os.path.splitext(files)[1] == '.docbook':
                checker(args.doc + files)    
else:
    sys.exit('This is not a file or a directory')