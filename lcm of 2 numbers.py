a=int(input("enter a number:\n"))
b=int(input("enter a number:\n"))
def gcd(a,b):
 while b:
     a,b = b,a%b
     print(a,b)
 return a
def lcm(a,b):
 return (a*b)/gcd(a,b)
if a<0 or b<0:
 print("invalid")
else:
 print("lcm of",a,"and",b,"is",lcm(a,b))
