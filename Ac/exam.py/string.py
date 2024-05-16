name = "            anush  shivanand chinchankar    "
print("display original name:",name)

name = name.strip()
print("display stripped name:",name)
print("display sentence case:",name.capitalize())
print("display name in title case:",name.title())

fname,mname,lname = name.title().split()

shortname = " ".join([fname[0],mname[0],lname])
print("display shortname:",shortname)

#replacing space with underscore

usrname = shortname.replace(" ","_")
passwd = fname[:2]+mname[:2]+lname
print(usrname)
print(passwd)