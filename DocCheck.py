#!/usr/bin/env python3
import hunspell #python3-hunspell in Ubuntu/Debian
import argparse
import string
import re

#commandline arguments
parser = argparse.ArgumentParser()

#file to spellcheck
parser.add_argument("doc", help="A file to be procesed")

#log the spellcheck results in a file
parser.add_argument("-l", "--log", action="store_true", help="log the spell check output in a file")
args = parser.parse_args()

#dictionary, to be added as an optional cli arg later with the default being a modified en_US dict
hunspellObj = hunspell.HunSpell('./dictionary/en-US.dic', './dictionary/en-US.aff')



#run a spellcheck
def checker(document):
    if args.log:
        log = open(document + '-log.txt', 'w+')
    f = open(document).read()
    #remove all the XML entities from text
    f = re.sub('&[^;]*;', ' ', f)
    #remove XML/HTML tags
    f = re.sub('<[^>]*>', ' ', f)
    for word in f.split():
        word = word.strip(string.punctuation)
        if hunspellObj.spell(word) == False:
            suggestions = ' '.join(hunspellObj.suggest(word))
            if args.log:
                log.write(word + '\n' + 'Suggestions: ' + suggestions + '\n \n')
            else:
                print(word + '\n' + 'Suggestions: ' + suggestions + '\n')

checker(args.doc)