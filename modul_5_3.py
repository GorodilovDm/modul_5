class House:
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i + 1)

    def __str__(self) -> str:
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __len__(self) -> int:
        return self.number_of_floors

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        return self.number_of_floors + value

    def __iadd__(self, value):
        return self.number_of_floors + int(value)



h1 = House('ЖК Матрешки', 14)
h2 = House('ЖК Адмирал', 17)
# h1.go_to(14)
# h2.go_to(7)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

# __eq__
print(h1 == h2)
h1.number_of_floors = 17
print(h1 == h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)
print(h1 == h2)