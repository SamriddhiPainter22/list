#initialize the python list

It1=[2,4,6,8,10,12]
It2=[2,4,6,8,10,20]

#print the original list of python
print("Python list 1 :"+str(It1))
print("Python list 2 :"+str(It2))

#use the comprehension method to add the two list
res_It=[It1[x]+It2[x]
for x in range(len(It1))]

#display the addition result of two lists
print("Addition of list It1 and It2 is :" +str(res_It))

