import random 

class Player:
    CHOICES = ('rock', 'paper', 'scissors')
    
    def __init__(self):
        self.move = None 
        self.score = 0 
    
    @property 
    def score(self):
        return self._score
    
    @score.setter 
    def score(self, score):
        self._score = score
    
    def increment_score(self):
        self.score += 1

class Computer(Player):
    def __init__(self):
        super().__init__()
        self.move = None 
    
    def choose(self):
        self.move = random.choice(Player.CHOICES)

class Human(Player):
    def __init__(self):
        super().__init__()
        self.move = None   
        
    def choose(self):
        prompt = f'Please choose from {Player.CHOICES}: '
        
        while True:
            player_move = input(f'{prompt}')
            if player_move.lower() in Player.CHOICES:
                break
            
            print('Invalid choice. Choose again.')

        self.move = player_move    
        

class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()
    
    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')
        
    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')
        
    def _display_score(self):
        print(f'Player: {self._human.score} Computer: {self._computer.score}')
        
    def _human_wins(self):
        human_move = self._human.move 
        computer_move = self._computer.move 
        
        return ((human_move == 'rock' and computer_move == 'scissors') or
            (human_move == 'paper' and computer_move == 'rock') or
            (human_move == 'scissors' and computer_move == 'paper'))
    
    def _computer_wins(self):
        human_move = self._human.move 
        computer_move = self._computer.move
        
        return ((computer_move == 'rock' and human_move == 'scissors') or
              (computer_move == 'paper' and human_move == 'rock') or
              (computer_move == 'scissors' and human_move == 'paper'))
        
    def _display_winner(self):
        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')

        if self._human_wins():
            print('You win!')
            self._human.increment_score()
        elif self._computer_wins():
            print('Computer wins!')
            self._computer.increment_score()
        else:
            print("It's a tie")
        print()
    
    def _play_again(self):
        response = input('Would you like to play again? (y/n) ')
        return response.lower().startswith('y')
    
    def _winner_decided(self):
        return self._human.score == 3 or self._computer.score == 3

    def _display_final_score(self):
        print('Final Score')
        print(f'Player: {self._human.score}, Computer: {self._computer.score}')
    
    def play(self):
        while True: # play again 
            self._display_welcome_message()
            # while scores are less than 3 
            while not self._winner_decided():
            # display current score
                self._display_score()
                self._human.choose()
                self._computer.choose()
                # increment winner's score
                # display current score
                self._display_winner() # if player.score == 3
            
            self._display_final_score()
            if not self._play_again():
                break     
        
        self._display_goodbye_message()
            
        
RPSGame().play()
