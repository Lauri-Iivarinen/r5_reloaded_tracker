class Challenge:

    def should_be_ignored(self):
        self.approved = True
        if self.shots == 0 and self.damage == 0:
            self.approved = False
    
    def format_json(self):
        return {
            "gamemode" : self.gamemode,
            "hits" : self.hits,
            "kills" : self.kills,
            "weapon" : self.weapon,
            "accuracy" : self.accuracy,
            "damage" : self.damage,
            "crits" : self.crits,
            "shots" : self.shots,
            "time" : self.time
        }


    def __init__(self, array) -> None:
        self.gamemode = array[0]
        self.hits = array[1]
        self.kills = array[2]
        self.weapon = array[3]
        self.accuracy = array[4]
        self.damage = array[5]
        self.crits = array[6]
        self.shots = array[7]
        self.time = array[8]

        self.should_be_ignored()
