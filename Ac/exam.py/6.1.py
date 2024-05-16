stud1 = ["samarth","370cs22005"]

tmarks = [67,71,76]
lmarks = [35,39,45]

tmarks = [x for x in tmarks if x<100 and x >=0]                 
lmarks = [x for x in lmarks if x<100 and x >0]

if(len (tmarks)!=3 or len(lmarks)!=3):
    print("marrks contain invalid values")

else:
    marks = tmarks.copy()
    marks.extend(lmarks)
    print(marks)

    stud1.append(marks)
    print(stud1)

    sum1 = sum(marks)
    print("total:",sum)

if "samarth" in stud1:
    print("student name is samarth")

else:
    print("different student's information")

regno = stud1[1]
colcode = list(regno)
print(colcode)
colcode = list(regno)[:3]

if colcode == ["3","7","0"]:
    print("student is registered from svp:")

else:
    print("student is not from svp")