
def intersection(l1, l2):
    l3 = [value for value in l1 if value in l2]
    return l3
def union(l1, l2,l3):
    merge_list = set((l1 + l2))
    l4=list(merge_list)
    return l4


n=int(input("Enter a number-n:"))
l1=[]   
for i in range(0,n,1):
    a=int(input("Enter a value in l1["+str(i)+"]:"))
    l1.append(a)
print(l1)
m=int(input("Enter a number-m:"))
l2=[]   
for i in range(0,m,1):
    b=int(input("Enter a value in l2["+str(i)+"]:"))
    l2.append(b)
print(l2)
l3=intersection(l1,l2)
print("intersection of two lists:",l3)
print("union of two lists:",union(l1,l2,l3))