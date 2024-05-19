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
            #print(row)
            if "new_log" in row:
                if len(current_log) == 0:
                    print("first log")
                    formatted = row.replace("new_log ", "").replace("\n", "").split("-")
                    current_log.append(formatted)
                else:
                    print("new log")
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
                current_log.append(trim)
                
        log.close()
    logs.append(current_log)


def main():
    read_log_file()
    for log in logs:
        print(log)
        print("")

if __name__ == "__main__": main()

