import random

class Jangchi:
    def __init__(self, ism, jon, kuch):
        self.ism = ism
        self.jon = jon
        self.kuch = kuch

    def urish(self, raqib):
        zarba = random.randint(1, self.kuch)
        raqib.jon -= zarba
        print(f"{self.ism} {raqib.ism}ga {zarba} zarba berdi!")

    def tirikmi(self):
        return self.jon > 0


o1 = Jangchi("Botir", 100, 20)
o2 = Jangchi("Sher", 100, 18)

while o1.tirikmi() and o2.tirikmi():
    o1.urish(o2)
    if o2.tirikmi():
        o2.urish(o1)
    print(f"{o1.ism}: {o1.jon} | {o2.ism}: {o2.jon}")
    print("-" * 30)

if o1.tirikmi():
    print(f"G'olib: {o1.ism}")
else:
    print(f"G'olib: {o2.ism}")
