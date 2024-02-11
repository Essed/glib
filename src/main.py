from engine import player, coin, wallet
from engine import unit
from engine import battle
from engine import trade
from engine import inventory
from engine import quest
from engine import resources
from engine import clan
from engine import mining

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
    t1.set_content_for_trader(pl2, d1)


    t1.show()
    t1.swap()
    t1.show()
    
    
    gen = unit.StatsCompiler(100, 25, 30, 5)
    stats_ = gen.compile_stats()
    d2 = unit.Dinosaur("Invoker", stats_["Race"], stats_['level'], stats_['AttackType'], stats_['damage'], stats_['Rarity'], stats_['armor'], stats_['hp'])
    d2.show()

    i1 = inventory.Inventory()
    i1.add_item(d1, 1)
    i1.add_item(d2, 1)
    i1.show()
    i1.acquire_item(d1)
    i1.acquire_item(d2)
    i1.show()
    print("IS Acquired item: ", i1.is_acquired(d1))
    print("Acquired items: ", i1.get_acquired_items()) 
    i1.unacquire_item(d2)
    print("Acquired items: ", i1.get_acquired_items())
    print(i1.count_items())

    q1 = quest.Quest("Quest1", 25, 3600, "Quest description", "www.google.com")
    print(q1.get_quest_name())
    print(q1.is_complete())
    print(q1.get_award())
    print(q1.get_finish_time())
    print(q1.get_quest_url())
    print(q1.get_description())

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
    udb1.add_units([d2])
    print(udb1.get_units())

    d3 = p1.instance_unit(udb1)
    udb1.add_unit(d3)
    print(udb1.get_units())

    ug1 = unit.UnitGenerator(udb1)
    print("Generated unit:", ug1.generate_unit())
  
    cl1 = clan.Clan("Winners", "WIN", pl1)
    cl1.accept(pl1)
    cl1.accept(pl2)
    print(cl1.get_members())
    print(cl1.get_members_nickname())
    cl1.kick("Any")
    print(cl1.get_members())
    print(cl1.get_clan_leader())
    cl1.set_leadership("Askme")
    print(cl1.get_clan_leader())
    cl1.status()
    print(cl1.status())
    cl1.level_up(1)
    print(cl1.status())
    f1 = mining.Formula("!10+2*5:,!?")
    f1.parse_formula()
