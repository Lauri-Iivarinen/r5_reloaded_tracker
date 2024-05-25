from Challenge import Challenge

class Gamemode:

    def format_json(self):
        chl = []
        for challenge in self.challenges:
            chl.append(challenge.format_json())
        return {
            "accuracy" : self.accuracy,
            "damage" : self.damage,
            "kills" : self.kills,
            "hits" : self.hits,
            "shots" : self.shots,
            "challenges": chl
        }

    def __init__(self, dct: dict) -> None:
        self.accuracy = dct["accuracy"]
        self.damage = dct["damage"]
        self.kills = dct["kills"]
        self.hits = dct["hits"]
        self.shots = dct["shots"]
        self.challenges: list[Challenge] = dct["challenges"]