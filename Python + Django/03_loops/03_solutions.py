number = 3

for i in range(1, 11):
    if i == 5:
        continue #5th iteration disappeared
    print(number, 'X' , i, '=', number * i)

# 3 * 1 = 3    