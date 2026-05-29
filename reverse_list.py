num = int(input("How many numbers do you want to enter? "))

numbers = []
for i in range(num):
    temp = int(input("Please enter your number: "))
    numbers.append(temp)

reverse_numbers = []
for j in range(len(numbers)-1,-1,-1):
    reverse_numbers.append(numbers[j])

print("Numbers Entered: ",numbers)
print("Reversed List: ",reverse_numbers)