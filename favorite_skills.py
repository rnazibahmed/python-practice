skills = []

for i in range(5):
    skill = input(f"Enter skill {i+1}: ")
    skills.append(skill)

print("\n--- Your Skill List ---")

for skill in skills:
    print("-",skill)

print("Total skills:",len(skills))
