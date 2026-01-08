'''
Create an object-oriented number guessing class for numbers in the 
range 1 to 100, with a limit of 7 guesses per game.
'''
import random 
class GuessingGame:
    def __init__(self):
        self.target_number = random.randint(1, 100)
        self.num_guesses = 7 
    
    @staticmethod
    def is_valid_num(num):
        return 1 <= num <= 100
    
    def play(self):
        while self.num_guesses >= 1:
            print()
            print(f'You have {self.num_guesses} guesses remaining')
            self.num_guesses -= 1
            
            user_guess = int(input('Enter a number between 1 and 100: '))
            while True:
                if GuessingGame.is_valid_num(user_guess):
                    break 
                
                user_guess = int(input('Invalid guess. Enter a number between 1 and 100: '))
            
            if user_guess == self.target_number:
                print('That\'s the number!')
                print()
                print('You won!')
                return 
            elif user_guess > self.target_number:
                print('Your guess is too high.')
            else:
                print('Your guess is too low.')
        
        print('You have no more guesses. You lost!')    
    
game = GuessingGame()
game.play()

