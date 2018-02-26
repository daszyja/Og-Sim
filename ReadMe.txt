lass Simulator.Simulator
Simulator engine

attack()
sequenially executes the attack function for each ship on the fleet list

do_sim(rounds)
Function starting sim / rounds

load_from_file(file1, file2)
Load data from file

load_from_list(file1, file2)
Load data from list

sym_result(sim_number)
Returning Simmulation Result

wyniki1()
RETURN ALIVE SHIPS

wyniki2()
RETURN ALIVE SHIPS

Flota.random() → x in the interval [0, 1).
class Ship.Ship(short_name)
Class containing basic fleet operations and game functions

destroy()
Destroy

dmg(other)
dmg function here we’re changing life level

do_attack(other)
Function calling dmg other ship and checking if it’s destroyed

isAlive()
Check if sheep is alive

class ShipLoad.ShipLoad
Class for loading game data from files

add_fast_cannon()
add Cannon from szybkie_dziala.txt

add_ship()
add Ships from file

get_data(short_name)
Getting specific data ex. mt

get_fast_cannon_data(shortname)
Getting specific data ex. mt
