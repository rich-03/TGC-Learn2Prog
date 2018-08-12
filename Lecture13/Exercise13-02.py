def make_move(board, position, value):
    position -= 1  # change position to be 0-8
    pos1 = position // 3  # integer division gets the row number
    pos2 = position % 3  # modulus gives the column number
    board[pos1][pos2] = value
