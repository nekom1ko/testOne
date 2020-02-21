import os

# from pyinput import keyboard


def cls():
    os.system("cls" if os.name == "nt" else "clear")


class Field:
    def __init__(self, w, h):
        cls()
        self.field = [[0 for x in range(w)] for y in range(h)]

    def reset(self):
        pass

    def refresh(self, field):
        cls()
        return "\n".join(
            ["".join([format(item) for item in row]) for row in self.field]
        )

    def spawnHero(self):
        self.field[0][0] = "S"
        print(self.refresh(self.field))

    def moving(self):
        self.field


field = Field(20, 10)
field.spawnHero()

