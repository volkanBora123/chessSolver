
board_file = "ex_board3.txt"
opponent_file = "ex_opponent3.txt"
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
#Bismillahirrahmanirrahim
chessboard = [[0 for i in range(8)] for j in range(8)]
f = open(board_file)
filecontent = ""
for line in f.readlines():
    filecontent += line
color = filecontent.split("\n")[0].strip()
for line in filecontent.split("\n")[1:]:
    try:
        piece,coord = line.split()
        chessboard[8 - int(coord[1])][ord(coord[0]) - ord("a")] = piece
    except:
        pass
f.close()
def pprint(grid):
    for r in grid:
        for c in r:
            print(c,end = " ")
        print()
def moves(board,piece,coord):
    piecey,piecex = coord
    color = piece[0]
    lmoves = [(-1,2),(1,2),
        (-2,1),            (2,1),
        (-2,-1),            (2,-1),
              (-1,-2),(1,-2)]
    knight = []
    for dy,dx in lmoves:
        if 0 <= piecey + dy <= 7 and 0 <= piecex + dx <= 7:
            if board[piecey + dy][piecex + dx] == 0 or board[piecey + dy][piecex + dx][0] != color:
                knight.append((piecey + dy,piecex + dx))
    bishop = []
    #solust
    for i in range(1,8):
        if piecey - i < 0 or piecex - i < 0:
            break
        if board[piecey - i][piecex - i] == 0:
            bishop.append((piecey - i,piecex - i))
        elif board[piecey - i][piecex - i][0] != color:
            bishop.append((piecey - i,piecex - i))
            break
        else:
            break
    #solalt
    for i in range(1,8):
        if piecey + i >= 8 or piecex - i < 0:
            break
        if board[piecey + i][piecex - i] == 0:
            bishop.append((piecey + i,piecex - i))
        elif board[piecey + i][piecex - i][0] != color:
            bishop.append((piecey + i,piecex - i))
            break
        else:
            break
    #sagust
    for i in range(1,8):
        if piecey - i < 0 or piecex + i > 7:
            break
        if board[piecey -i][piecex + i] == 0:
            bishop.append((piecey - i,piecex + i))
        elif board[piecey -i][piecex + i][0] != color:
            bishop.append((piecey - i,piecex + i))
            break
        else:
            break
    #sagalt
    for i in range(1, 8):
        if piecey + i > 7 or piecex + i > 7:
            break
        if board[piecey + i][piecex + i] == 0:
            bishop.append((piecey + i, piecex + i))
        elif board[piecey + i][piecex + i][0] != color:
            bishop.append((piecey + i, piecex + i))
            break
        else:
            break
    rook = []
    #ust
    for i in range(1,8):
        if piecey - i < 0:
            break
        if board[piecey - i][piecex] == 0:
            rook.append((piecey - i,piecex))
        elif board[piecey - i][piecex][0] != color:
            rook.append((piecey - i, piecex))
            break
        else:
            break
    #alt
    for i in range(1,8):
        if piecey + i > 7:
            break
        if board[piecey + i][piecex] == 0:
            rook.append((piecey + i,piecex))
        elif board[piecey + i][piecex][0] != color:
            rook.append((piecey + i, piecex))
            break
        else:
            break
    #sol
    for i in range(1,8):
        if piecex - i < 0:
            break
        if board[piecey][piecex - i] == 0:
            rook.append((piecey,piecex - i))
        elif board[piecey][piecex - i][0] != color:
            rook.append((piecey, piecex - i))
            break
        else:
            break
    #sag
    for i in range(1,8):
        if piecex + i > 7:
            break
        if board[piecey][piecex + i] == 0:
            rook.append((piecey,piecex + i))
        elif board[piecey][piecex + i][0] != color:
            rook.append((piecey, piecex + i))
            break
        else:
            break
    queen = []
    # ust
    for i in range(1, 8):
        if piecey - i < 0:
            break
        if board[piecey - i][piecex] == 0:
            queen.append((piecey - i, piecex))
        elif board[piecey - i][piecex][0] != color:
            queen.append((piecey - i, piecex))
            break
        else:
            break
    # alt
    for i in range(1, 8):
        if piecey + i > 7:
            break
        if board[piecey + i][piecex] == 0:
            queen.append((piecey + i, piecex))
        elif board[piecey + i][piecex][0] != color:
            queen.append((piecey + i, piecex))
            break
        else:
            break
    # sol
    for i in range(1, 8):
        if piecex - i < 0:
            break
        if board[piecey][piecex - i] == 0:
            queen.append((piecey, piecex - i))
        elif board[piecey][piecex - i][0] != color:
            queen.append((piecey, piecex - i))
            break
        else:
            break
    # sag
    for i in range(1, 8):
        if piecex + i > 7:
            break
        if board[piecey][piecex + i] == 0:
            queen.append((piecey, piecex + i))
        elif board[piecey][piecex + i][0] != color:
            queen.append((piecey, piecex + i))
            break
        else:
            break
    #solust
    for i in range(1,8):
        if piecey - i < 0 or piecex - i < 0:
            break
        if board[piecey - i][piecex - i] == 0:
            queen.append((piecey - i,piecex - i))
        elif board[piecey - i][piecex - i][0] != color:
            queen.append((piecey - i,piecex - i))
            break
        else:
            break
    #solalt
    for i in range(1,8):
        if piecey + i >= 8 or piecex - i < 0:
            break
        if board[piecey + i][piecex - i] == 0:
            queen.append((piecey + i,piecex - i))
        elif board[piecey + i][piecex - i][0] != color:
            queen.append((piecey + i,piecex - i))
            break
        else:
            break
    #sagust
    for i in range(1,8):
        if piecey - i < 0 or piecex + i > 7:
            break
        if board[piecey - i][piecex + i] == 0:
            queen.append((piecey - i,piecex + i))
        elif board[piecey - i][piecex + i][0] != color:
            queen.append((piecey - i,piecex + i))
            break
        else:
            break
    #sagalt
    for i in range(1, 8):
        if piecey + i > 7 or piecex + i > 7:
            break
        if board[piecey + i][piecex + i] == 0:
            queen.append((piecey + i, piecex + i))
        elif board[piecey + i][piecex + i][0] != color:
            queen.append((piecey + i, piecex + i))
            break
        else:
            break
    kingmoves = [(-1,1),(0,1),(1,1),
            (-1,0),      (1,0),
            (-1,-1),(0,-1),(1,-1)]
    king = []
    for dy,dx in kingmoves:
        if 0 <= piecey + dy <= 7 and 0 <= piecex + dx <= 7:
            if board[piecey + dy][piecex + dx] == 0 or board[piecey + dy][piecex + dx][0] != color:
                king.append((piecey + dy,piecex + dx))
    pawn = []
    if color == "B":
        #y,x
        #siyah asagi beyaz yukari yani beyazy eksiliyor
        if piecey + 1 <= 7:
            if board[piecey + 1][piecex] == 0:
                pawn.append((piecey + 1,piecex))
            if piecex - 1 >=0 and board[piecey + 1][piecex - 1] != 0:
                if board[piecey + 1][piecex - 1][0] != color:
                    pawn.append((piecey + 1,piecex - 1))
            if piecex + 1 <= 7 and board[piecey + 1][piecex + 1] != 0:
                if board[piecey + 1][piecex + 1][0] != color:
                    pawn.append((piecey + 1, piecex + 1))
    else:
        if piecey - 1 >= 0:
            if board[piecey - 1][piecex] == 0:
                pawn.append((piecey - 1, piecex))
            if piecex - 1 >= 0 and board[piecey - 1][piecex - 1] != 0:
                if board[piecey - 1][piecex - 1][0] != color:
                    pawn.append((piecey - 1, piecex - 1))
            if piecex + 1 <= 7 and board[piecey - 1][piecex + 1] != 0:
                if board[piecey - 1][piecex + 1][0] != color:
                    pawn.append((piecey - 1, piecex + 1))
    move_dict = {
        "Q" : queen,
        "R" : rook,
        "B" : bishop,
        "K" : king,
        "P" : pawn,
        "N" : knight,
    }
    moves = move_dict[piece[1]]
    valid_moves = []
    for movey,movex in moves:
        board[coord[0]][coord[1]] = 0
        temp = board[movey][movex]
        board[movey][movex] = piece
        if not ischecked(board,color):
            valid_moves.append((movey,movex))
        board[coord[0]][coord[1]] = piece
        board[movey][movex] = temp
    return valid_moves

