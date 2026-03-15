import random

while True:
    roll = random.randint(1,6)
    print("Dice rolled result :", roll)

    again = int(input("Roll again? 1 , 0): "))

    if again==0:
        break