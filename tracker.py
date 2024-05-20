from Challenge import Challenge
import json


logs = []


def num(s): #Convert string to either int or float based on input given
    try:
        return int(s)
    except ValueError:
        return float(s)


def read_log_file():
    current_log = []
    with open("full_log.txt") as log:
        for row in log.readlines():
            if "new_log" in row:
                if len(current_log) == 0:
                    formatted = row.replace("new_log ", "").replace("\n", "").split("-")
                    current_log.append(formatted)
                else:
                    print(len(current_log))
                    logs.append(current_log)
                    current_log = []
                    formatted = row.replace("new_log ", "").replace("\n", "").split("-")
                    current_log.append(formatted)
            elif "===" not in row and "ChallengeName" not in row and row != "\n":
                trim = []
                row = row.replace("\n", "").strip().split(",")
                for i in range(0, len(row)):
                    string = row[i].strip()
                    if (i != 0 and i != 3):
                        string = num(string)
                    trim.append(string)
                challenge = Challenge(trim)
                if challenge.approved:
                    current_log.append(challenge)
                
        log.close()
    logs.append(current_log)

def convert_logs_json():
    file = []
    for log in logs:
        date = log[0][0]
        time = log[0][1]
        jsons = []
        for i in range(1, len(log)):
            jsons.append(log[i].format_json())
        dictionary = {"date": date, "time": time, "challenges": jsons}
        file.append(dictionary)
    return file

def export_json():
    with open('report/data.json', 'w') as f:
        json.dump(convert_logs_json(), f)

def main():
    read_log_file()
    for log in logs:
        #print(log)
        print("")
    export_json()

if __name__ == "__main__": main()

