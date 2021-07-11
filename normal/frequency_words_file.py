fp=open("list-11\\readme.txt","r")
sentence=fp.read()
words=sentence.split()
d = dict()
for c in words:
    if c not in d:
       d[c] = 1
    else:
       d[c] += 1       
#dictionary values       
a=d.values()
b=max(a)
for i in d:
    if(d[i]==b):
        print("frequent word:",i,";","count:",b)