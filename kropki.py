# Nabira Ahmad
# Artificial Intelligence 
# December 16, 2024

# necessary import
import copy

# PURPOSE: check if moving val to grid[row][col] is a valid move (if val already in grid, and checks dots)
# RETURN: true if valid move, false if not
def valid_move(grid, row, col, val, horiz_dots, vert_dots):
    # checks if val in row
    for j in range(9):
        if grid[row][j] == val:
            return False

    # checks if val in col
    for i in range(9):
        if grid[i][col] == val:
            return False

    # check each pos in the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            # check if val already exists in grid
            if grid[i][j] == val:
                return False
            
    # check the horizontal dots
    if col < 8 and grid[row][col + 1] != 0: 
        # if a neighbor exists 
        if horiz_dots[row][col] == 1 and abs(val - grid[row][col + 1]) != 1:
            # if there's a white dot (horizontally) and the diff. between cells is not 1, return false
            return False
        if horiz_dots[row][col] == 2 and not (
            val == 2 * grid[row][col + 1] or grid[row][col + 1] == 2 * val
        ):
            # if there's a black dot (horizontally) and the divison of the cells aren't 2, return false
            return False
        
    # check the vertical dots
    if row < 8 and grid[row + 1][col] != 0:  
        # if a neighbor exists
        if vert_dots[row][col] == 1 and abs(val - grid[row + 1][col]) != 1:
            # if there's a white dot (vertically) and the diff. between cells is not 1, return false
            return False
        
        if vert_dots[row][col] == 2 and not (
            val == 2 * grid[row + 1][col] or grid[row + 1][col] == 2 * val
        ):
            # if there's a black dot (vertically) and the divison of the cells aren't 2, return false
            return False
        
    # else, return true
    return True

# PURPOSE: looks for the next blank cell according to the Minimum Remaining Value Heuristics
# RETURNS: the next best cell to fill according to heuristic
def find_mrv_cell(grid, horiz_dots, vert_dots):
    # mrv = 10 -> minimum value =10 bc it has to be higher than the max. possible number of valid values for any cell
    mrv = 10 
    best_cell = None
    # iterate through the grid, look for blank cells
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0: 
                # if cell blank
                possible_values = sum(1 for num in range(1, 10) if valid_move(grid, i, j, num, horiz_dots, vert_dots))
                # loops through possible values (1-9) and checks if valid move
                # sum to take the # of possible values
                if possible_values < mrv:
                    mrv = possible_values
                    # if possible values < mrv update mrv
                    best_cell = (i, j)
    return best_cell

# PURPOSE: backtracking algorithm to solve the puzzle
# RETURN: returns true if solution exists to sudoku and false if not
def backtrack(grid, horiz_dots, vert_dots):
    # find the next cell to fill
    cell = find_mrv_cell(grid, horiz_dots, vert_dots)

    if not cell:
            # grid is full
        return True  

    row, col = cell
    # try to assign each number from 1-9 to the cell (use if valid move)
    for val in range(1, 10):
        if valid_move(grid, row, col, val, horiz_dots, vert_dots):
            # assign the value to the cell if valid
            grid[row][col] = val  
            if backtrack(grid, horiz_dots, vert_dots):
                # recurisve implementation to go to the rest of the grid
                return True
            grid[row][col] = 0 

    # if no values are valid return false
    return False

# PURPOSE: read input file and initialize grids
# RETURN: the grids
def read_input(filename):
    # read input file according to spacing and blank lines
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]  

    # first 9 rows = initial board grid
    grid = [list(map(int, lines[i].split())) for i in range(9)]

    # next 9 rows -> horizontal dots arrangement
    horiz_dots = [list(map(int, lines[i + 9].split())) for i in range(9)]

    # next 8 rows -> vertical dots arrangement
    vert_dots = [list(map(int, lines[i + 18].split())) for i in range(8)]
    
    return grid, horiz_dots, vert_dots

# PURPOSE: write the solved output grid to a new file
def write_output(grid, output_file):
    with open(output_file, 'w') as f:
        for row in grid:
            f.write(' '.join(map(str, row)) + '\n')

def main():
    # get input file
    input_file = input("Please enter the input file name: ").strip()
    try:
        # generate the output file according to the input file's name
        file_num = ''.join(filter(str.isdigit, input_file)) or "1"
        output_file = f"Output{file_num}.txt"

        # intialize the grids
        grid, horiz_dots, vert_dots = read_input(input_file)
        # debugging purposes:
        # print("start grid:")
        # for row in grid:
        #     print(row)
        # print("\nhorizontal dot grid:")
        # for row in horiz_dots:
        #     print(row)
        # print("\nvertical dot grid:")
        # for row in vert_dots:
        #     print(row)

        # call the backtrack algo to solve
        if backtrack(grid, horiz_dots, vert_dots):
            # give feedback that a solution was generated
            print("solved kropki sudoku!!")
            write_output(grid, output_file)
            print(f"output in {output_file}")
        else:
            print("solution cannot be found")

    # error handling
    except FileNotFoundError:
        print(f"error: file '{input_file}' not found")
    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    main()
