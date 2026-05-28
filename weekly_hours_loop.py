total_hours = 0

for day in range(1,8):
    hours = int(input(f"Enter study hours for day {day}: "))
    total_hours = total_hours + hours

print("\n-- weekly Study Summary ---")
print("Total study hours:", total_hours)
print("Average study hours per day:", total_hours / 7 )

if total_hours >= 28:
    print("You met your weekly goal.")
else:
    print("You did not meet your weekly goal")