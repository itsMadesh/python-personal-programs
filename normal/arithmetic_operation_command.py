import sys
f=open("file5.txt","w")
f.write("2\n")
f.write("3")
f.close()
print(sys.argv)
fp=open(sys.argv[1],"r")
a=[]
for line in fp:
    a.append(int(line))
if sys.argv[2]=="+":
    print(a[0],"+",a[1],":",a[0]+a[1])
elif sys.argv[2]=="-":
    print(a[0],"-",a[1],":",a[0]-a[1])
elif sys.argv[2]=="*":
    print(a[0],"*",a[1],":",a[0]*a[1])
elif sys.argv[2]=="%":
    print(a[0],"%",a[1],":",a[0]%a[1])
elif sys.argv[2]=="/":
    print(a[0],"//",a[1],":",(a[0]//a[1]))
elif sys.argv[2]=="**":
    print(a[0],"**",a[1],":",a[0]**a[1])            