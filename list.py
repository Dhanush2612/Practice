# List Comprehension in 1 line(Method 3)
x = [i for i in range(0,101,2)]
print(x)

#Method 1
x=list(range(0,101,2))
print(x)

#Method 2
x=[]
for i in range(0,101,2):
    x.append(i)
print(x)



