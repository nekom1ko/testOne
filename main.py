import os
import msvcrt
import keyboard


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

    # заполняю массив поля нулями
    def reset(self):
        self.field = [[0 for x in range(self.w)] for y in range(self.h)]

    # очищаю консоль и рисую поле заново (передаю в функцию массив с полем)
    def refresh(self, field):
        cls()
        print(
            "\n".join(["".join([format(item) for item in row]) for row in self.field])
        )

    # спавню героя на 0 0
    def spawnHero(self):
        self.xPos = 0
        self.yPos = 0
        self.field[self.xPos][self.yPos] = self.heroSymbol
        self.refresh(self.field)

    def moveRight(self):
        if self.xPos != (self.w - 1):
            self.xPos += 1
            self.reset()
            self.field[self.yPos][self.xPos] = self.heroSymbol
            self.refresh(self.field)

    def moveLeft(self):
        if self.xPos != 0:
            self.xPos -= 1
            self.reset()
            self.field[self.yPos][self.xPos] = self.heroSymbol
            self.refresh(self.field)


def startGame():
    cls()
    global field
    field = Field(20, 10)
    field.spawnHero()


def updateMoving(key):
    if key == "a":
        print("kek")
        # field.moveLeft()
    if key == "d":
        field.moveRight()


startGame()


try:
    while True:
        updateMoving(keyboard.read_key())

except KeyboardInterrupt:
    pass

