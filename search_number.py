num = int(input("How many numbers do you want to enter? "))

numbers = []
for i in range(num):
    temp = int(input("Please enter number: "))
    numbers.append(temp)

target = int(input("what is your target number? "))

found = False
for number in numbers:
    if target == number:
        found = True

if found == True:
    print("Target found")
else: 
    print("Target not found")