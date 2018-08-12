def first_row(board):
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
        return 'X'
    elif board[0][0] == '0' and board[0][1] == '0' and board[0][2] == '0':
        return '0'
    else:
        return '.'
