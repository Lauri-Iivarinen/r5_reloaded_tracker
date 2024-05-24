
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

    fh.export_json("data.json", sessions)

if __name__ == "__main__": main()

