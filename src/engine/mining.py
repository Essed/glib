
class Formula:
    def __init__(self, formula: str) -> None:
        self.__formula = formula
        self.__excluded_symbols = "\!,?|@&#<>~$:;"

    async def parse_formula(self):
        inputs_symbols = [symbol for symbol in self.__formula if symbol in self.__excluded_symbols]

        if len(inputs_symbols) != 0:
            raise ValueError("Unacceptable experssion")
        
        return self.__formula
            
    

class Miner:
    def __init__(self, formula: Formula) -> None:
        self.__formula = formula

    async def mining(self) -> float:
        return eval(self.__formula.parse_formula())

    