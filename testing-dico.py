fh = open("1dict-full.txt")

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


fy = open("2dict-full.txt")
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


fz = open("3dict-full.txt")
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

print(list_dicts, 'SPACE SPACE')
list_dicts_worked.append(t1)

def a_minus_b(a,b):
    a = {k:v for k,v in a.items() if k not in b or v != b[k]}
    return a

dico2 = a_minus_b(list_dicts[1],list_dicts[0])
list_dicts_worked.append(dico2)

dico3 = a_minus_b(list_dicts[2],list_dicts[0])
dico3 = a_minus_b(list_dicts[2],list_dicts[1])
list_dicts_worked.append(dico3)

print(list_dicts_worked)
