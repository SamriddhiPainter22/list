#initialize the pyhton list

from re import X


It1=[5,10,15,20,25,30,35]
It2=[2,4,6,8,10,12,14]

#print both the original list
print("Python Original list1 :"+str(It1))
print("Python Original list2 :"+str(It2))

#use the naive method to add two lists

res_It=[]  #Declaration of list
for x in range(0,len(It1)):
    res_It.append(It1[x]+It2[x])

#Display the sum of two lists

print("Addition of the two given lists are : "+str(res_It))
