from datetime import datetime, timedelta

# 1. Display current time with item & cost
sample_data = "2025-06-29\t11:23:00\tPublix\tMilk\t3.25\tCredit"
data = sample_data.strip().split("\t")
if len(data) == 6:
    _, _, _, item, cost, _ = data
    print("Current time:", datetime.now())
    print(f"Item: {item}\tCost: {cost}")

# 2. Add 2 years and subtract 60 seconds
now = datetime.now()
future = now + timedelta(days=730) - timedelta(seconds=60)
print("Modified time:", future)

# 3. Create specific timedelta
d = timedelta(days=100, hours=10, minutes=13)
print("Timedelta:", d)

# 4. Function with 2 arguments + datetime
def print_height_with_time(feet, inches):
    print(f"Height: {feet} ft, {inches} in — Time: {datetime.now()}")

print_height_with_time(6, 1)
