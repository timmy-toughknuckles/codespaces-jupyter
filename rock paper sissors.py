while True:

    import random
    def get_user_choice():
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
        while user_input not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            user_input = input("Enter your choice (rock, paper, scissors): ").lower()
        return user_input
    def get_computer_choice():
        choices = ['rock', 'paper', 'scissors']
        return random.choice(choices)
    def determine_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
            return "You win!"
        else:
            return "Computer wins!"

    determine_winner(get_user_choice(), get_computer_choice())