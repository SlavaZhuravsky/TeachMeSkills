

# class Student():
#     firstName = 'Слава'
#     lastName = 'Журавский'
#     groupNumber = 'Z24-onl'
#     age = 26
#     def getFullname(self):
#         print(f'{self.firstName} {self.lastName}')
#     def getAge(self):
#         print(f'{self.age}')
#     def GetGroupNumber(self):
#         print(f'{self.groupNumber}')
#     def setNameAge(self, fistName, lastName, groupNumber, age):
#         self.firstName = fistName
#         self.lastName = lastName
#         self.groupNumber = groupNumber
#         self.age = age
#     def setGroupNumber(self, groupNumber):
#         self.groupNumber = groupNumber
        
# student = Student()
# student.getFullname()
# student.getAge()
# student.GetGroupNumber()
# student1 = Student()
# student1.setNameAge('Вова', 'Пестунов', 'сс12', 21)
# student1.setGroupNumber('сс13')
# student1.getFullname()
# student1.getAge()
# student1.GetGroupNumber()
# student2 = Student()
# student2.setNameAge('Дашаf', 'Рыдлевич', 'сс13r', 21)
# student2.setGroupNumber('сс14')
# student2.getFullname()
# student2.getAge()
# student2.GetGroupNumber()
#________________________________________________________________


class Product():
    def __init__(self, price, weight, quality):
        self.price = price
        self.weight = weight
        self.quality = quality
        
    def value(self):
        print(f"Шоколад стоит {self.price}")

    def weighing(self):
        print(f"Шоколад весит {self.weight}")

    def assesment(self):
        print(f"Качество {self.quality}")

class Fruits(Product):
    def value(self):
        print(f"Яблоко стоит {self.price}")

    def weighing(self):
        print(f"Яблоко весит {self.weight}")

    def assesment(self):
        print(f"Яблоко качества {self.quality}")


class Vegetables(Product):
    def value(self):
        print(f"Картошка стоит {self.price}")

    def weighing(self):
        print(f"картошка весит {self.weight}")

    def assesment(self):
        print(f"Картошка качества {self.quality}")    

class Nuts(Product):
    def value(self):
        print(f"Миндаль стоит {self.price}")

    def weighing(self):
        print(f"Миндаль весит {self.weight}")

    def assesment(self):
        print(f"Миндаль качества {self.quality}")

    
Chocolate = Product("1.8 BYN", "90g", "High")
Chocolate.value()
Chocolate.weighing()
Chocolate.assesment()

Apple = Fruits("2 BYN", "1kg", "High")

Apple.value()
Apple.weighing()
Apple.assesment()

Potato = Vegetables("3 BYN", "3.5 kg", "High")
Potato.value()
Potato.weighing()
Potato.assesment()

Almonds = Nuts("3 BYN", "3.5 kg", "High")
Almonds.value()
Almonds.weighing()
Almonds.assesment()



# class Product():

#     def __init__(self, price, title, producing_country):
#         self.price = price
#         self.title = title
#         self.producing_country = producing_country

# class Purchase(Product):
    
#     def purchase(self):
#         self.title = ['картошка', 'морковь', 'лук', 'яблоко']
#         name = input('Введите название продукта: ')
#         if name in self.title:
#             print(f'{name} есть в надличии, на какую сумму вам взвесить?')   
#         else:
#             print('приходите позже, данного продукта нет в наличии')
#         return 
#     def purchase_1(self):
#         self.price = int(input('Введите сумму: '))
#         if self.price > 100:
#             print('Извините, но столько товара нету!')
#         else:
#             print('Хорошо, держите!')
# class 

# b = Product(12, 'лук', 'dsd')
# a = Purchase(12, 'лук', 'лук')
# a.purchase()
# a.purchase_1()


