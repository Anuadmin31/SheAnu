sub1 = int(input("Enter a marks1:"))
sub2 = int(input("Enter the marks:"))
sub3 = int(input("Enter the marks:"))
sub4 = int(input("Enter the marks:"))

subtotal = sub1+sub2+sub3+sub4
if (sub1 >= 40) and (sub2 >=40) and (sub3>=40) and (sub4>=40) :
    if subtotal >= 75 :
         print("Passed in distinction")
    elif subtotal >= 60 : 
          print("Passed in first class")
    elif subtotal >= 50:
          print("passed in second class")
    else:
         print("Passed in all subjects")

print (subtotal)
subpercent = (subtotal/500)*100
print(subpercent)