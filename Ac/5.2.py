stdrec = (("20CS31P0","Python programming",45),
          ("20CS32P","DBMS",48),
          ("20CS33P","CN",45))

print("S.NO","coursecode","\tcoursename","\tmarks")

for i, x in enumerate (stdrec):
    print("{:4d} {:10s}  {:11s} {:5d}".format(i+1, x[0],x[1],x[2]))

    
#unpacking students info in separate variable
sub1,sub2,sub3 = stdrec
print("Unpacking\n",sub1,sub2,sub3)

#concatenation
subconcat = sub1+sub2+sub3
print("Concatenation:/n",subconcat) 

#membership
print("membership:","20CS31P"in subconcat)

#slicing
print("Slicing")
for x in stdrec:
    print(x[1:])

tmarks = tuple(x[2] for x in stdrec)

print("total:",sum(tmarks))
print("maximum marks:",max(tmarks))
print("minimum marks:",min(tmarks))