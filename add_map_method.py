from operator import add
#import th eadd Python List element

It1=[2,4,6,8,10]
It2=[1,2,3,4,5]

#display the original list 
print("Display the element of list1:"+str(It1))
print("Display the element of list2:"+str(It2))

#use map() function with add operator to add the original list It1 and It2
res_It=list(map(add,It1,It2))
#pass the It1 and It2 and add as a parmeter

#Display the sum of the two list
print("Sum of the list 1 and list 2:"+str(res_It))