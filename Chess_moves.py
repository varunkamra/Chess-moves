# This program calculates the moves of all the chess pieces from a given chess board configuration

# board variable represents the chess board configuration;
# lower case characters represent black pieces and upper case represents white peices.
board=[['r','kn',' ','q','k',' ',' ','r'],[' ','b',' ','p',' ','p',' ','p'],[' ',' ','p','b',' ','kn',' ',' '],['p',' ',' ',' ','p',' ',' ',' '],[' ',' ',' ','P',' ',' ',' ',' '],[' ','P','KN','Q',' ','KN',' ',' '],['P',' ','P',' ','P',' ','P',' '],['R',' ','B',' ','K','B',' ','R']]

# generates the player pieces
def player_pieces(board,player):
    for i in range(len(board)):
        for j in range(len(board)):
            if(player==1 and board[i][j]!=' ' and not board[i][j].islower()):
                yield(board[i][j],(i,j))
            elif(player==2 and board[i][j].islower()):
                yield(board[i][j],(i,j))

# moves_pawn calculates the possible moves of all the pawns on the chess board
def moves_pawn(board,player,t):
    list=[]
    if(player==1):
        if(t[0]==6):
            if(board[t[0]-2][t[1]]==' ' and board[t[0]-1][t[1]]==' '):
                list.append(((t),(t[0]-2,t[1])))
        if(board[t[0]-1][t[1]]==' '):
            list.append(((t),(t[0]-1,t[1])))
        if(not(t[1]-1<0) and board[t[0]-1][t[1]-1].islower() and board[t[0]-1][t[1]-1]!='k'):
            list.append(((t),(t[0]-1,t[1]-1)))
        if(not(t[1]+1>7) and board[t[0]-1][t[1]+1].islower() and board[t[0]-1][t[1]+1]!='k'):
            list.append(((t),(t[0]-1,t[1]+1)))
    else:
        if(t[0]==1):
            if(board[t[0]+2][t[1]]==' ' and board[t[0]+1][t[1]]==' '):
                list.append(((t),(t[0]+2,t[1])))
        if(board[t[0]+1][t[1]]==' '):
            list.append(((t),(t[0]+1,t[1])))
        if(not(t[1]-1<0)and not board[t[0]+1][t[1]-1]==' ' and not board[t[0]+1][t[1]-1].islower() and board[t[0]+1][t[1]-1]!='K'):
            list.append(((t),(t[0]+1,t[1]-1)))
        if(not(t[1]+1>7)and not board[t[0]+1][t[1]+1]==' ' and not board[t[0]+1][t[1]+1].islower() and board[t[0]+1][t[1]+1]!='K'):
            list.append(((t),(t[0]+1,t[1]+1)))
    return list

# function for calculating moves of all the bishops on the board
def moves_bishop(board,player,t):
    list=[]
    i=1
    j=1
    
    while(not t[0]-i<0 and not t[1]+j>7 and board[t[0]-i][t[1]+j]==' '):
        list.append(((t),(t[0]-i,t[1]+j)))
        i+=1
        j+=1
    if(player==1 and not t[0]-i<0 and not t[1]+j>7 and board[t[0]-i][t[1]+j].islower() and board[t[0]-i][t[1]+j].lower()!='k' ):
        list.append(((t),(t[0]-i,t[1]+j)))

    if(player==2 and not t[0]-i<0 and not t[1]+j>7 and not board[t[0]-i][t[1]+j].islower() and board[t[0]-i][t[1]+j].lower()!='k' ):
        list.append(((t),(t[0]-i,t[1]+j)))

    i=1
    j=1
    while(not t[0]-i<0 and not t[1]-j<0 and board[t[0]-i][t[1]-j]==' '):
        list.append(((t),(t[0]-i,t[1]-j)))
        i+=1
        j+=1
    if(player==1 and not t[0]-i<0 and not t[1]-j<0 and board[t[0]-i][t[1]-j].islower() and board[t[0]-i][t[1]-j].lower()!='k'):
        list.append(((t),(t[0]-i,t[1]-j)))

    if(player==2 and not t[0]-i<0 and not t[1]-j<0 and not board[t[0]-i][t[1]-j].islower() and board[t[0]-i][t[1]-j].lower()!='k'):
        list.append(((t),(t[0]-i,t[1]-j)))

    i=1
    j=1
    while(not t[0]+i>7 and not t[1]-j<0 and board[t[0]+i][t[1]-j]==' '):
        list.append(((t),(t[0]+i,t[1]-j)))
        i+=1
        j+=1
    if(player==1 and not t[0]+i>7 and not t[1]-j<0 and board[t[0]+i][t[1]-j].islower() and board[t[0]+i][t[1]-j].lower()!='k'):
        list.append(((t),(t[0]-i,t[1]-j)))

    if(player==2 and not t[0]+i>7 and not t[1]-j<0 and not board[t[0]+i][t[1]-j].islower() and board[t[0]+i][t[1]-j].lower()!='k'):
        list.append(((t),(t[0]-i,t[1]-j)))

    i=1
    j=1
    while(not t[0]+j>7 and not t[1]+j>7 and board[t[0]+i][t[1]+j]==' '):
        list.append(((t),(t[0]+i,t[1]+j)))
        i+=1
        j+=1
    if(player==1 and not t[0]+j>7 and not t[1]+j>7 and board[t[0]+i][t[1]+j].islower() and board[t[0]+i][t[1]+j].lower()!='k'):
        list.append(((t),(t[0]+i,t[1]+j)))

    if(player==2 and not t[0]+j>7 and not t[1]+j>7 and not board[t[0]+i][t[1]+j].islower() and board[t[0]+i][t[1]+j].lower()!='k'):
        list.append(((t),(t[0]+i,t[1]+j)))

    return list

