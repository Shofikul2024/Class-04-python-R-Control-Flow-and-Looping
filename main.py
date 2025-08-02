"""
marks=66
if marks>=80 and marks<=100:
    print("A+")

elif marks>=70 and marks<80:
    print("A")

elif marks>=60 and marks<70:
    print("A-")

elif marks>=50 and marks<60:
    print("B")

elif marks>=40 and marks<50:
    print("C")

elif marks>=33 and marks<40:
    print("D")

else:
    print("F")


age=30
permission=False

if age>=20:
    if permission==True:
        print("You can join with us")
    else:
        print("You can't join with us")
else:
    print("You are under aged")




"""

"""
girls=["Katrina","Carina","Jarina","Sakhina"]
# 0,1,2,3---->
for gf in girls:
    print(gf)

girls=["Katrina","Carina","Jarina","Sakhina"]
chokkor=0
# 0 , 1 , 2 , 3
while chokkor<len(girls):
    print(girls[chokkor])
    chokkor=chokkor+1    


girls=["Katrina","Carina","Jarina","Sakhina"]
# 0,1,2,3---->
for gf in girls:
    if gf=="Jarina":
        break
    print(gf)    

girls=["Katrina","Carina","Jarina","Sakhina"]
# 0,1,2,3---->
for gf in girls:
    if gf=="Carina":
        continue
    print(gf)    
"""

"""
age=19
permission=True

if age>=18 and permission==True:
    print("Welcome")



age=10
permission=True

if age>=18 or permission==True:
    print("Welcome")


age=10
permission=True

if not age>18:
    print("Not Welcome")    
"""

#
girls = ["Katrina", "Carina", "Jarina"]  # 3
girls_papa = ["KatrinaBap", "CarinaBap", "JarinaBap", "SakhinaBap"]  # 3X4=12
# 0,1,2,3---->
for gf in girls:
    print(gf)
    for papa in girls_papa:
        print(papa)




