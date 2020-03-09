import os
import msvcrt

# from pyinput import keyboard


def cls():
    os.system("cls" if os.name == "nt" else "clear")


class Field:
    heroSymbol = "S"

    def __init__(self, w, h):
        self.w = w
        self.h = h
        cls()
        self.field = [[0 for x in range(w)] for y in range(h)]

    # заполняю поле нулями
    def reset(self):
        self.field = [[0 for x in range(self.w)] for y in range(self.h)]

    # очищаю консоль и заполняю поле заново
    def refresh(self, field):
        cls()
        print(
            "\n".join(["".join([format(item) for item in row]) for row in self.field])
        )

    def spawnHero(self):
        self.xPos = 0
        self.yPos = 0
        self.field[self.xPos][self.yPos] = self.heroSymbol
        self.refresh(self.field)

    def moveRight(self):
        self.xPos += 1
        self.reset()
        self.field[self.yPos][self.xPos] = self.heroSymbol
        self.refresh(self.field)


field = Field(20, 10)
field.spawnHero()
field.moveRight()
field.moveRight()

