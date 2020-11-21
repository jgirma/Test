class game():
    def __init__(self, board, finished, winner, tie):
        self.board = board
        self.finished = finished
        self.winner = winner
        game.tie = tie


def checkboard(game):
    game.tie = 1
    for i in range(3):
        print(game.board[i])
    for row in range(3):
        if game.board[row][0] == game.board[row][1] and game.board[row][0] == game.board[row][2] and game.board[row][
            1] == game.board[row][2]:
            if game.board[row][0] == "X":
                game.winner += "Player 1"
                game.finished = 1
            elif game.board[row][0] == "O":
                game.winner += "Player 2"
                game.finished = 1
    for col in range(3):
        if game.board[0][col] == game.board[1][col] and game.board[0][col] == game.board[2][col] and game.board[1][
            col] == game.board[2][col]:
            if game.board[0][col] == "X":
                game.winner += "Player 1"
                game.finished = 1
            elif game.board[0][col] == "O":
                game.winner += "Player 2"
                game.finished = 1
    if game.board[0][0] == game.board[1][1] and game.board[0][0] == game.board[2][2] and game.board[1][1] == \
            game.board[2][2]:
        if game.board[0][0] == "X":
            game.winner += "Player 1"
            game.finished = 1
        elif game.board[0][0] == "O":
            game.winner += "Player 2"
            game.finished = 1
    if game.board[2][0] == game.board[1][1] and game.board[2][0] == game.board[0][2] and game.board[1][1] == \
            game.board[0][2]:
        if game.board[2][0] == "X":
            game.winner += "Player 1"
            game.finished = 1
        elif game.board[2][0] == "O":
            game.winner += "Player 2"
            game.finished = 1
    for checkrow in range(3):
        for checkcol in range(3):
            if not game.board[checkrow][checkcol]:
                game.tie = 0
    if game.tie != 0:
        game.finished = 1
    return


setup = [[[], [], []], [[], [], []], [[], [], []]]
Tic = game(setup, 0, "", 0)

while True:

    while True:
        index1x = int(input("Player 1 Choose a row: "))
        index1y = int(input("Player 1 Choose a column: "))
        if not 0 <= index1x and index1y <= 2 or Tic.board[index1x][index1y] != []:
            print("Error: Try Again")
        else:
            break
    Tic.board[index1x][index1y] = "X"
    checkboard(Tic)
    if Tic.finished:
        break
    while True:
        index2x = int(input("Player 2 Choose an row: "))
        index2y = int(input("Player 2 Choose a column: "))
        if not 0 <= index2x and index2y <= 2 or Tic.board[index2x][index2y] != []:
            print("Error: Try Again")
            continue
        else:
            break
    Tic.board[index2x][index2y] = "O"
    checkboard(Tic)
    if Tic.finished:
        break
if Tic.winner == "":
    print("It's a tie. Thanks for playing.")
else:
    print("Congratulations " + Tic.winner + " You are a winner.")
