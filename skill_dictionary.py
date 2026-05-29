profile = {
    "name": "Rezoan",
    "goal": "AI/ML Engineer",
    "main_language": "Python",
    "daily_hours": 4
}

print("--- Profile Summary ---")

for key,value in profile.items():
    print(key, ":", value)

profile["weekly_hours"] = profile["daily_hours"] * 7

print("\nUpdated weekly hours:", profile["weekly_hours"])