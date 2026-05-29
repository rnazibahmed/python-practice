num = int(input("How many numbers do you want to enter? "))

numbers = []
for i in range(num):
    temp = int(input("Please enter number: "))
    numbers.append(temp)

target = int(input("what is your target number? "))

count = 0
for number in numbers:
    if target == number:
        count += 1

print("Numbers Entered: ", numbers)
print("Target: ", target)
print("Count: ", count)