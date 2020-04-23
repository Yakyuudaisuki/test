class Horse:
    def __init__(self, name, race, owner, rider):
        self.name = name
        self.race = race
        self.owner = owner
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name

lemaire = Rider("C.Lemaire")
vok = Horse("Vodlka","Rare","Y.Mizutani",lemaire)
print(vok.rider.name)        
