n = int(input("Enter a number: "))
a,b = 0,1
for _ in range(n):
  print(a, end =" ")  
  a,b = b,a+b
   
