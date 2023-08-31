N=int(input("Enter any Number"))
i=1
for i in range(1,5):
    j=1
    for j in range(i):
        print("*",end=" ")
    print()
print()
for i in range(1 ,11):
    print("2*",i,"=", 2*i)
print()
for n in range(10,-1,-2):
    print(n)
print()
start=1
while(start <= 10):
    print(start,"Amruta Here!")
    start=start+1
name="Amruta"
print(name)
for i in range(-1,len(name),-1):
      print(name[i])
print()
print(name[0::2])
print(name[-1::-1])
print(name.lower())
print(name.upper())
b="heream rutabagde"
print(b.title())
print(b.capitalize())
print(b.find('z',6))
print(b.index('a',11))
print(b.isalnum())
def f1(name):
  print(name)
for i in range(5):
    name=input("Enter name:")
    f1(name)
print()

def f2(x):
   return x**2
x=float(input("Enter any Number:"))
res=f2(x)
print(res)