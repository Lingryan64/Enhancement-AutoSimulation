import statistics, math
from matplotlib import pyplot as plt
from matplotlib import colors as mcolors
from myLib import Swinger
from collections import deque
f = open('Boss Fight Timing.txt', 'r')
data = f.read()
f.close()
data = data.split()
data = list(map(int,data))
meanT = round((statistics.mean(data)),0)
repeat = True
while repeat == True:
    x = input("Please enter your weapons low end damage: ")
    y = input("Please enter your weapons high end damage: ")
    z = input("Please enter your weapons attack speed in seconds: ")

    char = Swinger(int(x), int(y), float(z), 4)
    hits = math.floor(meanT / char.getSpeed())

    noEnh = deque()
    wind = deque()
    rock = deque()
    frost = deque()
    for i in range(0, hits):
        
        noEnh.append(round(char.getDph(),0))

        char.setEnh("windfury")
        wind.append(round(char.getTrueDph(),0))

        char.setEnh("rockbiter")
        rock.append(round(char.getTrueDph(),0))

        char.setEnh("frostbrand")
        frost.append(round(char.getTrueDph(),0))
                
              
    def graphDPH():
        hitsList = [i for i in range(hits)]
        
        plt.plot(hitsList, noEnh, label= 'Base total dmg ['+ str(char.getTotalNone())+']')
        plt.plot(hitsList, wind, label = 'Windfury total dmg ['+ str(char.getTotalWind()) + '] procs( '+ str(char.getWindProcs()) + ')')
        plt.plot(hitsList, rock, label = 'Rockbiter total dmg ['+ str(char.getTotalRock())+ ']')
        plt.plot(hitsList, frost, label = 'Frostbrand total dmg ['+ str(char.getTotalFrost()) + '] procs( '+ str(char.getFrostProcs()) + ')]')
        plt.legend()
        plt.title('Damage per Hit')
        plt.xlabel("Number of Hits within " + str(round(meanT))+ " seconds")
        plt.ylabel("Damage")
        plt.show()


    graphDPH()

    log = open('Logs.txt', 'a')
    log.write("no enhancement damage : [" + str(char.getTotalNone()) +"]" + "\n" + "Windfury damage : [" + str(char.getTotalWind()) + "] procs (" + str(char.getWindProcs()) + ")" + "\n")
    log.write("Rockbiter total dmg : [" + str(char.getTotalRock()) + "]" + "\n" + "Frostbrand Damage : [" + str(char.getTotalFrost()) + "] procs(" + str(char.getFrostProcs()) + ")")
    log.write("\n" + "\n")
    log.close()

    promp = input("simulate again? (y) | (n) :")
    if promp == "n":
        repeat = False
