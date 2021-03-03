This is a script to extract vocabulary list for pleco flashcards out of a series of subtitles files in traditional mandarin (here placed in the folder: subtitles). I am using ckiptagger to cut the words and extract places and people from the subs. I haven't tried it on simplified mandarin yet. You can find how to install ckiptagger here: https://github.com/ckiplab/ckiptagger

The data folder for ckip must be placed in the same folder than extract_subs.py, "hsk1-TO-4-trad.txt", "non-hsk_toremove_trad.txt" and the subtitles folder as well. The subtitles (files) must be placed in the subtitles folder, in order and without any other files. Normally any readable file format should work but I only tested it with ".srt"

The result are different txt files:
- "sorted_full.txt" which is all the vocabulary extracted with word count.
- "lieux_result.txt" which is a list of all the extracted places : countries, cities or states (usually not a lot) (with minimal code modification all the ckip entities can be extracted https://github.com/ckiplab/ckiptagger/wiki/Entity-Types) 
-  "perso_result.txt" which is the list of people's name in the subs (not always correct though)
-  The vocabulary list per episode named by number. To all the vocabulary list has been removed vocabulary up to hsk4 and non-hsk words which are pretty common (check "hsk1-TO-4-trad.txt" and "non-hsk_toremove_trad.txt", non-hsk also contain weird cut or simple expression like 看看 or 等一下, 之中,... You can also add your own words to remove to that file). The vocabulary list from one episode does not contain the vocabulary from previous episodes!


The vocabulary list can be imported into pleco flashcards (import/export functionnality). You can revise the voc before and after the episode :)

Note:
- The word cutter does sometimes make mistakes, and so does the name and places recognition. Overall, I found it pretty good but that is something to take into account.
- The number of words per vocabulary list is decreasing from the beginning to the end, proof that watching series is a great way to build vocabulary :D

