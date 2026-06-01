num = int(input("How many numbers do you want to input? "))

numbers = []


for i in range(num):
    temp = int(input("Please enter a number: "))
    numbers.append(temp)

largest = numbers[0]
second_largest = numbers[0]

for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number

print("Numbers Entered: ", numbers)
print("Largest: ", largest)
print("Second largest: ", second_largest)