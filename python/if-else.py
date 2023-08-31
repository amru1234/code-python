a=int(input())
b=int(input())
c=int(input())
res=a+b+c/150*100
if(res>=35 and res<=45):
    print("Varpass")
elif(res>=46 and res<=60):
    print("pass")
elif(res>=61 and res<=74):
    print("Good")
elif(res>=75 and res<=85):
    print("1'st class")
else:
    print("Golden Opportunities")
i=1
while(i<10):
    if(i==5):
        break
    print(i,"Hello")
    i=i+1
print()

L=[]
sum=0
len=int(input())
for i in range(len):
    a=int(input())
    L=L+[a]
    if(L[i]%2==0):
        sum=sum+L[i]
print(L)
print("Sum of the element are = ",sum)


for i in range(1,len+1):
    j=i
    for j in range(i):
        print(i,end=" ")
    print()
print()

def fun():
    print("Amruta")
for i in range(5):
    fun()
print()


len=int(input())
L=[]
d=[]
for i in range(len):
    a=input()
    L=L+[a]
for i in range(len):
    j=i+1
    while(j<len):
        if(L[i]==L[j] and L[i] not in d):
            d=d+[L[i]]
        j=j+1
print(L)
print(d)

def fun(i):
    print("Amruta")
    if(i<5):
        i=i+1
        fun(i)
    return 0
i=1
fun(i)

L=[]
len=int(input())
for i in range(len):
    a=int(input())
    L=L+[a]
print(L)

yes = "Amruta Sewakram Bagde"
print(yes)

f1=open('amc.txt','w')
f1.write('Amruta Here')
f1.close()





        
    
        
    