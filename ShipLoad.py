#-*- coding: utf-8 -*-

class ShipLoad(object):
    """Class for loading game data from files"""
    def __init__(self):
        super(ShipLoad, self).__init__()
        self.ship_data = self.add_ship()
        self.ship_sd = self.add_fast_cannon()
        self.a = []



    def add_ship(self):
        """add Ships from file"""
        ships = []
        dane_statkow = open('./dane/dane_statkow.txt').readlines()[1:]
        for i in dane_statkow:
            ships.append(i.rsplit())
        return ships
    def add_fast_cannon(self):
        """add Cannon from szybkie_dziala.txt"""
        szybkie_dziala = []
        szybkie_dziala_file = open('./dane/szybkie_dziala.txt').readlines()

        for i in szybkie_dziala_file:
            szybkie_dziala.append(i.rsplit())
        return szybkie_dziala


    def get_data(self,short_name):
        """Getting specific data ex. mt"""
        len_list = len(self.ship_data)
        for i in range(len_list):
            if self.ship_data[i][0] == short_name:
                return self.ship_data[i]
            i+=1
        return None
    def get_fast_cannon_data(self,shortname):
        """Getting specific data ex. mt"""
        len_list = len(self.ship_sd)
        for i in range(1,len_list):
            if self.ship_sd[i][0] == shortname:
                return self.ship_sd[i]
            i +=1
        return None
a = ShipLoad()
asd = a.add_ship()
# print(ship1.get_fast_cannon_data('mt'))
