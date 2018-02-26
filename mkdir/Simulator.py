from ShipLoad import *
from Flota import *
import random

import numpy as np

class Simulator():
    """Simulator engine """
    def __init__(self):
        self.shipload1 = Flota()
        self.shipload2 = Flota()

    def load_from_file(self,file1,file2):
        """Load data from file"""
        self.flota1 = self.shipload1.load_fleet(file1)
        self.flota2 = self.shipload2.load_fleet(file2)

    def load_from_list(self,file1,file2):
        """Load data from list"""
        self.flota1 = self.shipload1.load_list(file1)
        self.flota2 = self.shipload2.load_list(file2)

    def do_sim(self, rounds):
        """Function starting sim / rounds"""
        for i in range(0, rounds):
            self.attack()
            # for statek in self.flota1:
            #     statek.do_attack(self.flota2)

        if len(self.flota1)>0 and len(self.flota2)>0 or len(self.flota1)==0 and len(self.flota2) ==0:
            return None
        elif len(self.flota1)>0:
            return True
        else:
            return False


    def sym_result(self,sim_number):
        """Returning Simmulation Result"""
        flota1 = 0
        flota2 =0
        remis = 0

        for i in range(0,sim_number):
            # self.flota1.reset()
            # self.flota2.reset()
            result = self.do_sim(6)
            # import pdb; pdb.set_trace()
            a = self.wyniki1()
            b = self.wyniki2()
            if result:
                flota1 += 1
            elif result == None:
                remis +=1
            else:
                flota2 += 1
            if flota1>flota2 and flota1>remis:

                return ("Wygrała FLOTA NR 1 \nStan floty po walce:\n %s " %(a))
            elif flota1==flota2 or flota2<remis:

                return ("Remis! \nStan Floty nr 1:\n %s, \nStan Floty nr 2:\n %s" %(a,b))
            else:

                return ("Wygrała FLOTA NR 2 \nStan floty po walce:\n %s " %(b))

    def attack(self):
        """sequenially executes the attack function for each ship on the fleet list"""
        # import pdb; pdb.set_trace()
        for ship in self.flota1:
            if len(self.flota2) > 0:
                enemyShip = random.choice(self.flota2)
                ship.do_attack(enemyShip)

                while ship.SD_chance(enemyShip):
                    enemyShip = random.choice(self.flota2)
                    ship.do_attack(enemyShip)

        for ship in self.flota2:
            if len(self.flota1) > 0:
                enemyShip = random.choice(self.flota1)
                ship.do_attack(enemyShip)

                while ship.SD_chance(enemyShip):
                    enemyShip = random.choice(self.flota1)
                    ship.do_attack(enemyShip)

        not_destroyed1 = []
        not_destroyed2 = []


        for ship in self.flota1:
            if ship.isAlive():
                ship.shield_rege()
                not_destroyed1.append(ship)
            self.flota1 = not_destroyed1

        for ship in self.flota2:
            if ship.isAlive():
                ship.shield_rege()
                not_destroyed2.append(ship)
            self.flota2 = not_destroyed2

        # print(len(not_destroyed2))

        # print("-------------------------------------------")
    def wyniki1(self):
        """RETURN ALIVE SHIPS"""
        end = []
        final = []
        # mt = 0
        # dt = 0
        # lm = 0
        # cr = 0
        # kr = 0
        # sk = 0
        # re = 0
        # ss =0, b = 0, n = 0, gs =0, p = 0
        mt, dt, lm, cm, kr, sk, ow, re, ss, b, n, gs, p = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        koniec = ''
        for ship in self.flota1:
            if ship.shortname == 'mt':
                mt +=1
            elif ship.shortname == 'dt':
                dt +=1
            elif ship.shortname == 'lm':
                lm +=1
            elif ship.shortname == 'cm':
                cm +=1
            elif ship.shortname == 'kr':
                kr +=1
            elif ship.shortname == 'ow':
                ow +=1
            elif ship.shortname == 'sk':
                sk +=1
            elif ship.shortname == 're':
                re +=1
            elif ship.shortname == 'ss':
                ss +=1
            elif ship.shortname == 'b':
                b +=1
            elif ship.shortname == 'n':
                n +=1
            elif ship.shortname == 'gs':
                gs +=1
            elif ship.shortname == 'p':
                p +=1
        # import pdb; pdb.set_trace()
        end.append((mt,'Maly Transporter')), end.append((dt,'Duzy Transporter')) , end.append((lm,'Lekki Mysliwiec')), end.append((cm,'Ciezki Mysliwiec')), end.append((kr,'Krazownik')) , end.append((ow,'okret wojewnik'))
        end.append((sk,'statek kolonizacyjny')), end.append((re,'recykler')) , end.append((ss,'sonda szpiegowska')), end.append((n,'niszczyciel')),
        end.append((b,'bombowiec')) , end.append((gs,'gwiada smierci')), end.append((p,'pancernik'))
        for number in range(0,len(end)):
            if end[number][0] != 0:
                final.append(end[number])
                koniec += ' ' + str(end[number][1] + ': ' + str(end[number][0]) )
        return koniec
    def wyniki2(self):
        """RETURN ALIVE SHIPS"""

        end = []
        final = []
        # mt = 0
        # dt = 0
        # lm = 0
        # cr = 0
        # kr = 0
        # sk = 0
        # re = 0
        # ss =0, b = 0, n = 0, gs =0, p = 0
        mt, dt, lm, cm, kr, sk, ow, re, ss, b, n, gs, p = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        koniec = ''
        for ship in self.flota2:
            if ship.shortname == 'mt':
                mt +=1
            elif ship.shortname == 'dt':
                dt +=1
            elif ship.shortname == 'lm':
                lm +=1
            elif ship.shortname == 'cm':
                cm +=1
            elif ship.shortname == 'kr':
                kr +=1
            elif ship.shortname == 'ow':
                ow +=1
            elif ship.shortname == 'sk':
                sk +=1
            elif ship.shortname == 're':
                re +=1
            elif ship.shortname == 'ss':
                ss +=1
            elif ship.shortname == 'b':
                b +=1
            elif ship.shortname == 'n':
                n +=1
            elif ship.shortname == 'gs':
                gs +=1
            elif ship.shortname == 'p':
                p +=1
        # import pdb; pdb.set_trace()
        end.append((mt,'Maly Transporter')), end.append((dt,'Duzy Transporter')) , end.append((lm,'Lekki Mysliwiec')), end.append((cm,'Ciezki Mysliwiec')), end.append((kr,'Krazownik')) , end.append((ow,'okret wojewnik'))
        end.append((sk,'statek kolonizacyjny')), end.append((re,'recykler')) , end.append((ss,'sonda szpiegowska')), end.append((n,'niszczyciel')),
        end.append((b,'bombowiec')) , end.append((gs,'gwiada smierci')), end.append((p,'pancernik'))
        for number in range(0,len(end)):
            if end[number][0] != 0:
                final.append(end[number])
                koniec += ' ' + str(end[number][1] + ': ' + str(end[number][0]) )
        return koniec
    def __str__(self):
        return str(self.flota1)
    # def test(self):
    #     enemy = random.choice(self.flota1.fleet)
    #     print (enemy)
    #
    #     print (self.flota2)



# s = Simulator()
# s.load_from_file('flota_1.txt','flota_2.txt')
# # s.load_from_list([("mt",1),("dt",1)],[("kr",1),("dt",1)])
# print(s.sym_result(6))
