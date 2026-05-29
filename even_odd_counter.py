num = int(input("How many numbers they want to enter? "))

even_num = 0
odd_num = 0
numbers = []

for i in range(num):
    temp_num = int(input("Please enter the number : "))
    if temp_num%2 == 0:
        even_num += 1
    else:
        odd_num += 1
    numbers.append(temp_num)

print("\nNumbers Entered: ",numbers)
print("Even numbers:", even_num)
print("Odd numbers:", odd_num)