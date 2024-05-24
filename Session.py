from Challenge import Challenge

class Session:

    def print(self):
        print(len(self.challenges))

    def __init__(self, arr: list) -> None:
        self.date: str = arr[0][0]
        self.time: str = arr[0][1]
        self.challenges: list[Challenge] = arr[1:len(arr)]
    