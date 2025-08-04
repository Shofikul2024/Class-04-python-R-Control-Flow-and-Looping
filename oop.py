# # class
#
#
# class Myclss:          #  clss   er    nam ta  capital letter  a   ditye  hoy
#     x=10
#     y=30
#     z=40
#     sum=x+y+z
#
#
# obj1=Myclss()                #aitake object bola  hoy
# print(obj1.x)
#
#
# obj2=Myclss()                #aitake object bola  hoy
# print(obj1.y)
#
#
#
# obj2=Myclss()                #aitake object bola  hoy
# print(obj1.z)
#
#
# obj1=Myclss()                #aitake object bola  hoy
# print(obj1.x)
# print(obj1.y)
# print(obj1.z)
# print(obj1.sum)


#
# class Myclss:          #  clss   er    nam ta  capital letter  a   ditye  hoy
#     x=10
#     y=20
#     z=30
#
#     def addTwo(self,a,b):
#         sum=self.x+self.y+self.z+a+b
#         print(sum)
#
#     def addNew(self):
#         self.addTwo(5,6)
#
#
# obj =Myclss()
# obj.addTwo(30,50)
# obj.addNew()









#
# class Myclss:          #  clss   er    nam ta  capital letter  a   ditye  hoy
#     x=10
#     y=20
#     #z=100
#
#     def __init__(self,zValue,xValue):
#         self.z=zValue
#         self.x=xValue
#
#     def addTwo(self):
#         print(self.x+self.y+self.z)
#
#
# obj =Myclss(100 , 5)
# obj.addTwo()
#
#
#
#

#static method
#
# class Myclss:          #  clss   er    nam ta  capital letter  a   ditye  hoy
#     x=10
#     y=20
#     @staticmethod
#     def addTwo():
#         z=Myclss.x+Myclss.y
#         print(z)
# Myclss.addTwo()
#
#
#
#






#static  variable
#
# class Myclass:
#     x=10
#     y=20
#     @staticmethod
#     def addTwo():
#         z=Myclass.x+Myclass.y
#         print(z)
#
# Myclass.addTwo()
#






#  static variable
class Myclas:
    x=10
    y=20
    @staticmethod
    def addTwo():
        z=Myclas.x+Myclas.y
        print(z)
print(Myclas.x)
print(Myclas.y)
obj=Myclas()
print(obj.x)
print(obj.y)


