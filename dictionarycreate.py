x={}
n=int(input("Enter number of elements: "))
for i in range(n):
  k=input("Enter key: ")
  v=int(input("Enter value: "))
  x.update({k:v})
print(x)  
