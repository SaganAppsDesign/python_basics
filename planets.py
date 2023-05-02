from datetime import datetime

class Planet:
    def __init__(self, name, radius, num_satel):
        self.name = name
        self.radius = radius
        self.num_satel = num_satel
        self.date = datetime.now()
        
    def infoPlanet(self):
        print(f"\nInfo Planeta: {self.date}")
        print(f"\nNombre : {self.name}")
        print(f"Radio : {self.radius}")
        print(f"Num satélites : {self.num_satel}\n")

class ExoPlanet (Planet):
    def infoPlanet(self):
        print(f"\nExoplaneta")
        return super().infoPlanet()


planet1 = Planet("Urano", 12000, 5)
planet2 = Planet("Neptuno", 18000, 54)
planet3 = Planet("Saturno", 72000, 123)
exoPlanet1 = ExoPlanet("GPT92", 45555, 78)

planet1.infoPlanet()
exoPlanet1.infoPlanet()

planetNameList = [planet1.name, planet2.name, planet3.name, exoPlanet1.name]

for planet in planetNameList:
    print(planet)

print("\n")