def allmoves(board,color):
    res = []
    for r in range(8):
        for c in range(8):
            if board[r][c] != 0 and board[r][c][0] == color:
                res.append((board[r][c],(r,c),moves(board,board[r][c],(r,c))))
    return res

def ischecked(board,color):
    kingcoords = [0,0]
    opposite_color = "B"
    if color == "B":
        opposite_color = "W"
    for r in range(8):
        for c in range(8):
            if board[r][c] == color + "K":
                kingcoords = [r,c]
                break
    kingy,kingx = kingcoords
    #sol
    for i in range(kingx - 1,-1,-1):
        if board[kingy][i] == opposite_color + "Q" or board[kingy][i] == opposite_color + "R":
            #print("solda queen ya da rook")
            return True
        elif board[kingy][i] == 0:
            continue
        else:
            break
    #sag
    for x in range(kingx + 1,8):
        if board[kingy][x] == opposite_color + "Q" or board[kingy][x] == opposite_color + "R":
            #print("sagda queen ya da rook")
            return True
        elif board[kingy][x] == 0:
            continue
        else:
            break
    #ust
    for y in range(kingy - 1,-1,-1):
        if board[y][kingx] == opposite_color + "Q" or board[kingy][y] == opposite_color + "R":
            #print("ustte queen ya da rook")
            return True
        elif board[y][kingx] == 0:
            continue
        else:
            break
    #alt
    for y in range(kingy + 1,8):
        if board[y][kingx] == opposite_color + "Q" or board[y][kingx] == opposite_color + "R":
            #print("altta queen ya da rook")
            return True
        elif board[y][kingx] == 0:
            continue
        else:
            break
    #solust
    for i in range(1,8):
        if kingy - i < 0 or kingx - i < 0:
            break
        if board[kingy - i][kingx - i] == opposite_color + "Q" or board[kingy - i][kingx - i] == opposite_color + "B":
            #print("ustcapraz queen ya da bishop")
            return True
        elif board[kingy - i][kingx - i] == 0:
            continue
        else:
            break
    #solalt
    for i in range(1,8):
        if kingy + i > 7 or kingx - i < 0:
            break
        if board[kingy + i][kingx - i] == opposite_color + "Q" or board[kingy + i][kingx - i] == opposite_color + "B":
            #print("solalt queen ya da bishop")
            return True
        elif board[kingy + i][kingx - i] == 0:
            continue
        else:
            break
    #sagust
    for i in range(1,8):
        if kingy - i < 0 or kingx + i > 7:
            break
        if board[kingy - i][kingx + i] == opposite_color + "Q" or board[kingy - i][kingx + i] == opposite_color + "B":
            #print("sagust queen ya da bishop")
            return True
        elif board[kingy - i][kingx + i] == 0:
            continue
        else:
            break
    #sagalt
    for i in range(1,8):
        if kingy + i > 7 or kingx + i > 7:
            break
        if board[kingy + i][kingx + i] == opposite_color + "Q" or board[kingy + i][kingx + i] == opposite_color + "B":
            #print("sagalt queen ya da bishop")
            return True
        elif board[kingy + i][kingx + i] == 0:
            continue
        else:
            break
    #at
    lmoves = [(-1,2),(1,2),
        (-2,1),            (2,1),
        (-2,-1),            (2,-1),
              (-1,-2),(1,-2)]
    for dy,dx in lmoves:
        if 0 <= kingy + dy <= 7 and 0 <= kingx + dx <= 7:
            if board[kingy + dy][kingx + dx] == opposite_color + "N":
                #print("aigggggg")
                return True
    #piyon
    if color == "B":
        #asagi bak
        if kingy + 1 <= 7:
            if kingx + 1 <= 7:
                if board[kingy + 1][kingx + 1] == opposite_color + "P":
                    #print("sagpiyon")
                    return True
            if kingx - 1 >= 0:
                if board[kingy + 1][kingx - 1] == opposite_color + "P":
                    #print("sol piyon")
                    return True
    else:
        #yukari bak
        if kingy - 1 >= 0:
            if kingx + 1 <= 7:
                if board[kingy - 1][kingx + 1] == opposite_color + "P":
                    #print("sagpiyon")
                    return True
            if kingx - 1 >= 0:
                if board[kingy - 1][kingx - 1] == opposite_color + "P":
                    #print("sol  piyon")
                    return True
    #sah
    kingmoves = [(-1,1),(0,1),(1,1),
            (-1,0),      (1,0),
            (-1,-1),(0,-1),(1,-1)]
    for dy,dx in kingmoves:
        if 0<=kingy + dy<=7 and 0<= kingx + dx <= 7:
            if board[kingy + dy][kingx + dx] == opposite_color + "K":
                return True
    return False

