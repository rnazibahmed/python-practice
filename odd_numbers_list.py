num = int(input("How many numbers do you want to input? "))

numbers = []
odd_numbers = []

for i in range(num):
    temp = int(input("Please enter your number : "))
    numbers.append(temp)
    if temp % 2 != 0 : 
        odd_numbers.append(temp)
    
print("Numbers Entered: ", numbers)
print("Odd Numbers: ",odd_numbers)
print("Count of Odd Numbers: ",len(odd_numbers))