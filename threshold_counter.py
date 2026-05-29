num = int(input("How many numbers do you want to input? "))

numbers = []
for i in range(num):
    temp = int(input("Enter your number: "))
    numbers.append(temp)

thres = int(input("Please enter the threshold: "))

greater_num = []
lesser_num = []

for number in numbers:
    if number > thres:
        greater_num.append(number)
    else:
        lesser_num.append(number)

print("Number Entered: ", numbers)
print("Threshold: ", thres)
print("Numbers greater than threshold: ",greater_num)
print("Numbers lesser or equal to threshold: ", lesser_num)