import random

game_count = 1
score = []


while game_count < 4:
    game_count += 1

    lower_limit = int(input("Enter lower limit: "))
    upper_limit = int(input("Enter upper limit: "))

    number = random.randint(lower_limit, upper_limit)
    counter = 1

    for counter in range(5):
        try:
            guess = int(
                input(f"Guess the number (from {lower_limit} - {upper_limit}): "))
            counter += 1

            if guess > number:
                print("Too high! Try again.")

            elif guess < number:
                print("Too low! Try again.")

            elif guess == number:

                if counter == 1:
                    print(f"You got it in {counter} try!")
                else:
                    print(f"You got it in {counter} tries!")

                score.append(counter)
                break

        except ValueError:
            print("Please enter a number.")

    else:
        print(f"You have run out of attempts! The number is {number}")

else:
    lowest_score = min(score)
    print(f"Your best score is {lowest_score}!")
