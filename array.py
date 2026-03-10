#1 integer array
from array import array
arr=array('i',[10,20,30,40])
print(arr)
print(type(arr))

#2 len()-number of element
from array import array
arr=array('i',[10,20,30,40,50])
print(len(arr))

#3 append(x)-add element at end
arr=array('i',[10,20,30])
arr.append(40)
print(arr)

#4 insert (pos,x)insert at position
arr=array('i',[10,20,40])
arr.insert(2,30)
print(arr)

#5 remove(x)-remove first occurence
arr=array('i',[10,20,30,20,40])
x=arr.pop()
print("remove:",x)
print(arr)

#6 pop()-remove andreturn last element
arr=array('i',[10,20,30,40])
x=arr.pop()
print("removed:",x)
print(arr)

#7 index(x)-find index of element
arr=array('i',[10,20,30,40])
print(arr.index(30))

#8 count(x)-count occurrences
arr=array('i',[10,20,30,20,40])
print(arr.count(20))

#9 reverse()-reverse array
arr=array('i',[10,20,30,40])
arr.reverse()
print(arr)

