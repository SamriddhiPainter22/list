import collections

list1=[10,20,30,50,60]
list2=[20,10,50,70,40]
list3=[50,40,30,20,10]

if collections.Counter(list1)==collections.Counter(list2):
    print("The list |1 and |2 are the same")
else:
    print("The list |1 and |2 are the same")

if collections.Counter(list1)==collections.Counter(list3):
    print("The list |1 and |3 are the same")
else:
    print("The list |1 and |3 are not the same")