def comptochess(y,x):
    chars = "abcdefgh"
    return (chars[x],8 - y)

def compmovestochessmoves(movearr):
    res = []
    for piece,startcoord,endcoords in movearr:
        start = comptochess(startcoord[0],startcoord[1])
        prefix = f"{start[0]}{start[1]} "
        for endcoordy,endcoordx in endcoords:
            end = comptochess(endcoordy,endcoordx)
            word = prefix + f"{end[0]}{end[1]}"
            res.append(word)
    return sorted(res)

def chesstocomp(s):
    start,end = s.split()
    chars = "abcdefgh"
    compstart = (8 - int(start[1]),chars.index(start[0]))
    compend = ((8 - int(end[1]),chars.index(end[0])))
    return (compstart,compend)


opp_file = open(opponent_file)

opp_text = ""
for line in opp_file:
    opp_text += line
opponent_moves = opp_text.split("\n")
opponent_moves = [arr.split(",") for arr in opponent_moves]
def play(board,color,counter,pastmoves):
    opposite_color = "B"
    if color == "B":
        opposite_color = "W"
    new_board = []
    for r in board:
        new_board.append(r)
    if len(allmoves(board,opposite_color)) == 0:
        return pastmoves
    finishingmove = False
    want = []
    if counter == len(opponent_moves):
        finishingmove = True
    else:
        want = sorted(opponent_moves[counter])
    for piece,startcoord,actions in allmoves(board,color):
        for move in actions:
            temp = new_board[move[0]][move[1]]
            new_board[startcoord[0]][startcoord[1]] = 0
            new_board[move[0]][move[1]] = piece
            if finishingmove:
                totaloppmoves = 0
                for opppiece,oppcord,oppactions in allmoves(new_board,opposite_color):
                    totaloppmoves += len(oppactions)
                if totaloppmoves == 0:
                    return pastmoves + [(comptochess(startcoord[0],startcoord[1]),comptochess(move[0],move[1]))]
            elif sorted(compmovestochessmoves(allmoves(new_board,opposite_color))) == want:
                opposite_start,opposite_end = chesstocomp(opponent_moves[counter][0])
                opp_temp = new_board[opposite_end[0]][opposite_end[1]]
                opp_piece = new_board[opposite_start[0]][opposite_start[1]]
                new_board[opposite_end[0]][opposite_end[1]] = new_board[opposite_start[0]][opposite_start[1]]
                new_board[opposite_start[0]][opposite_start[1]] = 0
                rest = play(new_board,color,counter + 1,pastmoves + [(comptochess(startcoord[0],startcoord[1]),comptochess(move[0],move[1]))])
                if rest != None:
                    return rest
                new_board[opposite_end[0]][opposite_end[1]] = opp_temp
                new_board[opposite_start[0]][opposite_start[1]] = opp_piece
            new_board[move[0]][move[1]] = temp
            new_board[startcoord[0]][startcoord[1]] = piece
res = play(chessboard,color.upper()[0],0,[])
for start,end in res:
    print(f"{start[0]}{start[1]} {end[0]}{end[1]}")
print("",allmoves(chessboard,"W"))
print(allmoves(chessboard,"B"))
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

