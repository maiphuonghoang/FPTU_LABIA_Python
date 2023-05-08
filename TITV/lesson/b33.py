
# Xây dựng class "cha"
class Animal:
    def __init__(self, animalTypeA, nameA, weightA, heightA):
        self.type = animalTypeA
        self.name = nameA
        self.weight = weightA
        self.height = heightA
    def makeVoice(self):
        print('Unknown voice')
    def printMe(self):
        print('animalType: {0}, name: {1}, weight: {2}, height: {3}'
              .format(self.type, self.name, self.weight, self.height))
    
a1 = Animal("Con người", "Nguyễn Văn A", '60kg', '170cm')
a1.printMe()

class Dog (Animal):
    #constructor của lớp con 
    def __init__ (self, name, weight, height, isChampion):
        # gọi constructor của lớp cha 
        Animal.__init__(self, "Dog", name, weight, height)
        # gán giá trị cho các thuộc tính bổ sung 
        self.isChampion = isChampion
    
    # override method
    def makeVoice(self):
        print(self.name,'gau gau' )

    def takeHome(self):
        print('zzzZZZ')


d1 = Dog('Cậu vàng', '20kg', '80cm', True)
d1.printMe(); d1.makeVoice(); d1.takeHome()
d2 = Animal('Chó','20kg', '80cm', True)
d2.printMe(); d2.makeVoice()
