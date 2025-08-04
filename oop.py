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



class Myclss:          #  clss   er    nam ta  capital letter  a   ditye  hoy
    x=10
    y=20
    z=30

    def addTwo(self,a,b):
        sum=self.x+self.y+self.z+a+b
        print(sum)

    def addNew(self):
        self.addTwo(5,6)


obj =Myclss()
obj.addTwo(30,50)
obj.addNew()











