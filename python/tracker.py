
from Session import Session
from Challenge import Challenge
from Data_processor import Data_processor
from File_handler import File_handler

logs = []

def main():
    #Open and read file
    fh = File_handler()
    sessions: list[Session] = []
    logs = fh.read_log_file("full_log.txt")
    for log in logs:
        sessions.append(Session(log))
    
    processor = Data_processor(sessions)
    #Process data here with Data_processor
    processor.split_challenge_types()
    processor.filter_and_validate_based_on_playtime(120)
    processor.calculate_avgs_for_all_gamemodes()

    fh.export_json("report/data.json", sessions, processor.with_averages)

if __name__ == "__main__": main()

