import random

NUM_ROUNDS = 5

def main():

    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    # Milestone 5: keep track of your score
    your_score = 0

    # Milestone 4: Play multiple rounds
    for i in range(NUM_ROUNDS):
        print(f"Round {i + 1}")
        # Milestone 1: Generate the random numbers and print them out
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print(f"Your number is {your_num}")

        # Milestone 2: Get user input for their choice
        choice = input("Do you think your number is higher or lower than the computer's?: ")

        # Milestone 3: Map out all the ways to win the round
        higher_and_correct = choice == "higher" and your_num > computer_num
        lower_and_correct = choice == "lower" and your_num < computer_num

        if higher_and_correct or lower_and_correct:
            print(f"You were right! The computer's number was {computer_num}")
            # Milestone 5: keep track of your score
            your_score += 1 
        else: 
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")

        # Milestone 5: keep track of your score
        print(f"Your score is now {your_score}")
        print()

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
