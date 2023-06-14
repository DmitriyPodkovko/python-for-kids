class Animal():
    def dyxaty(self):
        print('дихає')
    def move(self):
        print('рухається')
    def toeat(self):
        print('харчується їжею')
class Ssavci(Animal):
    def eatforchildren(self):
        print('годує дитанчат')
class Giraf(Ssavci):
    def toeatlist(self):
        print('їсть листя')
    def leftlegforward(self):
        print('ліва нога вперед')
    def leftlegbackforward(self):
        print('ліва нога назад')
    def rightlegforward(self):
        print('права нога вперед')
    def rightlegbackforward(self):
        print('права нога назад')
    def dansing(self):
        self.leftlegforward()
        self.leftlegbackforward()
        self.rightlegforward()
        self.rightlegbackforward()
        self.leftlegbackforward()
        self.rightlegbackforward()
        self.rightlegforward()
        self.leftlegforward()
    def __init__(self, prm):
        self.valueparam = prm
        print(self.valueparam)

Redginald = Giraf(100)
Redginald.dansing()
print(Redginald.valueparam)
