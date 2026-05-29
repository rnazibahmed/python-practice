num = int(input("How many numbers do you want to enter? "))

numbers = []
total = 0
for i in range(num):
    temp = int(input("Please enter your number: "))
    numbers.append(temp)
    total += temp

print("Numbers Entered: ",numbers)
print("Total: ", total)
print("Average: ", round(total/len(numbers),2))

