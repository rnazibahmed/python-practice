seen = []
duplicates = []
numbers = []

num = int(input("How many numbers do you want to enter? "))

for i in range(num):
    temp = int(input("Please enter your number: "))
    numbers.append(temp)

for number in numbers:
    seen_flag = False
    for seen_number in seen:
        if number == seen_number:
            seen_flag = True
            dup_flag = False
            for dup_number in duplicates:
                if number == dup_number:
                    dup_flag = True
            if dup_flag == False:
                duplicates.append(number)
    if seen_flag == False:
        seen.append(number)

print("Numbers Entered: ",numbers)
print("Duplicates: ", duplicates)

