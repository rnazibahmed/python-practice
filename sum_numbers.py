num = int(input("How many numbers? "))

numbers = []
for n in range(num):
    number = int(input(f"Enter number {n+1}: "))
    numbers.append(number)

print("Numbers Entered ", numbers)
sum_numbers = sum(numbers)
print("\nSum = ", sum_numbers)
print("Average = ", round(sum_numbers/len(numbers),2))
print("Maximum = ",max(numbers))
print("Minimum = ",min(numbers))