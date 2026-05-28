name = input("Enter your name: ")
hours = int(input("How many hours did you study today? "))

weekly_goal = hours * 7
print("\n--- Daily Report ---")
print("Name:", name)
print("Daily Study Hours:", hours)
print("Projected Weekly Hours:", weekly_goal)

if weekly_goal >= 28:
    print("Excellent consistancy")
else:
    print("You should increase your study hours.")