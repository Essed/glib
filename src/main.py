from game import player, coin, wallet
from game import unit
from game import battle
from game import trade

if __name__ == "__main__":

    pl1 = player.Player("Any")
    c1 = coin.Coin("Dyno") 
    w1 = wallet.Wallet(pl1, 1.99)
    w1.set_coin(c1.get_name())
    
    print(w1.get_balance(), w1.get_coin())
    w1.show()

    d1 = unit.Dinosaur("Rex", unit.Race.ROCK, 1, unit.AttackType.MELEE, 18, unit.Rarity.RARE, 9, 100)
    d1.show()
    d1.apply_damage(3)
    d1.show()
    d1.set_experience_for_up(100)
    d1.add_experience(50)
    d1.show()
    d1.add_experience(50)
    d1.show()
    if d1.try_levelup():
        d1.level_up()
        d1.reset_experience()
        d1.set_experience_for_up(200)
    d1.show()
    p1 = battle.PVE(30)
    p1.add_unit(d1)

    for un in p1.get_units():
        un.show()

    print(p1.get_start_time())
    p1.set_finish_time()
    print(p1.get_finish_time())
    p1.progress_unit(210)
    d1.shift_experience()
    for un in p1.get_units():
        un.show()
    d2 = p1.instance_unit()
    d2.show()
     
    pl2 = player.Player("Askme")
    t1 = trade.Trade(2)
    t1.add_trader(pl1)
    t1.show()
    t1.add_trader(pl2)
    t1.show()
    pl3= player.Player("MSK")
    t1.add_trader(pl3)
    t1.show()

    t1.set_content_for_trader(pl1, d1)
    t1.set_content_for_trader(pl2, d2)


    t1.show()
    t1.swap()
    t1.show()
  