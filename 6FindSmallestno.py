a=[]
n=int(input("enter the number of element"))
for i in range(1,n+1):
    b=int(input("Enter the number"))
    a.append(b)
a.sort(reverse=True)
print("minimum element is:",a[n-1])
