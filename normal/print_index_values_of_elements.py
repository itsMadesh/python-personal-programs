def find(arr, search):
    index=[] 
    for i in range(0,n):
        if search==arr[i]:
            index.append(i)
    return index
arr=[]
n=int(input("Enter no.of inputs:"))
for i in range(0,n):
    a=int(input("Enter a value in index-"+str(i)+":"))
    arr.append(a)
print(arr)
search=int(input("Enter a search value:"))   
        