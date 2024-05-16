lst1 = [14,23,23,46,78]


lst1.append(4)

lst1.append((3,4))

lst1.extend((3,7))


lst1.insert(3,2)
print(lst1)

del lst1[3]
print(lst1)

a = lst1.pop()
print(a)

lst1.remove(14)
print(lst1)



