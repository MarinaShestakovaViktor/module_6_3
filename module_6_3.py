import random
class Animal:
    live = True
    sound = None  # звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0  # степень опасности существа
    def __init__(self, speed, _cords = None): # None тк _cords не задан в db = Duckbill(10)
        if _cords is None:
            self._cords = [0, 0, 0]  #  - координаты в пространстве.
        self.speed = speed  # скорость передвижения существа

    def move(self, dx, dy, dz):
        x = self._cords[0] + dx * self.speed
        y = self._cords[1] + dy * self.speed
        z = self._cords[2] + dz * self.speed
        if z < 0:
            print("It's too deep, i can't dive :(" )
            self._cords[2] = z
        else:
            self._cords = [x, y, z]


    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")
        else:
            print("Sorry, i'm peaceful :)")

    def speak(self):
        if self.sound is not None:
            print(self.sound)

class Bird(Animal):
    beak = True  # клюв есть


    def lay_eggs(self):
        random_number = random.randint(1, 4)
        print(f"Here are(is) {random_number} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        z = self._cords[2] - abs(dz) * self.speed //2
        self._cords[2] = z



class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"
    def __init__(self, speed):
        super().__init__(speed)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()


