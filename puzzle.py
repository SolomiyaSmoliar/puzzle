'''
PUZZLE
'''


def check_uniqueness_in_rows(board: list):
    """
    Checks the uniqueness of each digit in
    the coloured cells of the row.

    Return True if didits in a row are unique, False otherwise.

    >>> check_uniqueness_in_rows(["**** ****" ,"***1 ****", "**  3****",\
         "* 4 5****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***",\
            "  2  ****"])
    True
    >>> check_uniqueness_in_rows(["**** ****" ,"***1 ****", "**  3****",\
         "* 4 4****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***",\
            "  2  ****"])
    False
    >>> check_uniqueness_in_rows(["**** ****" ,"***1 ****", "**  3****",\
         "* 4 5****", "     9 9 ", " 6  83  *", "3   1  **", "  8  2***",\
            "  2  ****"])
    False
    """
    for i in range(0, len(board)):
        check_number_in_str = any(map(str.isdigit, board[i]))
        if check_number_in_str:
            numbers = []
            for j in board[i]:
                try:
                    numbers.append(int(j))
                except:
                    pass
            if len(numbers) != len(set(numbers)):
                result = False
                break
            else:
                result = True
    return result


def check_uniqueness_in_columns(board: list):
    """
    Checks the uniqueness of each digit in
    the coloured cells of the column.

    Return True if didits in a row are unique, False otherwise.

    >>> check_uniqueness_in_columns(["**** ****" ,"***1 ****", "**  3****",\
         "* 4 5****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***",\
            "  2  ****"])
    True
    >>> check_uniqueness_in_columns(["**** ****" ,"***1 ****", "**  3****",\
         "* 4 5****", "     9 5 ", " 6  53  *", "3   1  **", "  8  2***",\
            "  2  ****"])
    False
    >>> check_uniqueness_in_columns(["**** ****" ,"***1 ****", "**  3****",\
         "* 4 5****", "     9 5 ", " 6  83  *", "3   1  **", "  8  3***",\
            "  2  ****"])
    False
    """
    new_board = []
    for i in range(0, len(board)):
        new_list = ''.join(list(map(lambda x: x[i], board)))
        new_board.append(new_list)
    # ------------------------------
    result = check_uniqueness_in_rows(new_board)
    return result


def check_uniqueness_in_colors(board: list):
    '''
    Check the blocks of cells with the same colour.
    If the numbers in each block do not repeat,
    it returns True, False otherwise.

    >>> check_uniqueness_in_colors(["**** ****" ,"***1 ****", "**  3****",\
         "* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***",\
            "  2  ****"])
    True
    >>> check_uniqueness_in_colors(["**** ****" ,"***1 ****", "**  3****",\
         "* 4 5****", "     9 5 ", " 6  53  *", "3   1  **", "  8  2***",\
            "  2  ****"])
    False
    >>> check_uniqueness_in_colors(["**** ****" ,"***1 ****", "**  3****",\
         "* 4 9****", "     9 5 ", " 6  83  *", "3   1  **", "  8  3***",\
            "  2  ****"])
    False
    '''
    new_board = []
    new_board_1 = []
    new_board_2 = []
    for i in range(0, len(board)):
        new_board.append(board[i][8 - i:])
    # ------------------------------
    for i in range(0, len(board)):
        new_list = ''.join(list(map(lambda x: x[i], board)))
        new_board_1.append(new_list[0:8 - i])
    new_board_1.reverse()
    for i, j in zip(new_board, new_board_1):
        new_board_2.append(i + j)
     # ------------------------------
    result = check_uniqueness_in_rows(new_board_2)
    return result


def validate_board(board: list):
    '''
    Checks that the playing field is ready for play.

    >>> validate_board(["**** ****" ,"***1 ****", "**  3****",\
         "* 4 2****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***",\
            "  2  ****"])
    True
    >>> validate_board(["**** ****" ,"***1 ****", "**  3****",\
         "* 4 5****", "     9 5 ", " 6  53  *", "3   1  **", "  8  2***",\
            "  2  ****"])
    False
    >>> validate_board(["**** ****" ,"***1 ****", "**  3****",\
         "* 4 9****", "     9 5 ", " 6  83  *", "3   1  **", "  8  3***",\
            "  2  ****"])
    False
    '''
    for i in range(0, len(board)):
        check_number_in_str = list(map(str.isdigit, board[i]))
        if True not in check_number_in_str:
            result = True
        else:
            result_1 = check_uniqueness_in_rows(board)
            result_2 = check_uniqueness_in_columns(board)
            result_3 = check_uniqueness_in_colors(board)
            if result_1 == False or result_2 == False or result_3 == False:
                result = False
            else:
                result = True
    return result
