appearance = {}

num = int(input("How many numbers do you want to enter? "))

for i in range(num):
    temp = int(input("Please enter your number: "))
    if temp in appearance:
        appearance[temp] += 1
    else:
        appearance[temp] = 1
min_encounter = 0
least_frequent = None
counter = 0
for key,value in appearance.items():
    if counter == 0:
        least_frequent = key
        min_encounter = value
        counter += 1
    if counter > 0 and value < min_encounter:
        least_frequent = key
        min_encounter = value

print("Least Frequent Number: ", least_frequent)
print("Frequency: ", min_encounter)


