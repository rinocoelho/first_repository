from random import randint


horse_one = 0

horse_two = 0

horse_three = 0

horse_four = 0

horse_five = 0

horse_six = 0

for i in range(10000):
    result =randint(1,100)
    if result <= 30:
        horse_one += 1
    elif result > 30 and result <= 50:
        horse_two += 1
    elif result > 50 and result <= 68:
        horse_three += 1
    elif result > 68 and result <= 83:
        horse_four += 1
    elif result > 83 and result <= 93:
        horse_five += 1
    elif result > 93 and result <= 100:
        horse_six += 1

print(horse_one/100)
print(horse_two/100)
print(horse_three/100)
print(horse_four/100)
print(horse_five/100)
print(horse_six/100)