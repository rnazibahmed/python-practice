num = int(input("How many numbers do you want to input? "))

numbers = []


for i in range(num):
    temp = int(input("Please enter a number: "))
    numbers.append(temp)

if numbers[0] > numbers[1]:
    largest = numbers[0]
    second_largest = numbers[1]
else:
    second_largest = numbers[0]
    largest = numbers[1]

for number in numbers[2:]:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number
        

print("Numbers Entered: ", numbers)
print("Largest: ", largest)
print("Second largest: ", second_largest)