# function for calculating moves of both Queens on the board
def moves_queen(board,player,t):
    list=[]

    #queen moves up-right for player 1 and down-left for player 2
    i=1
    j=1
    while(not t[0]-i<0 and not t[1]+j>7 and board[t[0]-i][t[1]+j]==' '):
        list.append(((t),(t[0]-i,t[1]+j)))
        i+=1
        j+=1
    if(player==1 and not t[0]-i<0 and not t[1]+j>7 and board[t[0]-i][t[1]+j].islower() and board[t[0]-i][t[1]+j].lower()!='k'):
        list.append(((t),(t[0]-i,t[1]+j)))

    if(player==2 and not t[0]-i<0 and not t[1]+j>7 and not board[t[0]-i][t[1]+j].islower() and board[t[0]-i][t[1]+j].lower()!='k'):
        list.append(((t),(t[0]-i,t[1]+j)))

    #queen moves up-left for player 1 and down-right for player 2
    i=1
    j=1
    while(not t[0]-i<0 and not t[1]-j<0 and board[t[0]-i][t[1]-j]==' '):
        list.append(((t),(t[0]-i,t[1]-j)))
        i+=1
        j+=1
    if(player==1 and not t[0]-i<0 and not t[1]-j<0 and board[t[0]-i][t[1]-j].islower() and board[t[0]-i][t[1]-j].lower()!='k'):
        list.append(((t),(t[0]-i,t[1]-j)))

    if(player==2 and not t[0]-i<0 and not t[1]-j<0 and not board[t[0]-i][t[1]-j].islower() and board[t[0]-i][t[1]-j].lower()!='k'):
        list.append(((t),(t[0]-i,t[1]-j)))

    #queen moves down-left for player 1 and up-right for player 2
    i=1
    j=1
    while(not t[0]+i>7 and not t[1]-j<0 and board[t[0]+i][t[1]-j]==' '):
        list.append(((t),(t[0]+i,t[1]-j)))
        i+=1
        j+=1
    if(player==1 and not t[0]+i>7 and not t[1]-j<0 and board[t[0]+i][t[1]-j].islower() and board[t[0]+i][t[1]-j].lower()!='k'):
        list.append(((t),(t[0]-i,t[1]-j)))

    if(player==2 and not t[0]+i>7 and not t[1]-j<0 and not board[t[0]+i][t[1]-j].islower() and board[t[0]+i][t[1]-j].lower()!='k'):
        list.append(((t),(t[0]-i,t[1]-j)))

    #queen moves down-right for player 1 and up-left for player 2
    i=1
    j=1
    while(not t[0]+i>7 and not t[1]+j>7 and board[t[0]+i][t[1]+j]==' '):
        list.append(((t),(t[0]+i,t[1]+j)))
        i+=1
        j+=1
    if(player==1 and not t[0]+j>7 and not t[1]+j>7 and board[t[0]+i][t[1]+j].islower() and board[t[0]+i][t[1]+j].lower()!='k'):
        list.append(((t),(t[0]+i,t[1]+j)))

    if(player==2 and not t[0]+j>7 and not t[1]+j>7 and not board[t[0]+i][t[1]+j].islower() and board[t[0]+i][t[1]+j].lower()!='k'):
        list.append(((t),(t[0]+i,t[1]+j)))

    #queen moves up
    i=1
    while(not t[0]-i<0 and board[t[0]-i][t[1]]==' '):
        list.append(((t),(t[0]-i,t[1])))
        i+=1
    if(player==1 and not t[0]-i<0 and board[t[0]-i][t[1]].islower() and board[t[0]-i][t[1]].lower()!='k'):
        list.append(((t),(t[0]-i,t[1])))

    if(player==2 and not t[0]-i<0 and not board[t[0]-i][t[1]].islower() and board[t[0]-i][t[1]].lower()!='k'):
        list.append(((t),(t[0]-i,t[1])))

    #queen moves down
    i=1
    while(not t[0]+i>7 and board[t[0]+i][t[1]]==' '):
        list.append(((t),(t[0]+i,t[1])))
        i+=1
    if(player==1 and not t[0]+i>7 and board[t[0]+i][t[1]].islower() and board[t[0]+i][t[1]].lower()!='k'):
        list.append(((t),(t[0]+i,t[1])))

    if(player==2 and not t[0]+i>7 and not board[t[0]+i][t[1]].islower() and board[t[0]+i][t[1]].lower()!='k'):
        list.append(((t),(t[0]+i,t[1])))

    #queen moves right for player 1 and left for player 2
    j=1
    while(not t[1]+j>7 and board[t[0]][t[1]+j]==' '):
        list.append(((t),(t[0],t[1]+j)))
        j+=1
    if(player==1 and not t[1]+j>7 and board[t[0]][t[1]+j].islower() and board[t[0]][t[1]+j].lower()!='k'):
        list.append(((t),(t[0],t[1]+j)))

    if(player==2 and not t[1]+j>7 and not board[t[0]][t[1]+j].islower() and board[t[0]][t[1]+j].lower()!='k'):
        list.append(((t),(t[0],t[1]+j)))

    #queen moves left for player 1 and right for player 2
    j=1
    while(not t[1]-j<0 and board[t[0]][t[1]-j]==' '):
        list.append(((t),(t[0],t[1]-j)))
        j+=1
    if(player==1 and not t[1]-j<0 and board[t[0]][t[1]-j].islower() and board[t[0]][t[1]-j].lower()!='k'):
        list.append(((t),(t[0],t[1]-j)))

    if(player==2 and not t[1]-j<0 and not board[t[0]][t[1]-j].islower() and board[t[0]][t[1]-j].lower()!='k'):
        list.append(((t),(t[0],t[1]-j)))

    return list

