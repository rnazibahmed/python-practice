num = int(input("How many numbers do you want to enter? "))

numbers = []
for i in range(num):
    temp = int(input("Please enter number: "))
    numbers.append(temp)

minimum = numbers[0]
for num in numbers:
    if minimum > num:
        minimum = num

print("Numbers Entered: ",numbers)
print("Smallest number: ",minimum)