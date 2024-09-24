import random

continue_calculating = True
while continue_calculating:
    input_value = input("Choose one (R, P, S): ")
    computer_options = ["R", "P", "S"]
    computer = random.choice(computer_options)
    print(f"Computer chose: {computer}")
    if input_value == computer:
        print("It's a tie!")
    elif input_value == "R" and computer == "S":
        print("You win!")
    elif input_value == "P" and computer == "R":
        print("You win!")
    elif input_value == "S" and computer == "P":
        print("You win!")
    elif input_value == "R" and computer == "P":
        print("You lose!")
    elif input_value == "P" and computer == "S":
        print("You lose!")
    elif input_value == "S" and computer == "R":
        print("You lose!")

    continue_answer = input("Do you want to continue? (Y/n): ")
    continue_calculating = continue_answer.lower() == "y" or continue_answer == ""