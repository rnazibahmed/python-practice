appearance = {}

num = int(input("How many numbers do you want to enter? "))

for i in range(num):
    temp = int(input("Please enter your number: "))
    if temp in appearance:
        appearance[temp] += 1
    else:
        appearance[temp] = 1
max_encounter = 0
most_frequent = None
for key,value in appearance.items():
    if value > max_encounter:
        most_frequent = key
        max_encounter = value

print("Most Frequent Number: ", most_frequent)
print("Frequency: ", max_encounter)


