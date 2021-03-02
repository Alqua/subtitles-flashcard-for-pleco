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
#a and b MUST be dictionnaries, value must be set on 1 for it to work properly
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



#print(lst[0], '/n /n /n /n NEXTNEXTNEXTNEXTNEXTNEXTNEXTNEXTNEXTNEXTNEXTNEXTNEXTNEXTNEXT', lst[1])

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

#--end ckip part



list_dicts_prep=[]

for i[0] in segmented_texts:
    for a in i[0] :
        di={}
        for s in a:
            #print(s)
            di[s]= di.get(s,0)+1
        list_dicts_prep.append(di)



dict_in_list = []

for a in list_dicts_prep:
    lt1 = list(a.keys())
    dict_in_list.append(lt1)

#print('dictionnaires dans des listes', dict_in_list[2], dict_in_list[3])

list_of_list = []
removing = []

for l in dict_in_list:
    list_voc = []
    for word in l:
        if removing is None:
            removing.append(word)
            list_voc.append(word)
        elif word not in removing:
            removing.append(word)
            list_voc.append(word)
    list_of_list.append(list_voc)

print('/n', 'List de voc (normalement moins en moins de voc par liste)', list_of_list[7])

#create folder for results
if not os.path.exists('results'):
    os.makedirs('results')

for count, item in enumerate(list_of_list, 1):
    # every file will get the the index as name
    with open(f'results/{count}.txt', 'w') as f:
        f.write("\n".join(str(i) for i in item))
