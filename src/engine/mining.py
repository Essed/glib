
class Formula:
    def __init__(self, formula: str) -> None:
        self.__formula = formula
        self.__excluded_symbols = "\!,?|@&#<>~$:;"

    def parse_formula(self):
        inputs_symbols = [symbol for symbol in self.__formula if symbol in self.__excluded_symbols]

        print(inputs_symbols)
            

class Miner:
    def __init__(self) -> None:
        pass

    def mining(self) -> float:
        pass

    