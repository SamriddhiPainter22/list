It1=[3,4,7,8,9]
It2=[4,8,12,16,20]

print("Display the original list1 :"+str(It1))
print("Display the original list2 :"+str(It2))

result_It=[sum(i) for i in zip(It1,It2)]

print("Sum of two list It1 and It2 is :"+str(result_It))