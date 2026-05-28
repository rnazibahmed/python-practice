def calculate_weekly_hours(daily_hours):
    total = sum(daily_hours)
    average = total / len(daily_hours)
    return total, average

hours_list = []

for day in range(1,8):
    hours = int(input(f"Enter study hours for day {day}: "))
    hours_list.append(hours)

total_hours, average_hours = calculate_weekly_hours(hours_list)

print("\n--- Weekly Study Summary ---")
print("Total study hours:", total_hours)
print("Average study hours per day:", round(average_hours,2))

if total_hours >= 28:
    print("You met your weekly goal.")
else:
    print("You did not meet your weekly goal.")