# function for calculating moves of a rook.
def moves_rook(board,player,t):
    list=[]
    #rook moves up
    i=1
    while(not t[0]-i<0 and board[t[0]-i][t[1]]==' '):
        list.append(((t),(t[0]-i,t[1])))
        i+=1
    if(player==1 and not t[0]-i<0 and board[t[0]-i][t[1]].islower() and board[t[0]-i][t[1]].lower()!='k' ):
        list.append(((t),(t[0]-i,t[1])))
    if(player==2 and not t[0]-i<0 and not board[t[0]-i][t[1]].islower() and board[t[0]-i][t[1]].lower()!='k' ):
        list.append(((t),(t[0]-i,t[1])))

    #rook moves down
    i=1
    while(not t[0]+i>7 and board[t[0]+i][t[1]]==' '):
        list.append(((t),(t[0]+i,t[1])))
        i+=1
    if(player==1 and not t[0]+i>7 and board[t[0]+i][t[1]].islower() and board[t[0]+i][t[1]].lower()!='k' ):
        list.append(((t),(t[0]+i,t[1])))
    if(player==2 and not t[0]+i>7 and not board[t[0]+i][t[1]].islower() and board[t[0]+i][t[1]].lower()!='k' ):
        list.append(((t),(t[0]+i,t[1])))

    #rook moves right for player 1 and left for player 2
    j=1
    while(not t[1]+j>7 and board[t[0]][t[1]+j]==' ' ):
        list.append(((t),(t[0],t[1]+j)))
        j+=1
    if(player==1 and not t[1]+j>7 and board[t[0]][t[1]+j].islower() and board[t[0]][t[1]+j].lower()!='k'):
        list.append(((t),(t[0],t[1]+j)))
    if(player==2 and not t[1]+j>7 and not board[t[0]][t[1]+j].islower() and board[t[0]][t[1]+j].lower()!='k'):
        list.append(((t),(t[0],t[1]+j)))

    #rook moves left for player 1 and right for player 2
    j=1
    while(not t[1]-j<0 and board[t[0]][t[1]-j]==' ' ):
        list.append(((t),(t[0],t[1]-j)))
        j+=1
    if(player==1 and not t[1]-j<0 and board[t[0]][t[1]-j].islower() and board[t[0]][t[1]-j].lower()!='k' ):
        list.append(((t),(t[0],t[1]-j)))
    if(player==2 and not t[1]-j<0 and not board[t[0]][t[1]-j].islower() and board[t[0]][t[1]-j].lower()!='k' ):
        list.append(((t),(t[0],t[1]-j)))

    return list

