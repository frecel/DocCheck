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
To log the output of DocCheck in a file in the same directory as the docbook file(s)  
`python3 DocCheck.py -l ./this/is/a/directory`  
You can also specify where the log files should be kept  
`python3 DocCheck.py ./this/is/a/directory -d /home/JohnDoe/Documents`  
I just realized that that if you go recursively through a directory and put all of the log files in one directory chances are you are going to have multiple files with the same name (ex. index.docbook). Every time DocCheck will go through a new file with the same name as another one it check from another directory it will just write over the log file since -d and -l arguments use the same format for file names.

##Dictionary:
The en-KDE dictionary included with DocCheck is a modified version of Mozilla's en-US dictionary for Firefox browser. It is a more technical dictionary which includes names of programming languages, protocols, file extensions and names of many KDE projects. It also allows for different spelling variants of the some words (ex. both colour and color are acceptable words).




##TODO:
* Add the rest of KDE applications and projects to the dictionary
* Allow changing where the logs are saved
* Changing dictionaries through cli args
* Only allow for one spelling variant of a word in one document

