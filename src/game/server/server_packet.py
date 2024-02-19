
class Packet:
    def __init__(self) -> None:
        self.__data = None

    def pack(self):
        return self.__data
    
    def load_data(self, data):
        self.__data = data