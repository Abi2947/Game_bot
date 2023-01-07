#Using neural network to create game bot for chess

#pip install chess
#pip install numpy
#pip intsall tensorflow

import chess
import chess.engine
import random
import numpy as np
import tensorflow as tf

# define the neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(8, 8, 6)),
    tf.keras.layers.Conv2D(64, 3, activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(len(board.legal_moves), activation='softmax')
])

# compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

def game_bot():
  # create a chess board
  board = chess.Board()

  # start the game loop
  while not board.is_game_over():
    # print the board
    print(board)

    # check if it's the bot's turn
    if board.turn:
      # generate a prediction from the model
      inputs = np.expand_dims(board.board_fen(), axis=0)
      outputs = model.predict(inputs)

      # choose a move based on the prediction
      best_move_index = np.argmax(outputs)
      move = list(board.legal_moves)[best_move_index]
      print(f"Bot plays {move}")
      board.push(move)
    else:
      # prompt the user to make a move
      print("Enter your move (e.g. e2e4):")
      user_move = input()

      # try to make the move on the board
      try:
        board.push_uci(user_move)
      except ValueError:
        print("Invalid move, try again.")
        continue

    # save the current game state and result to a file
    result = 1 if board.result() == "1-0" else 0
    with open("games_history.txt", "a") as f:
      f.write(f"{board.fen()},{result}\n")

game_bot()
