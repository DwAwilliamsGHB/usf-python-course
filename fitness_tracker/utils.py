import csv

GOAL_KEY = "GOAL_ENTRY"

class StepEntry:
    def __init__(self, date: str, steps: int):
        self.date = date
        self.steps = steps

    def __str__(self):
        return f"{self.date}: {self.steps} steps"

def read_data(filename):
    entries = []
    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                entries.append(StepEntry(row["date"], int(row["steps"])))
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with empty data.")
    return entries

def write_data(filename, entries):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "steps"])
        for entry in entries:
            writer.writerow([entry.date, entry.steps])

def get_goal(entries):
    for entry in entries:
        if entry.date == GOAL_KEY:
            return entry.steps
    return 10000  # default goal if not found

def set_goal(entries, new_goal):
    for entry in entries:
        if entry.date == GOAL_KEY:
            entry.steps = new_goal
            return
    entries.append(StepEntry(GOAL_KEY, new_goal))
