class Hewan:
    def suara(self):
        pass

class Kucing(Hewan):
    def suara(self):
        return "Meong"

class Anjing(Hewan):
    def suara(self):
        return "Guk"

hewan1 = Kucing()
hewan2 = Anjing()
print(hewan1.suara())
print(hewan2.suara())

