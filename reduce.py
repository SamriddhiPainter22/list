import functools
list1=[10,20,30,40,50,60]
list2=[20,40,50,60,70,30]
list3=[30,60,80,40,20,10]

if functools.reduce(lambda x,y:x and y,map(lambda a,b:a==b,list1,list2),True):
    print("The list 1 and list2 are same")
else:
    print("The list 1 and list2 are not same")

if functools.reduce(lambda x,y:x and y,map(lambda a,b:a==b,list1,list3),True):
    print("The list 1 and list3 are same")
else:
    print("The list 1 and list3 are not same")
