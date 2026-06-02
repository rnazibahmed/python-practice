
num = int(input("How many numbers do you want to enter? "))
numbers = []
unique_numbers = []


for i in range(num):
    temp = int(input("Please Enter your number: "))
    numbers.append(temp)

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("Unique Numbers: ",unique_numbers)