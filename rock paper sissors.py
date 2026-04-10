while True:

    import random
    def get_user_choice():
        user_input = input("Enter your choice (rock, paper, scissors): ")
        while user_input not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            user_input = input("Enter your choice (rock, paper, scissors): ")
        return user_input
    def get_computer_choice():
        choices = ['rock', 'paper', 'scissors']
        return random.choice(choices)
    def determine_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            print(f"You chose {user_choice}, computer chose {computer_choice}.")
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
            print(f"You chose {user_choice}, computer chose {computer_choice}.")
            print("You win!")
        else:
            print(f"You chose {user_choice}, computer chose {computer_choice}.")
            print("Computer wins!")

    determine_winner(get_user_choice(), get_computer_choice())
    get_computer_choice = "0"
    get_user_choice = "0"
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        print("Thanks for playing!")
        break   
    else:
        continue