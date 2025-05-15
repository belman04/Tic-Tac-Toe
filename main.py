def main():
    spaces = ["   "] * 9 # list of 9 empty spaces
    current_player = "X" # start with player X
    
    display_board(spaces) 

    while "   " in spaces: # check if there are empty spaces to play       
        print(f"Player {current_player} turn")
        position = int(input("Choose a position in the board (1-9): ")) # input from player 1 in console

        if position < 1 or position > 9: # check if input is valid
            print("Invalid input. Choose a number between 1-9")
            continue # skips to the next iteration
            
        if spaces[int(position) - 1] != "   ": # check if position is already taken
            print("Position taken, choose another")
            continue # skips to the next iteration
                        
        spaces[int(position) - 1] = f" {current_player} " # sets the current player in the chosen position - 1 
        display_board(spaces) # display the board after a move
        
        if check_winner(spaces, current_player): # check if the current player has won
            print(f"Player {current_player} wins!")
            break # exits the loop
        elif "   " not in spaces: # check if there are no empty spaces left
            print("It's a draw!")
            break # exits the loop
        
        current_player = "O" if current_player == "X" else "X" # switch players

    restart = input("Do you want to play again? (y/n): ").lower() # ask if the player wants to play again
    
    if restart == "y": # 
        main() # restart the game
    else:
        print("Thanks for playing!")
        
# funtion to display the board
def display_board(spaces):
    print(spaces[0] + "|" + spaces[1] + "|" + spaces[2])
    print("------------")
    print(spaces[3] + "|" + spaces[4] + "|" + spaces[5])
    print("------------")
    print(spaces[6] + "|" + spaces[7] + "|" + spaces[8])

# function to check if there is a winner
def check_winner(spaces, player):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        
        [0, 4, 8],
        [2, 4, 6],
    ]
    
    for combo in winning_combinations: # check all winning combinations
        if all(spaces[i] == f" {player} " for i in combo): # check if all positions in the combination are the same
            return True
    return False
        
if __name__ == "__main__": main()