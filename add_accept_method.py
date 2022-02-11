#declaration of It1,It2 and It3 lists
It1=[]
It2=[]
It3=[]

items=int(input("Enter the total number of the lists element : "))

print("Enter the items into list1 : ")
for i in range(1,items+1):
    num=int(input("Enter the value of %d index is : "%i))
    It1.append(num)

print("Enter the items into list2 : ")
for i in range(1,items+1):
    num=int(input("Enter the value of %d index is : "%i))
    It2.append(num)

for j in range(items):
    It3.append(It1[j]+It2[j])
    print("\Addition of two list is : ",It3)