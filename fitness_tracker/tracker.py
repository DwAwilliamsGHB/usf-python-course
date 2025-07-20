import time
from utils import StepEntry, read_data, write_data, get_goal, set_goal, GOAL_KEY
from datetime import datetime

FILENAME = "steps_data.csv"

def add_new_entry(entries):
    print("\nWould you like to:")
    print("1. Use today's date")
    print("2. Enter a different date")
    choice = input("Choose an option: ")

    if choice == "1":
        date_str = datetime.today().strftime("%Y-%m-%d")
    elif choice == "2":
        date_str = input("Enter the date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("⚠️ Invalid date format.")
            return
    else:
        print("⚠️ Invalid choice.")
        return

    existing_entry = next((e for e in entries if e.date == date_str), None)
    if existing_entry:
        print(f"\n⚠️ Entry already exists for {date_str}: {existing_entry.steps} steps")
        print("1. Overwrite")
        print("2. Discard new entry")
        decision = input("Choose an option: ")

        if decision != "1":
            print("❌ Entry discarded.")
            return

    steps = input("Enter number of steps: ")
    if not steps.isdigit():
        print("⚠️ Please enter a valid number.")
        return

    if existing_entry:
        existing_entry.steps = int(steps)
        print(f"🔁 Overwritten: {date_str}: {steps} steps")
    else:
        entry = StepEntry(date_str, int(steps))
        entries.append(entry)
        print(f"✅ Added: {entry}")


def average_steps(entries):
    step_entries = [e for e in entries if e.date != GOAL_KEY]
    if not step_entries:
        print("⚠️ No step entries to calculate average.")
        return
    avg = sum(e.steps for e in step_entries) / len(step_entries)
    print(f"📊 Average steps: {round(avg)}")


def goal_menu(entries):
    current_goal = get_goal(entries)
    print(f"\n🎯 Current Step Goal: {current_goal} steps")
    print("1. Change goal")
    print("2. Keep current and track progress")
    choice = input("Choose an option: ")

    if choice == "1":
        new_goal = input("Enter new step goal: ")
        if new_goal.isdigit():
            set_goal(entries, int(new_goal))
            print(f"✅ Step goal updated to {new_goal}")
        else:
            print("⚠️ Please enter a valid number.")
    elif choice == "2":
        today = input("Enter today’s steps to track progress: ")
        if today.isdigit():
            today_steps = int(today)
            if today_steps >= current_goal:
                print("🎉 You hit your goal today!")
            else:
                print(f"🚶 Keep going! You're {current_goal - today_steps} steps away.")
        else:
            print("⚠️ Please enter a valid number.")
    else:
        print("⚠️ Invalid choice.")


def main():
    entries = read_data(FILENAME)

    while True:
        print("\n--- Fitness Tracker ---")
        print("1. Add new entry")
        print("2. View all entries")
        print("3. View average steps")
        print("4. Step Goal Menu")
        print("5. Save and exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_new_entry(entries)
        elif choice == "2":
            for e in entries:
                if e.date != GOAL_KEY:
                    print(e)
        elif choice == "3":
            average_steps(entries)
        elif choice == "4":
            goal_menu(entries)
        elif choice == "5":
            write_data(FILENAME, entries)
            print("✅ Data saved. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice.")

        time.sleep(1.5)


if __name__ == "__main__":
    main()
