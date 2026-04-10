class test:

    # магический метот
    def __init__(self, name):
        self .name = name

    def __str__(self):
        return self.name

# test_obj = test("NAme")
# test_int = 123
#
# print(test_obj)
# print(test_int)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, *args, **kwargs):
       print("HI")

    # def __add__(self, other):
    #     return self.x + other.x, self.y + other.y

    # def __lt__(self, other):
    #      print(self.x)
    #      print(other.x)
    #
    # def __gt__(self, other):
    #     print(self.x)
    #     print(other.x)




obj_1 = Vector(12, 13)
obj_2 = Vector(22, 23)

obj_1()


class Money:
    def __init__(self, currency, sum):
        self.currency = currency
        self.sum = sum

    def convert_to_coin(self,obj):
        pass

    def __add__(self, other):
        # if self.currency != "coin" and other.currency != "coin":
        #     self.convert_to_coin(self)
        #     self.convert_to_coin(other)
        if self.currency != other.currency:
            pass
          




kg = Money("SOM", 100)
kg = Money("USD", 100)


ardager_coin = kg + us