# function for calculating the moves of both Kings on the board.
def moves_king(board,player,t):
    list=[]
    #king moves up for player 1 and moves down for player 2
    if(player==1 and not t[0]-1<0 and (board[t[0]-1][t[1]]==' ' or (board[t[0]-1][t[1]].islower() and board[t[0]-1][t[1]].lower()!='k'))):
        list.append(((t),(t[0]-1,t[1])))

    if(player==2 and not t[0]-1<0 and (board[t[0]-1][t[1]]==' ' or (not board[t[0]-1][t[1]].islower() and board[t[0]-1][t[1]].lower()!='k'))):
        list.append(((t),(t[0]-1,t[1])))

    #king moves down for player 1 and moves up for player 2
    if(player==1 and not t[0]+1>7 and (board[t[0]+1][t[1]]==' ' or (board[t[0]+1][t[1]].islower() and board[t[0]+1][t[1]].lower()!='k'))):
        list.append(((t),(t[0]+1,t[1])))

    if(player==2 and not t[0]+1>7 and (board[t[0]+1][t[1]]==' ' or (not board[t[0]+1][t[1]].islower() and board[t[0]+1][t[1]].lower()!='k'))):
        list.append(((t),(t[0]+1,t[1])))

    #king moves right for player 1 and left for player 2
    if(player==1 and not t[1]+1>7 and (board[t[0]][t[1]+1]==' ' or (board[t[0]][t[1]+1].islower() and board[t[0]][t[1]+1].lower()!='k'))):
        list.append(((t),(t[0],t[1]+1)))

    if(player==2 and not t[1]+1>7 and (board[t[0]][t[1]+1]==' ' or (not board[t[0]][t[1]+1].islower() and board[t[0]][t[1]+1].lower()!='k'))):
        list.append(((t),(t[0],t[1]+1)))

    #king moves left for player 1 and right for player 2
    if(player==1 and not t[1]-1<0 and  (board[t[0]][t[1]-1]==' ' or(board[t[0]][t[1]-1].islower() and board[t[0]][t[1]-1].lower()!='k'))):
        list.append(((t),(t[0],t[1]-1)))

    if(player==2 and not t[1]-1<0 and  (board[t[0]][t[1]-1]==' ' or(not board[t[0]][t[1]-1].islower() and board[t[0]][t[1]-1].lower()!='k'))):
        list.append(((t),(t[0],t[1]-1)))

    #queen moves up-right for player 1 and down-left for player 2
    if(player==1 and not t[0]-1<0 and not t[1]+1>7 and  (board[t[0]-1][t[1]+1]==' ' or (board[t[0]-1][t[1]+1].islower() and board[t[0]-1][t[1]+1].lower()!='k'))):
        list.append(((t),(t[0]-1,t[1]+1)))

    if(player==2 and not t[0]-1<0 and not t[1]+1>7 and  (board[t[0]-1][t[1]+1]==' ' or (not board[t[0]-1][t[1]+1].islower() and board[t[0]-1][t[1]+1].lower()!='k'))):
        list.append(((t),(t[0]-1,t[1]+1)))

    #queen moves up-left for player 1 and down-right for player 2
    if(player==1 and not t[0]-1<0 and not t[1]-1<0 and (board[t[0]-1][t[1]-1]==' ' or (board[t[0]-1][t[1]-1].islower() and board[t[0]-1][t[1]-1].lower()!='k'))):
        list.append(((t),(t[0]-1,t[1]-1)))

    if(player==2 and not t[0]-1<0 and not t[1]-1<0 and (board[t[0]-1][t[1]-1]==' ' or (not board[t[0]-1][t[1]-1].islower() and board[t[0]-1][t[1]-1].lower()!='k'))):
        list.append(((t),(t[0]-1,t[1]-1)))

    #queen moves down-left for player 1 and up-right for player 2
    if(player==1 and not t[0]+1>7 and not t[1]-1<0 and (board[t[0]+1][t[1]-1]==' ' or (board[t[0]+1][t[1]-1].islower() and board[t[0]+1][t[1]-1].lower()!='k'))):
        list.append(((t),(t[0]-1,t[1]-1)))

    if(player==2 and not t[0]+1>7 and not t[1]-1<0 and (board[t[0]+1][t[1]-1]==' ' or (not board[t[0]+1][t[1]-1].islower() and board[t[0]+1][t[1]-1].lower()!='k'))):
        list.append(((t),(t[0]-1,t[1]-1)))

    #queen moves down-right for player 1 and up-left for player 2
    if(player==1 and not t[0]+1>7 and not t[1]+1>7 and (board[t[0]+1][t[1]+1]==' ' or (board[t[0]+1][t[1]+1].islower() and board[t[0]+1][t[1]+1].lower()!='k'))):
        list.append(((t),(t[0]+1,t[1]+1)))

    if(player==2 and not t[0]+1>7 and not t[1]+1>7 and (board[t[0]+1][t[1]+1]==' ' or (not board[t[0]+1][t[1]+1].islower() and board[t[0]+1][t[1]+1].lower()!='k'))):
        list.append(((t),(t[0]+1,t[1]+1)))

    return list

