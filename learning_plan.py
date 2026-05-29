learning_plan = {
    "week": 1,
    "topic": "Python Basics",
    "tasks": ["variables", "loops", "functions", "lists", "dictionaries"]
}

print("--- Learning Plan ---")
print("Week:", learning_plan["week"])
print("Topic", learning_plan["topic"])

print("\nTasks:")

for task in learning_plan["tasks"]:
    print("-", task)

print("\nTotal tasks:", len(learning_plan["tasks"]))
