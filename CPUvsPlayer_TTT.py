import random

board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

player = "X"
run = True
winner = None
turns = 0


# Check for a win
def horizontle(board):
    global winner
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2]:
            winner = board[i]
            return True
    return False


def vertical(board):
    global winner
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6]:
            winner = board[i]
            return True
    return False


def diagonal(board):
    global winner
    if board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        winner = board[4]
        return True
    return False


def tie():
    global run, turns, winner
    if turns == 9 and winner is None:
        print("It's a tie!")
        run = False


def checkwin():
    global run
    if horizontle(board) or vertical(board) or diagonal(board):
        print(f"The winner is {winner}")
        run = False


# Display the board
def display(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


display(board)


# Get player input
def playerinput():
    global turns
    p = int(input("Enter your position : ")) - 1
    if 0 <= p < 9 and board[p] not in ["X", "O"]:
        board[p] = player
        turns += 1
    else:
        print("Invalid position, try again.")
        playerinput()        


# CPU move logic
def cpuinput():
    global turns

    # Function to check for a winning or blocking move
    def find_best_move(player):
        for i in range(0, 9, 3):  # Rows
            if board[i] == board[i + 1] == player and board[i + 2] not in ["X", "O"]:
                return i + 2
            if board[i] == board[i + 2] == player and board[i + 1] not in ["X", "O"]:
                return i + 1
            if board[i + 1] == board[i + 2] == player and board[i] not in ["X", "O"]:
                return i

        for i in range(3):  # Columns
            if board[i] == board[i + 3] == player and board[i + 6] not in ["X", "O"]:
                return i + 6
            if board[i] == board[i + 6] == player and board[i + 3] not in ["X", "O"]:
                return i + 3
            if board[i + 3] == board[i + 6] == player and board[i] not in ["X", "O"]:
                return i

        # Diagonals
        if board[0] == board[4] == player and board[8] not in ["X", "O"]:
            return 8
        if board[0] == board[8] == player and board[4] not in ["X", "O"]:
            return 4
        if board[4] == board[8] == player and board[0] not in ["X", "O"]:
            return 0

        if board[2] == board[4] == player and board[6] not in ["X", "O"]:
            return 6
        if board[2] == board[6] == player and board[4] not in ["X", "O"]:
            return 4
        if board[4] == board[6] == player and board[2] not in ["X", "O"]:
            return 2

        return None  # No winning/blocking move found

    # CPU tries to win first
    move = find_best_move("O")
    if move is not None:
        board[move] = "O"
        turns += 1
        return

    # Block the player's winning move
    move = find_best_move("X")
    if move is not None:
        board[move] = "O"
        turns += 1
        return

    # If no win/block, pick the center if available
    if board[4] not in ["X", "O"]:
        board[4] = "O"
        turns += 1
        return

    # If center is taken, choose a random available spot
    empty_positions = [i for i in range(9) if board[i] not in ["X", "O"]]
    if empty_positions:
        board[random.choice(empty_positions)] = "O"
        turns += 1


# Running the game loop
while run:
    print("\nPlayer's Turn:")
    playerinput()
    display(board)
    checkwin()
    tie()
    if not run:
        break

    # Check if game is already over before CPU moves
    if turns < 9 and run:
        print("\nCPU's Turn:")
        cpuinput()
        display(board)
        checkwin()
        tie()
