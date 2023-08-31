l=[]
mul=1
n=int(input())
len=int(input())
for i in range(len):
    b=int(input())
    l=l+[b]
    mul=mul*b
print()
print(mul%n)
print(l)
print(max(l))



def ismonotronic(A):
    x,y=[],[]
    x.extend(A)
    y.extend(A)
    x.sort()
    y.sort(reverse=True)
    if(x==A or y==A):
        return True
    return False
A=[4,9,6,8]
print(ismonotronic(A))


    