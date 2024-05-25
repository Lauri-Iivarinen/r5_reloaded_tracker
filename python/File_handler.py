import json
from Challenge import Challenge
from Session import Session
from Gamemode import Gamemode

class File_handler:

    def num(self,s): #Convert string to either int or float based on input given
        try:
            return int(s)
        except ValueError:
            return float(s)


    def read_log_file(self, filename: str):
        self.logs = []
        current_log = []
        with open(filename) as log:
            for row in log.readlines():
                if "new_log" in row:
                    if len(current_log) == 0:
                        formatted = row.replace("new_log ", "").replace("\n", "").split("-")
                        current_log.append(formatted)
                    else:
                        #print(len(current_log))
                        self.logs.append(current_log)
                        current_log = []
                        formatted = row.replace("new_log ", "").replace("\n", "").split("-")
                        current_log.append(formatted)
                elif "===" not in row and "ChallengeName" not in row and row != "\n":
                    trim = []
                    row = row.replace("\n", "").strip().split(",")
                    for i in range(0, len(row)):
                        string = row[i].strip()
                        if (i != 0 and i != 3):
                            string = self.num(string)
                        trim.append(string)
                    challenge = Challenge(trim)
                    if challenge.approved:
                        current_log.append(challenge)
                    
            log.close()
        self.logs.append(current_log)
        self.files[filename] = self.logs
        return self.logs

    def convert_logs_json(self, data: list[Session], gamemodes: list[Gamemode]):
        file = {}
        sessions = []
        for log in data:
            jsons = []
            for i in range(1, len(log.challenges)):
                jsons.append(log.challenges[i].format_json())
            dictionary = {"date": log.date, "time": log.time, "challenges": jsons}
            sessions.append(dictionary)
        file["sessions"] = sessions
        parsed = []
        for mode in gamemodes:
            parsed.append(mode.format_json())
        file["gamemodes"] = parsed
        return file

    def export_json(self, fname, sessions: list[Session], gamemodes):
        with open(f'{fname}', 'w') as f:
            json.dump(self.convert_logs_json(sessions, gamemodes), f)
    
    def __init__(self) -> None:
        self.logs = []
        self.files = {}
        pass

