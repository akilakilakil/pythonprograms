gender,name=(input("enter the gender and name")).split()
if gender=="boy":
    if name=="dhoni" or name=="Dhoni":
        print("Hello","Mr",name,"too Great")
    else:
        print("Hello","Mr",name)
elif gender=="girl":
    print("Hello","Ms",name)
else:
    print("enter the correct gender")
