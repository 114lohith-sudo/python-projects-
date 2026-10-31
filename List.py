list1=[1,0.8,"red",1.3,"dog"]
print(list1)
print(list1[3])
numberOfelements=len(list1)
print(numberOfelements)
list1.append("hello")
print(list1)
list1.insert(2,35)
print(list1)
list1.remove("dog")
print(list1)
list1.pop(2)
print(list1)
#append only adds new elements at the end while insert adds new elements at any index
#to use remove to remove a element you need to put the name of the element, but to use pop to remove a element you need to put the index of that value
list1[4]="good"
print(list1)
h=list1.index("good")
print(h)
list1.append(1)
list1.append(1)
print(list1.count(1))
#len shows how many total elements they are in the list while count shows how many times one element is repeating in a list.