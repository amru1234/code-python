num1=int(input())
num2=int(input())
opr=(input("Enter the opr....."))
if(opr=="+"):
   print(num1+num2)
elif(opr=="-"):
    print(num1-num2)
elif(opr=="*"):
    print(num1*num2)
elif(opr=="/"):
    print(num1/num2)
else:
    print("Plizz enter valid no..")
for i in range(22,10,2):
      print(i)

var=56
def addition():
     var1=7
     c= var+var1
     print("local scope:",var1)
     print("Adding Global + Local Scope:",c)
addition()
print("in global scope",var)



