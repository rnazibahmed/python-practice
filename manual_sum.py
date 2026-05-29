num = int(input("How many numbers do you want to enter? "))

numbers = []
for i in range(num):
    temp = int(input("Please enter number: "))
    numbers.append(temp)

total = 0
for number in numbers:
    total += number

print("Numbers Entered: ",numbers)
print("Summation is: ",total)