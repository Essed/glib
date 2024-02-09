from game import player, coin, wallet
from game import unit
from game import battle
from game import trade
from game import inventory
from game import quest
from game import resources

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
    
    
    gen = unit.StatsCompiler(100, 25, 30, 5)
    stats_ = gen.compile_stats()
    d3 = unit.Dinosaur("Invoker", stats_["Race"], stats_['level'], stats_['AttackType'], stats_['damage'], stats_['Rarity'], stats_['armor'], stats_['hp'])
    d3.show()

    i1 = inventory.Inventory()
    i1.add_item(d1, 1)
    i1.show()
    i1.acquire_item(d1)
    i1.show()
    print(i1.count_items())

    q1 = quest.Quest("Q_Quest", 25)
    print(q1.get_quest_name())
    print(q1.is_complete())
    print(q1.get_award())

    e1 = resources.Energy(10,5)
    print(e1.get_max_quantity())
    print(e1.get_quantity())
    e1.consume(4)
    print(e1.get_quantity())
    e1.increase(3)
    print(e1.get_quantity())
    e1.refresh()
    print(e1.get_quantity())
    e1.upgrade_max_energy(100)
    print(e1.get_max_quantity())


    udb1 = unit.UnitDatabase()
    udb1.add_unit(d1)
    print(udb1.get_units())
    udb1.add_units([d2, d3])
    print(udb1.get_units())


    ug1 = unit.UnitGenerator(udb1)
    print("Generated unit:", ug1.generate_unit())
  