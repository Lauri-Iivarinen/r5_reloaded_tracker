
from Session import Session
from Challenge import Challenge
from Gamemode import Gamemode

class Data_processor:

    def split_challenge_types(self):
        challenge_types: dict[str, list[Challenge]] = {}
        for session in self.sessions:
            for challenge in session.challenges:
                if challenge.gamemode not in challenge_types:
                    challenge_types[challenge.gamemode] = []
                cht = challenge_types[challenge.gamemode]
                cht.append(challenge)
        
        self.split_by_gamemode = challenge_types
    
    def filter_and_validate_based_on_playtime(self, time: int): #Players can set the usual gametime they use to practise, this can filter out all test runs etc
        dct: dict[str, list[Challenge]] = {}
        for key in self.split_by_gamemode:
            arr = []
            for challenge in self.split_by_gamemode[key]:
                if challenge.duration == time and challenge.approved:
                    arr.append(challenge)
            if len(arr) != 0:
                dct[key] = arr
            
        self.filtered_by_duration_and_mode = dct

    def calc_avgs(self, arr: list[Challenge]) -> dict [str, float]:
        accuracy = 0
        damage = 0
        kills = 0
        hits = 0
        shots = 0
        for challenge in arr:
            accuracy = accuracy + challenge.accuracy
            damage = damage + challenge.damage
            kills = kills + challenge.kills
            hits = hits + challenge.hits
            shots = shots + challenge.shots
        
        size = len(arr)
        return {
            "accuracy" : accuracy/size,
            "damage" : damage/size,
            "kills" : kills/size,
            "hits" : hits/size,
            "shots" : shots/size,
        }
    
    def calculate_avgs_for_all_gamemodes(self):
        gamemodes: list[Gamemode] = []
        for key in self.filtered_by_duration_and_mode:
            averages = self.calc_avgs(self.filtered_by_duration_and_mode[key])
            averages["challenges"] = self.filtered_by_duration_and_mode[key]
            gamemodes.append(Gamemode(averages, key))
        
        self.with_averages = gamemodes


    def __init__(self, lst: list[Session]) -> None:
        self.sessions = lst