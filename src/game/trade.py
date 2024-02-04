from game import player



class Swapper:
    def __init__(self) -> None:       
        self.__elements = list()

    def add_element(self, element):
        self.__elements.append(element)

    def swap(self):       
        if len(self.__elements) == 2:       
            first, second = tuple(self.__elements)
            self.__elements.clear()
            self.add_element(second)
            return list((second, first))
    
    def get_elements(self):
        return self.__elements
    
    def show(self):
        print(self.__elements)




class Container:
    def __init__(self, contents: list) -> None:
        self.__contents = contents
        print(self.__contents)
    
    def swap(self):
        swapper = Swapper()
        result = list()
        for content in self.__contents:
            swapper.add_element(content)
            result = swapper.swap()
        return result
      


class Trade:
    def __init__(self, count_members) -> None:
        self.__traders = dict()
        self.__count_members = count_members 

    def add_trader(self, player: player.Player) -> None:
        if len(self.__traders) < self.__count_members:
            self.__traders[player] = None

    def get_traders(self) -> dict:
        return self.__traders

    def put_in(self, player: player.Player, content):
        if player in self.__traders.keys():
            self.__traders[player] = content

    def swap(self):        
        ct = Container(list(self.__traders.values()))
        ct.swap()

    def show(self) -> None:
        print(self.__traders)
