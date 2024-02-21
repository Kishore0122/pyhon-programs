a=int(input("enter a number:\n"))
b=int(input("enter a number:\n"))
def gcd(a,b):
 while b:
     a,b = b,a%b
     print(a,b)
 return a
if a<0 or b<0:
 print("invalid")
else:
 print("gcd of",a,"and",b,"is",gcd(a,b))
