days = int(input("How many days you have studied?"))

hours = []

for day in range(days):
    hour = int(input(f"How many hours did you on day {day+1}"))
    hours.append(hour)

total_hours = sum(hours)
print("\nTotal hours", total_hours)
print("Average hours", round(total_hours/days,2))
print("Lowest study hours", min(hours))
print("Highest study hours", max(hours))

if total_hours >= 28:
    print("\n goal met")
else:
    print("\ngoal not met")