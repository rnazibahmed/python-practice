num = int(input("How many numbers do you want to input? "))

numbers = []
even_numbers = []

for i in range(num):
    temp = int(input("Please enter your number : "))
    numbers.append(temp)
    if temp % 2 == 0 : 
        even_numbers.append(temp)
    
print("Numbers Entered: ", numbers)
print("Even Numbers: ",even_numbers)
print("Count of Even Numbers: ",len(even_numbers))