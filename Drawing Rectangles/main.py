# Elias Wolde
# Object-Oriented programming –-> Classes & Objects
# This program allows the user to move a rectangle around a grid

import rectangle
import check_input


def display_grid(grid):
    """
    This function display the contents of the grid

    Argument: display_grid(grid): passes in the grid

    """
    # For loop to diplay the 2d list in matrix form
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=' ')
        print()


def reset_grid(grid):
    """
    This function overwrites the contents of the grid with all ‘.’s. 

    Argument: display_grid(grid): passes in the grid

    """
    # filling the grid with '.'
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = '.'


def place_rect(grid, rect):
    """
    This function overwrites the ‘.’ characters with ‘*’s using the width and height of the rectangle at the location of 
the rectangle (x, y) on the grid 

    """
    # creating x and y cordiate
    y_cordinate = rect.get_coords()[0]
    x_cordinate = rect.get_coords()[1]

  # Filling the x and y cordinates with '*'
    for height in range(0, rect.get_height()):
        for width in range(0, rect.get_width()):
            grid[x_cordinate + height][y_cordinate + width] = '*'


def main():
    """
    This function main controlls the user height and width choice, the movement of the rectangle and checks the boundaries.

    """
    # Asking the user for the height and width
    rectWidth = check_input.get_int_range(
        "Enter rectangle width (1-5): ", 1, 5)
    rectHeight = check_input.get_int_range(
        "Enter rectangle height (1-5): ", 1, 5)

    # creating an object from the rectangle class
    rect = rectangle.Rectangle(rectWidth, rectHeight)

    # Creating the grid
    board = [[0 for i in range(0, 20)] for j in range(0, 20)]

    # while the user choice is not 0...
    choice = 0

    # While loop to repeatedly ask the user for the direction of the triangle
    while choice != 5:
        # prompting the user for direction
        choice = check_input.get_int_range(
            "Enter Direction:\n 1. Up\n 2. Down\n 3. Left\n 4. Right\n 5. Quit\n", 1, 5)

    # Conditionl statement to make sure the movement of the rectangle stays in the rectangle
        if choice == 1:
            # if the rectangle moves up initially, at 0, it will become negative which means out of the grid
            if rect.get_coords()[1] >= 1:
                rect.move_up()
                reset_grid(board)
                place_rect(board, rect)
                display_grid(board)
            else:
                print("Out of the rectangle. Please move inside!")
        elif choice == 2:
            # if the rectangle moves down 20+, it will cross the grid
            if (rect.get_coords()[1] + rect.height) < 20:
                rect.move_down()
                reset_grid(board)
                place_rect(board, rect)
                display_grid(board)
            else:
                print("Out of the rectangle. Please move inside!")
        elif choice == 3:
            # if the rectangle moves left initially, at 0, it will become negative which means out of the grid
            if rect.get_coords()[0] >= 1:
                rect.move_left()
                reset_grid(board)
                place_rect(board, rect)
                display_grid(board)
            else:
                print("Out of the rectangle. Please move inside!")
        elif choice == 4:
           # if the rectangle moves right 20+, it will cross the grid
            if (rect.get_coords()[0] + rect.width) < 20:
                rect.move_right()
                reset_grid(board)
                place_rect(board, rect)
                display_grid(board)
            else:
                print("Out of the rectangle. Please move inside!")
        elif choice == 5:
            break


main()
