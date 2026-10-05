#九宮格（グリッド）のボードを定義する
board =[
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

#2人のプレイヤーを定義する
player1 = "x"
player2 = "o"

#現在のプレイヤーを設定する
current_player = player1

#一歩進むごとに確認します
for turn in range(9):
    #現在のプレイヤーに位置を入力させる
    i = int(input(f"{current_player} row："))
    j = int(input(f"{current_player} column："))

    while i < 0 or i > 2 or j < 0 or j > 2:
        print("write inside 0～2")
        i = int(input(f"{current_player} row："))
        j = int(input(f"{current_player} column：")) 

    while board[i][j] == "x" or board[i][j] == "o":
        print("This position is already used.")
        i = int(input(f"{current_player} row："))
        j = int(input(f"{current_player} column："))

    #現在の盤面を表示する
    print("   0 1 2")
    print(f"0  {board[0][0]} {board[0][1]} {board[0][2]}")
    print(f"1  {board[1][0]} {board[1][1]} {board[1][2]}")
    print(f"2  {board[2][0]} {board[2][1]} {board[2][2]}")
    
    #勝敗を判定する
    #8種類の勝利の組み合わせ
    if board[0][0] == board[1][1] == board[2][2]== current_player:
        print(f"{current_player} wins")
        break
    if board[0][2] == board[1][1] == board[2][0]== current_player:
        print(f"{current_player} wins")
        break
    if board[0][0] == board[0][1] == board[0][2]== current_player:
        print(f"{current_player} wins")
        break
    if board[1][0] == board[1][1] == board[1][2]== current_player:
        print(f"{current_player} wins")
        break
    if board[2][0] == board[2][1] == board[2][2]== current_player:
        print(f"{current_player} wins")
        break
    if board[0][0] == board[1][0] == board[2][0]== current_player:
        print(f"{current_player} wins")
        break
    if board[0][1] == board[1][1] == board[2][1]== current_player:
        print(f"{current_player} wins")
        break
    if board[0][2] == board[1][2] == board[2][2]== current_player:
        print(f"{current_player} wins")
        break

    if current_player == player1:
        current_player = player2 
    else: 
        current_player = player1  









