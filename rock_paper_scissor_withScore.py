import random


def win():
    print('You win.')

def lost():
    print('You lost.')

def draw():
    print('Its a draw.')


def the_game():

    moves = ['rock', 'paper', 'scissors']

    print('THE GAME: Rock, Paper, Scissors?')
    attempts =3
    while True:
        

        player = str(input('Player: ')).lower()
        if player.lower() not in moves:
            print(f'Invalid Option! You have {attempts} attempts left.')
            attempts -= 1
        else:
            computer = random.choice(moves)
            print(f'Computer: {computer}')

            if player == computer:
                draw()
            elif player == 'rock' and computer == 'scissors':
                win()
            elif player == 'rock' and computer == 'paper':
                lost()
            elif player == 'paper' and computer == 'rock':
                win()
            elif player == 'paper' and computer == 'scissors':
                lost()
            elif player == 'scissors' and computer == 'paper':
                win()
            elif player == 'scissors' and computer == 'rock':
                lost()
            else:
                pass

            play_again = str(input('Retry? (y/n): '))
            if play_again.lower() == 'y':
                the_game()
            elif play_again.lower() == 'n':
                
                print('Game Over.')
                break
            else:
                print('Invalid Options.')
                
                


if __name__=='__main__':
    the_game()

    