from engine.unit import AttackType, Race, Rarity, Unit

class Mammoth(Unit):
    def __init__(self, name, race: Race, level: int, attack_type: AttackType, damage: float, rarity: Rarity, armor: float, hp: float) -> None:
        super().__init__(name, race, level, attack_type, damage, rarity, armor, hp)