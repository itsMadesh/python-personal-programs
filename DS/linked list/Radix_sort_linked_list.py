# from Doubly_linked_list import Doubly_Linked
def digits(num):
    rem=num%10
    num=num//10
    return rem,num
n=250
rem,n=digits(n)
print(n)