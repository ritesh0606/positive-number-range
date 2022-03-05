list1=[]
x=int(input("Enter the number of elements in the list1:"))
for i in range(0,x):
    z=int(input())
    list1.append(z)
list2=[]
y=int(input("Enter the number of elements in the list2:"))
for i in range(0,y):
    k=int(input())
    list2.append(k)
print("Input: list1 = ",end=" ")
print(list1)
print("Output:",end=" ")
for num in list1:
    if (num>0):
        print(num, end=" " )
    else:
        continue
print()
print("Input: list2 = ",end=" ")
print(list2)
print("Output:",end=" ")
for num in list2:
    if (num>0):
        print(num, end=" ")
    else:
        continue
