num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
   print("****")  
for i in range(8):
    print("{0} is num".format(i))
print("****")
n=float(int(input()))
if n>0:
    print("{0} is positive".format(n))
else:
    print("{0} is negative".format(n))
    
print("***")

n=int(input())
c=0
for i in range(1, n, 1):
    if(n%i==0):
        c=c+1
if(c==2):
    print("{0} is prime no",n)
else:
    print("{0} is not prime no",n)
