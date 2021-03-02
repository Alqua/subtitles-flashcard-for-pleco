import os

fh = open("Z1dict-full.txt")

list_dicts = []

hsk=[]

for line in fh:
    wds = line.split()
    hsk.append(wds)

di={}

#print(hsk1)

for a in hsk:
    for i in a:
        di[i]= di.get(i,0)+1
list_dicts.append(di)


fy = open("Z2dict-full.txt")
hsk=[]

for line in fy:
    wds = line.split()
    hsk.append(wds)

di={}

#print(hsk1)

for a in hsk:
    for i in a:
        di[i]= di.get(i,0)+1
list_dicts.append(di)


fz = open("Z3dict-full.txt")
hsk=[]

for line in fz:
    wds = line.split()
    hsk.append(wds)

di={}

#print(hsk1)

for a in hsk:
    for i in a:
        di[i]= di.get(i,0)+1
list_dicts.append(di)

'''print(list_dicts[0])
print('SPACE')
print(list_dicts[1])
print('SPACE')
print(list_dicts[2])
print('SPACE')
'''
t1 = list_dicts[0]
t2 = list_dicts[1]
t3 = list_dicts[2]

list_dicts_worked = []

#print(list_dicts, 'SPACE SPACE')
list_dicts_worked.append(t1)

def a_minus_b(a,b):
    a = {k:v for k,v in a.items() if k not in b or v != b[k]}
    return a

'''for k.value in t1.items():
    t1[k] = 5'''

'''t1 = dict.fromkeys(t1, 1)
t2 = dict.fromkeys(t2, 1)

p = a_minus_b(t1,t2)
print('THIS IS THE SECOND', t2)

print('THERE SHOULD HAVE NO ELEMENT OF FIRST PRINT HERE', p)
'''

dict_in_list = []

for a in list_dicts:
    lt1 = list(a.keys())
    dict_in_list.append(lt1)

print('dictionnaires dans des listes', dict_in_list)

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

print('/n', 'List de voc (normalement moins en moins de voc par liste)', list_of_list)

print('/n','tous le voc à la fin sans le dernier', removing)



if not os.path.exists('mini_results'):
    os.makedirs('mini_results')

for count, item in enumerate(list_of_list, 1):
    # every file will get the the index as name
    with open(f'mini_results/{count}.txt', 'w') as f:
        f.write("\n".join(str(i) for i in item))
