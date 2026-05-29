num = int(input("How many numbers do you want to enter? "))

numbers = []
for i in range(num):
    temp = int(input("Please enter number: "))
    numbers.append(temp)

max = numbers[0]
for num in numbers:
    if max < num:
        max = num

print("Numbers Entered: ",numbers)
print("Largest number: ",max)