# function for calculating moves of the Knight
def moves_knight(board,player,t):
    list=[]
    if(player==1 and not(t[0]+1>7) and not (t[1]+2>7) and (board[t[0]+1][t[1]+2]==' ' or (board[t[0]+1][t[1]+2].islower() and board[t[0]+1][t[1]+2].lower()!='k'))):
        list.append(((t),(t[0]+1,t[1]+2)))

    if(player==2 and not(t[0]+1>7) and not (t[1]+2>7) and (board[t[0]+1][t[1]+2]==' ' or (not board[t[0]+1][t[1]+2].islower() and board[t[0]+1][t[1]+2].lower()!='k'))):
        list.append(((t),(t[0]+1,t[1]+2)))

    if(player==1 and not t[0]-1<0 and not t[1]+2>7 and (board[t[0]-1][t[1]+2]==' ' or (board[t[0]-1][t[1]+2].islower() and board[t[0]-1][t[1]+2].lower()!='k'))):
        list.append(((t),(t[0]-1,t[1]+2)))

    if(player==2 and not t[0]-1<0 and not t[1]+2>7 and (board[t[0]-1][t[1]+2]==' ' or (not board[t[0]-1][t[1]+2].islower() and board[t[0]-1][t[1]+2].lower()!='k'))):
        list.append(((t),(t[0]-1,t[1]+2)))

    if(player==1 and not t[0]+1>7 and not t[1]-2<0 and (board[t[0]+1][t[1]-2]==' ' or (board[t[0]+1][t[1]-2].islower() and board[t[0]+1][t[1]-2].lower()!='k'))):
        list.append(((t),(t[0]+1,t[1]-2)))

    if(player==2 and not t[0]+1>7 and not t[1]-2<0 and (board[t[0]+1][t[1]-2]==' ' or (not board[t[0]+1][t[1]-2].islower() and board[t[0]+1][t[1]-2].lower()!='k'))):
        list.append(((t),(t[0]+1,t[1]-2)))

    if(player==1 and not t[0]-1<0  and not t[1]-2<0 and (board[t[0]-1][t[1]-2]==' ' or (board[t[0]-1][t[1]-2].islower() and board[t[0]-1][t[1]-2].lower()!='k'))):
        list.append(((t),(t[0]-1,t[1]-2)))

    if(player==2 and not t[0]-1<0  and not t[1]-2<0 and (board[t[0]-1][t[1]-2]==' ' or (not board[t[0]-1][t[1]-2].islower() and board[t[0]-1][t[1]-2].lower()!='k'))):
        list.append(((t),(t[0]-1,t[1]-2)))

    if(player==1 and not t[0]-2<0 and not t[1]+1>7 and (board[t[0]-2][t[1]+1]==' ' or (board[t[0]-2][t[1]+1].islower() and board[t[0]-2][t[1]+1].lower()!='k'))):
        list.append(((t),(t[0]-2,t[1]+1)))

    if(player==2 and not t[0]-2<0 and not t[1]+1>7 and (board[t[0]-2][t[1]+1]==' ' or (not board[t[0]-2][t[1]+1].islower() and board[t[0]-2][t[1]+1].lower()!='k'))):
        list.append(((t),(t[0]-2,t[1]+1)))

    if(player==1 and not t[0]-2<0 and not t[1]-1<0 and (board[t[0]-2][t[1]-1]==' ' or (board[t[0]-2][t[1]-1].islower() and board[t[0]-2][t[1]-1].lower()!='k'))):
        list.append(((t),(t[0]-2,t[1]-1)))

    if(player==2 and not t[0]-2<0 and not t[1]-1<0 and (board[t[0]-2][t[1]-1]==' ' or (not board[t[0]-2][t[1]-1].islower() and board[t[0]-2][t[1]-1].lower()!='k'))):
        list.append(((t),(t[0]-2,t[1]-1)))

    if(player==1 and not t[0]+2>7 and not t[1]+1>7 and (board[t[0]+2][t[1]+1]==' ' or (board[t[0]+2][t[1]+1].islower() and board[t[0]+2][t[1]+1].lower()!='k'))):
        list.append(((t),(t[0]+2,t[1]+1)))

    if(player==2 and not t[0]+2>7 and not t[1]+1>7 and (board[t[0]+2][t[1]+1]==' ' or (not board[t[0]+2][t[1]+1].islower() and board[t[0]+2][t[1]+1].lower()!='k'))):
        list.append(((t),(t[0]+2,t[1]+1)))

    if(player==1 and not t[0]+2>7 and not t[1]-1<0 and (board[t[0]+2][t[1]-1]==' ' or (board[t[0]+2][t[1]-1].islower() and board[t[0]+2][t[1]-1].lower()!='k'))):
        list.append(((t),(t[0]+2,t[1]-1)))

    if(player==2 and not t[0]+2>7 and not t[1]-1<0 and (board[t[0]+2][t[1]-1]==' ' or (not board[t[0]+2][t[1]-1].islower() and board[t[0]+2][t[1]-1].lower()!='k'))):
        list.append(((t),(t[0]+2,t[1]-1)))

    return list

