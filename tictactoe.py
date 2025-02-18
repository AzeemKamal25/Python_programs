
board=["1","2","3",
       "4","5","6",
       "7","8","9"]

player="X"
run=True
winner= None 
turns=0

#check win or tie
def horizontle(board):
    global winner
    for i in range(0,9,3):
        if board[i]==board[i+1]==board[i+2]:
            winner=board[i]
            return True
        
def vertical(board):
    global winner
    for i in range(0,3):
        if board[i]==board[i+3]==board[i+6]:
            winner=board[i] 
            return True 
        
def diagonal(board):
    global winner
    if board[0]==board[4]==board[8] or board[2]==board[4]==board[6]:
        winner=board[4]
        return True 
    
def tie():
    global run,turns,winner
    if turns==9 and winner==None:
        print("It's a tie")
        run=False

def checkwin():
    global run
    if horizontle(board) or vertical(board) or diagonal(board):
        print(f"The winner is {winner}")
        run =False

#switch player
def switch():
    global player
    if player=="X":
        player="O"
    else:
        player ="X"
    
          
    

#display the board
def display(board):
    print(board[0]+" |"+board[1]+" | "+board[2])
    print("--------")
    print(board[3]+" |"+board[4]+" | "+board[5])
    print("--------")
    print(board[6]+" |"+board[7]+" | "+board[8])
display(board)


#get input   
def playerinput():
    global turns
    p=int(input("Enter your position : "))
    if p>=1 and p<=9 and board[p-1] not in ["X","O"]:
        board[p-1]=player
        turns+=1
    else:
        print("Invaid position")
        playerinput()
        

#running the game
while(run):
    print(" ")
    playerinput()
    print(" ")
    display(board)
    checkwin()
    tie()
    switch()




