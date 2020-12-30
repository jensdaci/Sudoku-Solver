# Jens Daci 

#--- Sudoku Solver ---

# Reads the file named "sudoku_puzzle.txt"
# Solves the puzzle 
# Displays the solution on screen
# Saves the solution in another text file named "sudoku_solution.txt"

#--- Reading the puzzle from the file
def readBoard(filename):
	board = [[0] * 9] * 9
	f = open(filename, "r")

	for i in range (9):
		lines = f.readline().split(" | ", 2)
		row = []
		
		for j in range (3):
			num = lines[j].split("  ", 2)
			num = list(map(int, num))
			row.extend(num)
			board[i] = row
	f.close()

	return board
	
#--- Writing the solution into a file
def writeSolution(puzzle):
	f = open("sudoku_solution.txt", "w+")
	board = puzzle
	
	for i in range (9):
		for j in range (9):
			f.write("%d  " % board[i][j])
		
		f.write("\n")
	
	f.close()
	
#--- Drawing the board for better visual
def drawPuzzle(puzzle):
    for i in range(len(puzzle)):
        if i % 3 == 0:
            print("------------------------")
			
        for j in range(len(puzzle[0])):
            if j % 3 == 0:
                print("| ", end="")

            if j == 8:
                print(puzzle[i][j])
            else:
                print(str(puzzle[i][j]) + " ", end="")
    print("------------------------")

#--- Entering numbers into an empty box
def solvePuzzle(puzzle):
    find = isEmpty(puzzle)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if validEntry(puzzle, i, (row, col)):
            puzzle[row][col] = i

            if solvePuzzle(puzzle):
                return True

            puzzle[row][col] = 0

    return False

#--- Checking if the entry is valid
def validEntry(puzzle, number, position):
    # Rows
    for i in range(len(puzzle[0])):
        if puzzle[position[0]][i] == number and position[1] != i:
            return False

    # Columns
    for i in range(len(puzzle)):
        if puzzle[i][position[1]] == number and position[0] != i:
            return False

    # Sudoku Square
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if puzzle[i][j] == number and (i,j) != position:
                return False

    return True
	
#--- Checking if the puzzle entry is empty
def isEmpty(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0:
                return (i, j)  # row, col

    return None


# --- MAIN ---
print("\n-------- SUDOKU SOLVER -------- \n")

print("Reading the puzzle from the file...")
puzzle = readBoard("sudoku_puzzle.txt")
print("Puzzle read sucessfully! \n")

print("    ORIGINAL PUZZLE    ")
drawPuzzle(puzzle)
solvePuzzle(puzzle)
print("\n       SOLUTION       ")
drawPuzzle(puzzle)

print()
print("Writing solution into a file...")
writeSolution(puzzle)
print("Solution written successfully! \n")




