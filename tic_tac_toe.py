from os import system
from socket import *

class Game:
  def __init__(self):
    self.board = [[' ' for _ in range(3)] for _ in range(3)]
    self.rounds = 0
    self.turn = 'X'
    self.game_over = False
    self.winner = None

  def host_game(self, host, port):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    client, addr = server.accept()

    self.you = 'X'
    self.opponent = 'O'

    self.multiplayer_loop(client)

    server.close()

  def connect_to_game(self, host, port):
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((host, port))
    self.you = 'O'
    self.opponent = 'X'
    self.multiplayer_loop(client)

  def print_board(self):
    system('clear')
    for row in range(3):
      print(' | '.join(self.board[row]))
      if row != 2:
        print('---------')

  def is_valid_move(self, move):
    return self.board[int(move[0])][int(move[1])] == ' '

  def make_move(self, move, player):
    if self.game_over:
      return
    self.rounds += 1
    self.board[int(move[0])][int(move[1])] = player
    self.print_board()
    if self.rounds >= 5:
      self.verify_board()

  def end_game(self):
    if self.winner == self.you:
      print('Your Win!!!')
    elif self.winner == self.opponent:
      print('You Lose :( !!')
    else:
      print('TIE')
  
  def verify_board(self):
    for row in range(3):
      if self.board[row][0] == self.board[row][1] == self.board[row][2] != ' ':
        self.winner == self.board[row][0]
        self.game_over = True
        self.end_game()
    for column in range(3):
      if self.board[0][column] == self.board[1][column] == self.board[2][column] != ' ':
        self.winner == self.board[0][column]
        self.game_over = True
        self.end_game()
    if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
      self.winner = self.board[0][0]
      self.game_over = True
      self.end_game()
    if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
      self.winner = self.board[0][2]
      self.game_over = True
      self.end_game()

    if self.rounds == 9:
      self.game_over = True
      self.end_game()
  
  def multiplayer_loop(self, client):
    while not self.game_over:
      if self.turn == self.you:
        move = input('Enter a move (row,column):')
        if self.is_valid_move(move.split(',')):
          self.make_move(move.split(','), self.you)
          self.turn = self.opponent
          client.send(move.encode('utf-8'))
        else: 
          print('Invalid move')
      else:
        print('Waiting opponent move...')
        data = client.recv(1024)
        if not data:
          client.close()
          break
        else:
          self.make_move(data.decode('utf-8').split(','), self.opponent)
          self.turn = self.you