appearance = {}

num = int(input("How many numbers do you want to enter? "))

for i in range(num):
    temp = int(input("Please enter your number: "))
    if temp in appearance:
        appearance[temp] += 1
    else:
        appearance[temp] = 1

for key,value in appearance.items():
    print(key, " appears ", value, " times")


