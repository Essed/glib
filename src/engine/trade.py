from engine import actor



class Swapper:
    def __init__(self) -> None:       
        self.__elements = list()

    async def add_element(self, element):
        self.__elements.append(element)

    async def swap(self):       
        if len(self.__elements) == 2:       
            first, second = tuple(self.__elements)
            self.__elements.clear()
            self.add_element(second)
            return list((second, first))
    
    async def get_elements(self):
        return self.__elements
    
    async def show(self):
        print(self.__elements)



class Container:
    def __init__(self, contents: list) -> None:
        self.__contents = contents
        self.__cursor = 0
    
    async def swap(self):
        swapper = Swapper()
        for content in self.__contents:
            swapper.add_element(content)
            self.__contents = swapper.swap()

    async def pop_first(self):
        content = self.__contents[self.__cursor]
        self.__contents.pop(self.__cursor)
        return content
    
    async def get_contents(self):
        return self.__contents



class Trade:
    def __init__(self, count_members) -> None:
        self.__traders = dict()
        self.__count_members = count_members 

    async def add_trader(self, actor: actor.Actor) -> None:
        if len(self.__traders) < self.__count_members:
            self.__traders[actor] = None

    async def get_traders(self) -> dict:
        return self.__traders

    async def set_content_for_trader(self, actor: actor.Actor, content):
        if not self.__traders[actor]:
            self.__traders[actor] = content

    async def swap(self):        
        container = Container(list(self.__traders.values()))
        container.swap()
        for trader in self.__traders.keys():
            self.__traders[trader] = container.pop_first() 

    async def show(self) -> None:
        print(self.__traders)
