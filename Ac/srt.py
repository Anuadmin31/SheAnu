name = "      Anushri Shivanand Chinchankar  "
print("display the initial name:",name)

Name = name.strip()
print("Display stripped name:",Name)
print("Display name in sentence case:",Name.capitalize())
print("Display name in title case:",Name.title())
print("Display name in upper case:",Name.upper())


fname,mname , lname = Name.title().split()

#joining name
shortname = " ".join([fname[0],mname[0],lname])
print("Display name after joining:",shortname)

#replace space with underscore
usrname = shortname.replace(" ","_")

passwd = fname[:2]+mname[:2]+lname
print(usrname)
print(passwd)


