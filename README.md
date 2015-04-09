# DocCheck
Batch spell check for DocBook format files made with spell checking KDE documentation in mind.

pyhunspell is required to run DocCheck

For Ubuntu and its derivatives simply run:
`sudo apt install python3-hunspell`

##Usage:
To spell check a single file:  
`python3 DocCheck.py documentation.docbook`  
To spell check a directory:  
`python3 DocCheck.py ./this/is/a/directory`  
To spell check a directory recursively:  
`python3 DocCheck.py -r ./this/is/a/directory`

additaionally you can add -l argument to write all the results into a file called documentation.docbook-log.txt

##TODO:
* Add the rest of KDE applications and projects to the dictionary
* Allow changing where the logs are saved
* Changing dictionaries through cli args

