stud1 = ["samarth","370cs22005"]

tmarks = [46,89,90]
lmarks = [34,89,45]

tmarks = [x for x in tmarks if x <= 100 and x >= 0]
lmarks = [x for x in lmarks if x <= 100 and x >= 0]

if (len (tmarks) !=3 or len(lmarks)!=3):
    print("marks contain invalid marks")
else:
    marks = tmarks.copy()
    marks.extend(lmarks)

    stud1.append(marks)

    sum1 = sum(marks)
    print("total:",sum1)

if "samarth" in stud1:
    print("belongs to svp")
else:
    print("doesnt belongs to svp")


regno = stud1[1]
colcode = list(regno)

colcode = regno[:3]

if colcode == ["3","7","0"]:
    print("student belongs to svp")
else:
    print("not from svp")
