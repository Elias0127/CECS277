# Elias Woldie
# Python –-> 2D Lists
# This program generates a RxC solution board for the game Minesweeper.

import check_input
import random


def place_mines(board, mines):
    '''This function generates a random row and
    column within the bounds of the grid and check that location.

    Args: place_mines(board): takes the value of the board
    Args: place_mines(mines): takes the number of values
    '''

    num_rows = len(board)
    num_cols = len(board[0])
    i = 0
    # Generating random values for row and column
    while (i < mines):
        r = random.randint(0, num_rows-1)
        c = random.randint(0, num_cols-1)
        if board[r][c] == 0:
            board[r][c] = 'X'
            i += 1


def count_mines(board):
    '''This function counts any ‘X’s in the surrounding eight spaces, then place the value of the counter in that
    spot.

    Args: count_mines(board): takes the size of the grid
    '''
    # Use a nested set of loops to iterate through the surrounding eight spaces.
    for i in range(len(board)):
        for j in range(len(board[0])):
            count = 0
            if board[i][j] == 'X':
                for y in range(i - 1, i + 1):
                    for k in range(j - 1, j + 1):
                        # checking if both y and k are between 0 and the width or height of the 2d list
                        if y >= 0 and k >= 0 and y <= len(board) - 1 and k <= len(board) - 1:
                            if board[y][k] != 'X':
                                count += 1
                                board[y][k] = count


def display_board(board):
    '''This function displays the contents of the grid using a set of nested
    loops.

    Args: display_board(board): takes the size of the board
    '''

    # The for loop here iterates inside the board and prints each element in a matrix form
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print()


def main():

    print("Minesweeper Maker")

    # asks the user to input the size of the row, column, and mines
    rows = check_input.get_int_range("Enter number of rows (5-10): ", 5, 10)
    columns = check_input.get_int_range(
        "Enter number of columns (5-10): ", 5, 10)
    bombs = check_input.get_int_range("Enter number of mines (5-10): ", 5, 10)

    # Creating the grid per the given sizes by the user
    grid = [[0 for i in range(0, rows)] for j in range(0, columns)]

    place_mines(grid, bombs)
    count_mines(grid)
    display_board(grid)


main()
