from array import*

arr = array("i",[10,30,40,50])
print("original array:",arr)

arr.append(60)
arr.append(70)
print("after apending 60,70:",arr)
arr.insert(1,1)
print("after inserting 1 in ist position:",arr)
arr.remove(40)
print("after removing 40:",arr)
n = arr.pop()
print("after using pop:",arr)
print("popped item",n)
n = arr.index (30)
print("first occurences of element 30 is at:",n)
lst = arr.tolist()
print("list",lst)
print("array:",arr)