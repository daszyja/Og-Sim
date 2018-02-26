from Ship import Ship
from random import random

class Flota(object):
    def __init__(self):
        self.fleet = []


    def load_fleet(self,fleetfile):
        """Load fleet from file"""
        f = open('./dane/'+fleetfile).readlines()
        ship_list = []
        ships_in_list = []

        for i in f:
            ship_list.append(i.rsplit())

        for j in range(0, len(ship_list) ):
            # import pdb; pdb.set_trace()
            for ship in range( 0, int(ship_list[j][1]) ):
                if ship > 0:
                    a = Ship(ship_list[j][0])
                    ships_in_list.append(a)


        # print (ships_in_list)
        # print(ship_list)
        # print(ship_in_list)
        self.fleet = ships_in_list
        return ships_in_list

    def load_list(self,fleetfile):
        """Load Fleet From LIST"""
        fleet = []

        for i in fleetfile:
            for j in range(0,i[1]):
                fleet.append(Ship(i[0]))

        self.fleet = fleet
        return fleet
    def __str__(self):
        return str(self.fleet)

    def __len__(self):
        return len(self.fleet)

    def __iter__(self):
        for i in range(0,len(self.fleet)):
            yield self.fleet[i]

# s = Flota()
# s.load_fleet('flota_1.txt')
