import random

total = 0
n = 10000
for i in range(1, n):
    gain = 0
    success = False
    while(not success):
        dice = random.randint(1,6)
        if dice in range(1,3):
            gain = gain - 1
            success = True
        else:
            if dice in range(3,5):
                gain = gain - 1
                success = True
            else:
                gain = gain + 4
                success = False

    print(gain)
    total = total + gain

print("*********")
print("gain total: %d" % total)
