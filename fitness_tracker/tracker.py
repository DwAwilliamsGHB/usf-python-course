from utils import StepEntry, read_data, write_data
from datetime import datetime

FILENAME = "steps_data.csv"

def add_new_entry(entries):
    date_str = input("Enter the date (YYYY-MM-DD): ")
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return

    steps = input("Enter number of steps: ")
    if not steps.isdigit():
        print("Please enter a valid number.")
        return

    entry = StepEntry(date_str, int(steps))
    entries.append(entry)
    print(f"Added: {entry}")

def average_steps(entries):
    if not entries:
        print("No data available.")
        return
    avg = sum(entry.steps for entry in entries) / len(entries)
    print(f"Average steps: {round(avg)}")

def main():
    entries = read_data(FILENAME)

    while True:
        print("\n--- Fitness Tracker ---")
        print("1. Add new entry")
        print("2. View all entries")
        print("3. View average steps")
        print("4. Save and exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_new_entry(entries)
        elif choice == "2":
            for e in entries:
                print(e)
        elif choice == "3":
            average_steps(entries)
        elif choice == "4":
            write_data(FILENAME, entries)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
