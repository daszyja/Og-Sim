#-*- coding: utf-8 -*-
from ShipLoad import *
import random


class Ship():
    """
    Class containing basic fleet operations and game functions
    """
    def __init__(self, short_name):
        """
        Creates Ship data using short name
        :type short_name: string
        :param short_name: shortname of sheep
        """
        self.data = ShipLoad().get_data(short_name)
        self.sd = ShipLoad().get_fast_cannon_data(short_name)
        self.shortname = short_name
        self.longname = self.data[1]
        self.structual_p = int(self.data[2])
        self.shield = int(self.data[3])
        self.attack = int(self.data[4])
        self.alive = True
    def __str__(self):
        return ("Nazwa skrocona : %s pełna nazwa: %s, Punkty Strukturalne: %s, Obrona: %s Atak: %s" % (self.shortname, self.longname, self.structual_p, self.shield, self.attack))

    def __repr__(self):
        return ("Nazwa skrocona : %s pełna nazwa: %s, Punkty Strukturalne: %s, Obrona: %s Atak: %s" % (self.shortname, self.longname, self.structual_p, self.shield, self.attack))

    def SD_chance_get(self, enemy):
        ships = ShipLoad().add_fast_cannon()
        a = len(ships)
        st = 0
        for i in range(1, a):
            if (enemy == ships[i][0]):
                st = i
                return self.sd[st]
            i += 1
        return 0

    def SD_chance(self, enemy):
        a = float(self.SD_chance_get(enemy))
        if a > 0:
            a1 = random.uniform(0, 1)
            return a >= a1
        else:
            return False

    def do_attack(self, other):
        """
        Function calling dmg other ship and checking if it's destroyed
        """
        # import pdb; pdb.set_trace()
        self.dmg(other)
        if other.destroy() or other.structual_p <= 0:
            other.structual_p = 0
            other.alive = False

    def destroy(self):
        """
        Destroy
        """
        if self.structual_p < float(self.data[2]) * 0.7:
            bum = 1.0 - ((float(self.structual_p)) / float(self.data[2]))
            bum_chance = random.uniform(0, 1)
            return bum_chance < bum
        else:
            return False

    def dmg(self, other):
        """
        dmg function here we're changing life level
        """
        self.shield = float(self.shield)
        self.attack = float(self.attack)
        if (self.shield * 0.01) < self.attack:
            if self.shield > 0:
                other.shield = float(other.shield)
                other.shield -= self.attack
            else:
                other.structual_p = float(other.structual_p)
                other.structual_p -= self.attack
                # self.structual_p -= other.attack

            if other.shield < 0:
                other.structual_p += other.shield
                other.shield = 0

    def isAlive(self):
        """
        Check if sheep is alive
        """
        return self.alive

    def shield_rege(self):
        self.shield = self.data[3]


#
# s = Ship('lm')
# s1 = Ship('gs')
# s.do_attack(s1)
# print (s)
# print(s.isAlive)
