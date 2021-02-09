The app helps you check if the playing field is ready to play.

The game field of the logical puzzle has a square shape of 9×9 blocks. The playing field contains different colored commands that are used in the game and white areas that are not used for playing. 

The commands of the playing field before the start of the game must be filled according to the following rules:
 -The squares of each row must contain digits from 1 to 9 without repeats.
 -The cells of each column must contain digits from 1 to 9 without repeats.
 -Each block of blocks of the same color must contain digits from 1 to 9 without repeats.

The check_uniqueness_in_rows checks the uniqueness of each digit in the coloured cells of the row. Returns True if didits in a row are unique, False otherwise:

    >>> check_uniqueness_in_rows(["**** ****" ,"***1 ****", "**  3****",\
         "* 4 5****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***",\
            "  2  ****"])
    True
    >>> check_uniqueness_in_rows(["**** ****" ,"***1 ****", "**  3****",\
         "* 4 4****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***",\
            "  2  ****"])
    False


The check_uniqueness_in_columns checks the uniqueness of each digit in the coloured cells of the column. Returns True if didits in a row are unique, False otherwise:

    >>> check_uniqueness_in_columns(["**** ****" ,"***1 ****", "**  3****",\
         "* 4 5****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***",\
            "  2  ****"])
    True
    >>> check_uniqueness_in_columns(["**** ****" ,"***1 ****", "**  3****",\
         "* 4 5****", "     9 5 ", " 6  53  *", "3   1  **", "  8  2***",\
            "  2  ****"])
    False


The check_uniqueness_in_colors checks the blocks of cells with the same colour. If the numbers in each block do not repeat, it returns True, False otherwise:

    >>> check_uniqueness_in_colors(["**** ****" ,"***1 ****", "**  3****",\
         "* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***",\
            "  2  ****"])
    True
    >>> check_uniqueness_in_colors(["**** ****" ,"***1 ****", "**  3****",\
         "* 4 5****", "     9 5 ", " 6  53  *", "3   1  **", "  8  2***",\
            "  2  ****"])
    False


The validate_board checks if the playing field is ready for play.

    >>> validate_board(["**** ****" ,"***1 ****", "**  3****",\
         "* 4 2****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***",\
            "  2  ****"])
    True
    >>> validate_board(["**** ****" ,"***1 ****", "**  3****",\
         "* 4 5****", "     9 5 ", " 6  53  *", "3   1  **", "  8  2***",\
            "  2  ****"])
    False