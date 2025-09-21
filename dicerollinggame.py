import random


while True:
    roll_prompt = input("Roll the die? (y/n): ").lower()

    if roll_prompt != "y" and roll_prompt != "n":
        print("Invalid choice!")

    elif roll_prompt == "y":
        dice_num = int(input("Number of die to roll: "))
        rolls = [random.randint(1, 6) for _ in range(dice_num)]

        print(*rolls)

    elif roll_prompt == "n":
        print("Thanks for playing!")
        break