# function that calls proper functions based on the type of piece it receives.        
def moves_function(piece):
    if(piece.lower()=='p'):
        return moves_pawn
    elif(piece.lower()=='r'):
        return moves_rook
    elif(piece.lower()=='b'):
        return moves_bishop
    elif(piece.lower()=='q'):
        return moves_queen
    elif(piece.lower()=='kn'):
        return moves_knight
    elif(piece.lower()=='k'):
        return moves_king

# Main function that finds all the moves of the specified player.
def possible_moves(board,player):
    list=[]
    for i in player_pieces(board,int(player)):
        f=moves_function(i[0])
        list.append(f(board,int(player),i[1]))
    return list

def getColumn(n):
    if(n==0):
        return "A"
    if(n==1):
        return "B"
    if(n==2):
        return "C"
    if(n==3):
        return "D"
    if(n==4):
        return "E"
    if(n==5):
        return "F"
    if(n==6):
        return "G"
    if(n==7):
        return "H"

def getRow(n):
    if(n==0):
        return "8"
    if(n==1):
        return "7"
    if(n==2):
        return "6"
    if(n==3):
        return "5"
    if(n==4):
        return "4"
    if(n==5):
        return "3"
    if(n==6):
        return "2"
    if(n==7):
        return "1"
list1=possible_moves(board,1)
print("Player 1 moves:")
for i in list1:
    for j in i:
        print(getColumn(j[0][1])+getRow(j[0][0])+" to "+getColumn(j[1][1])+getRow(j[1][0])+" ")

print("\nPlayer 2 moves:")    
list2=possible_moves(board,2)
for i in list2:
    for j in i:
        print(getColumn(j[0][1])+getRow(j[0][0])+" to "+getColumn(j[1][1])+getRow(j[1][0])+" ")


