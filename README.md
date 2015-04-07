# DocCheck
Batch spell check for DocBook format files made with spell checking KDE documentation in mind.

pyhunspell is required to run DocCheck

For Ubuntu and its derivatives simply run:
`sudo apt install python3-hunspell`

##Usage:
`python3 DocCheck.py documentation.docbook`

additaionally you can add -l argument to write all the results into a file called documentation.docbook-log.txt

##TODO:
* Add the rest of KDE applications and projects to the dictionary
* Spellchecking entire directories
* Changing dictionaries through cli args

