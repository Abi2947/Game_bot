# Below code is written by usng chess package to run in your device remove "#" infrom of pip 
#pip install chess

import chess
import chess.engine as ce
import random

def game_bot():

    # creating a chess board
    board=chess.Board()

    # creating a dictionary to store the frequency of each move
    move_counts ={}

    #starting the game loop
    while not board.is_game_over():

        #print the board
        print(board)

        #check if it's the bot's turn
        if board.turn:

            #determine the best move based on the move counts
            best_move =None
            max_count = 0
            for move in board.legal_moves:
                uci=move.uci()
                count = move_counts.get(uci,0)
                if count >max_count:
                    best_move = move
                    max_count = count
            if best_move:

                #make the best move
                print(f"Bot plays {best_move}")
                board.push(best_move)
            
            else:

                #make a random move if there is no data on past moves
                move= random.choice(list(board.legal_moves))
                print(f"Bot plays {move}")
                board.push(move)
        
        else:
            
            #prompt the user to make a move
            print("Enter you move:")
            user_move=input()

            #try to make the move on the board
            try:
                board.push_uci(user_move)
            except ValueError:
                print("Invalid move, try again.")
                continue
        
        #saveing the current game state to a file
        with open("game_history.txt","a") as f:
            f.write(f"{board.fen()}\n")

    #after the game is over, update the move counts
    with open("game_history.txt","r") as f:
        for line in f:
            fen =line.strip()
            board.set_fen(fen)
            for move in board.legal_moves:
                uci=move.uci()
                count= move_counts.get(uci,0)
                move_counts[uci]=count+1

game_bot()
