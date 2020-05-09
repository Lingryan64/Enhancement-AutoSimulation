import random
import statistics
from collections import deque
class Weapon():
    
    windProcs = 0
    frostProcs = 0 
    totalNone = 0
    totalWind = 0
    totalRock = 0
    totalFrost = 0
    
    def __init__(self, dX, dY, speed):
        self.dX = dX
        self.dY = dY
        self.speed = speed
        
    def getSpeed(self):
        return self.speed
    
#damage that will be added to base, includes proc chances
    def windFury(self):
        if random.randint(0,100) <= 20:
            Weapon.windProcs += 1
            return self.getDph() + self.getDph()
        else:
            return 0

    def frostBrand(self):
        procChance = (9 / (60 / self.getSpeed())) * 100
                      
        if random.randint(0,100) <= procChance:
            Weapon.frostProcs += 1
            return 187
        else:
            return 0
    
    def rockBiter(self):
        return (194 / 14) * self.getSpeed()
    
    def getFrostProcs(self):
        return Weapon.frostProcs
    
    def getWindProcs(self):
        return Weapon.windProcs

    def getTotalNone(self):
        return self.totalNone

    def getTotalWind(self):
        return self.totalWind
    
    def getTotalFrost(self):
        return self.totalFrost
    
    def getTotalRock(self):
        return self.totalRock
    
class Swinger(Weapon):
    
    def __init__ (self, dX, dY, speed, enh):
        Weapon.__init__(self, dX, dY, speed)
        self.enh = str(enh)

    def getDph(self): 
        dph = random.randint(self.dX, self.dY)
        self.totalNone += dph
        return dph
    
    def getTrueDph(self):
        if self.enh == 'windfury':
            self.totalWind += self.getDph() + self.windFury() 
            return self.getDph() + self.windFury()
        
        if self.enh == 'frostbrand':
            self.totalFrost += self.getDph() + self.frostBrand() 
            return self.getDph() + self.frostBrand()
        
        if self.enh == 'rockbiter':
            self.totalRock += self.getDph() + self.rockBiter() 
            return self.getDph() + self.rockBiter()
        
    def setEnh(self, x):
        self.enh = str(x)



        
