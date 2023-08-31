len=int(input())
l=[]
for i in range(len):
    a=int(input())
    l=l+[a]
print(l)
i=0
for i in range(len):
    j=i+1
    for j in range(len-1):
        if(l[i]==l[j]):
            print(l[i])
print()    
    
    
        