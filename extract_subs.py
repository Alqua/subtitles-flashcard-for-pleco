#import packages
import os
import re
from ckiptagger import data_utils, construct_dictionary, WS, POS, NER

#create functions:
#-cleaning (since ckiptagger can use delimiter, it can sometimes be useful not to clean everything below)
def filter(text):
    text = re.sub("[A-Za-z0-9\!\=\？\%\[\]\,\（\）\>\<:&lt;\/#\. -----\_]", "", text)
    text = text.replace('image', '')
    text = text.replace('\xa0', '') # Delete nbsp
    # new
    r1 =  "\\【.*?】+|\\《.*?》+|\\#.*?#+|[.!/_,$&%^*()<>+""'?@|:~{}#]+|[——！\\\，。=？、：“”‘’￥……（）《》【】]"
    cleanr = re.compile('<.*?>')
    text = re.sub(cleanr, ' ', text)        #Remove html tags
    text = re.sub(r1,'',text)
    text = text.strip()
    return text

#remove a dictionnary to another one (remove b from a) based on key, a and b must be dictionnaries
def a_minus_b(a,b):
    a = {k:v for k,v in a.items() if k not in b or v != b[k]}
    return a




le_chemin_sub = 'subtitles'  # write the subtitles folder path

filenames = os.listdir(le_chemin_sub)

print(filenames)


texts_list = []  # create an empty list to save all the subtitles inside

for filename in sorted(os.listdir(le_chemin_sub)):  # for all file names in folder subtitles in order
    #ignore hidden files
    if filename[0] != '.':

        file_path = os.path.join(le_chemin_sub, filename)  # Create path with folder path and file names

        print(file_path) #to check if the order is correct
        with open(file_path, 'r') as f2:
            data = f2.read() #take the text in the file

        texts_list.append(data)  # add it to the list


sentence_list=[] # create an empty list to save all the cleaned subtitles inside

#cleaning
for i in texts_list:
    x=filter(i)
    sentence_list.append(x)


#print(sentence_list[0])

# using ckiptagger with CPU to cut the words and prepare entities
ws = WS("./data")
pos = POS("./data")
ner = NER("./data")

# create a list of a list of texts since ws accept list element and we want to keep the texts separate this time
lst = []
for i in sentence_list:
    lst.append([i])

#create empy list to store the lists of the segmented texts
segmented_texts = []

#segment
for i in lst:
    y = ws(i,segment_delimiter_set = {",", "。", ":", "?", "!", ";", "\n"}, )
    segmented_texts.append(y)

#print(segmented_texts[0]) #testing

di={}
list_dicts=[]

for i in segmented_texts:
    for a in i:
        for s in a:
            di[s]= di.get(s,0)+1
            list_dicts.append(di)

print(list_dicts[0])
#print(word_sentence_list)

'''word_sentence_list = ws(
    sentence_list,
    # sentence_segmentation = True, # To consider delimiters
    segment_delimiter_set = {",", "。", ":", "?", "!", ";", "\n"}, # This is the default set of delimiters
    # recommend_dictionary = dictionary1, # words in this dictionary are encouraged
    # coerce_dictionary = dictionary2, # words in this dictionary are forced
)

pos_sentence_list = pos(word_sentence_list)

entity_sentence_list = ner(word_sentence_list, pos_sentence_list)

def print_word_pos_sentence(word_sentence, pos_sentence):
    assert len(word_sentence) == len(pos_sentence)
    for word, pos in zip(word_sentence, pos_sentence):
        print(f"{word}({pos})", end="\u3000")
    print()
    return

print(entity_sentence_list)

print(word_sentence_list)'''

#print(entity_sentence_list)
#--end ckip part
