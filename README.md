## Kropki Sudoku Solver 🧩
This is a Python-based solver for Kropki Sudoku puzzles, a variant of Sudoku that includes additional constraints using white and black dots:
- A white dot between two cells indicates that the numbers are consecutive.
- A black dot indicates that one number is double the other.
- 
The program efficiently solves Kropki Sudoku using:

1. Backtracking algorithm for assigning values.
2. Minimum Remaining Value (MRV) heuristic to reduce the search space.

# Features 📋
- Reads input from a text file containing the grid and Kropki dot constraints
- Solves the puzzle and generates an output file with the solution
- Supports standard 9x9 Sudoku grid format
- Implements advanced CSP techniques for efficiency

# How to Run 🚀
1. Clone the repository
2. Make sure input file is in the same directory as the .py file
3. Run the program
4. Enter the input file name when prompted (e.g., Input5.txt).
The solved grid will be saved in an output file (e.g., Output5.txt)

*Sample output files are provided*

# Input Format 📄
- First 9 lines: Sudoku grid with 0 representing empty cells.
- Next 9 lines: Horizontal Kropki dots (0 for none, 1 for consecutive, 2 for double).
- Final 8 lines: Vertical Kropki dots in the same format.

