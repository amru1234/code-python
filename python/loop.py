'''N=int(input())
j=1
for i in range(1,N+1):
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(j-1,0,-1):
        print(k,end=" ")
    print()
    

N=int(input())
j=1
for i in range(1,N+1):
    for j in range(1,N+1):
        if(j<=N-i):
           print(" ",end=" ")
        else:
            print(i,end=" ")
    print()
print()

N=int(input())
j=1
for i in range(1,N+1):
    for j in range(i):
           print(j**2,end=" ")
    print() 
print() 

N=int(input())
j=1
for i in range(1,N+1):
    for j in range(1,N+1):
           print("*",end=" ")
    print() 
print() 

N=int(input())
for i in range(1,N+1):
    for j in range(1,N+1):
        if(j<=N-i):
            print(" ",end="")
        else:
            print("* ",end="")
    print()
print()

N=int(input())
a=65
for i in range (N+1):
    for i in range(1,i+1):
        print(chr(a),end=" ")
    print()
    a=a+1
print()

N=int(input())
a=1
for i in range(1,N+1):
    for j in range(1,i+1):
       print(a,end=" ")
    print()
    a=a+2
print()

N=int(input())
for i in range(1,N+1):
    for j in range(N+1):
        print(i,end=" ")
    print()
print()

rows=int(input())
num=1
print("Show the numbers")
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1
    print()
print()

N=int(input())
for i in range(1,N+1):
    for j in range(1,i+1):
        if(j==1 or j==i or i==N):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()
'''
N=int(input())
for i in range(1,N+1):
    for j in range(1,N+1):
        if(j<=N-i):
            print(" ",end="")
        else:
            print(i,end="")
    for k in range(1,i):
        print(i,end="")
    print()
print()

        
    
                    
    
    
        



      