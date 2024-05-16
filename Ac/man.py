stdrec = (("20CS31P","python programming",40),
          ("20CS32P","DBMS",49),
          ("20CS33P","CN",47),
          ("20CS34P","Computer Hardware",46))


#used for loop to access and display tuple items in .format form 

print("SR.NO",   "coursecode",     "coursename",    "marks")

for i, x in enumerate (stdrec):
 print("{:5d} {:10s} {:10s} {:7d}".format(i+1,x[0],x[1],x[2]))

#unpacking student info in separate variable
sub1, sub2, sub3, sub4 = stdrec
print("Unpacking:",sub1,sub2,sub3,sub4)

#concatenation
subconcat = sub1+sub2+sub3+sub4
print("after concatenation:",subconcat)

#membership
("Membership:",47 in stdrec)

#slicing
for x in stdrec:
  print("Slicing/n:",x[1:])


tmarks = tuple(x[2] for x in stdrec)

print("Maxmimum marks:",max(tmarks))
print("Minimum marks:",min(tmarks))
[print("sum:",sum(tmarks))]




    


