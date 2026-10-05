board =["1","2","3",
        "4","5","6",
        "7","8","9"]

player1 = "x"
player2 = "o"
current_player = player1

for i in board: 
    board[i]=current_player

if current_player == player1:
    current_player = player2 
else: 
    current_player = player1  

print(board)

