name = "    anushri shivanand chinchankar       "
print("original name:",name)

name = name.strip()
print("stripped name:",name)
print("upper case:",name.upper())
print("title case:",name.title())

fname, mname, lname = name.split().title()

shortname = " ".join([fname[0],mname[0],lname])
print("display the short name:",shortname)

usrname = shortname.replace(" ","_")
passwd = fname[:2]+mname[:2]+lname
print(usrname)