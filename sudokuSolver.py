def invalidProblem():
	print("Problem has no valid solution.")
	quit()

def prevValue(problem, i, j):
	found = False;
	while(not found):
		if(j == 0):
			i -= 1
			j = 8
			if(i < 0):
				invalidProblem()
		else:
			j -= 1

		if(not problem[i][j][1]):
			found = True;

	return i, j

def nextValue(problem, i, j):
	found = False;
	while(not found):
		if(j == 8):
			i += 1
			j = 0
		else:
			j += 1

		if(i == 9 or not problem[i][j][1]):
			found = True;

	return i, j

def readSudokuLine(lineStr):
	lineArr = []
	for element in range(9):
		if (lineStr[element] == 'x'):
			lineArr.append([0, False])
		else:
			lineArr.append([ord(lineStr[element]) - 48, True])
	return lineArr

def readSudoku():
	problem = []
	problemFile = open("problemFile.txt")

	for x in range(9):
		problemLine = problemFile.readline()
		problemLineArr = readSudokuLine(problemLine)
		problem.append(problemLineArr)
	return problem

def validEntry(problem, i, j, entry):
	for m in range(9):
		if(problem[i][m][0] == entry):
			return False
	for n in range(9):
		if(problem[n][j][0] == entry):
			return False
	
	if(i >= 0 and i <= 2):
		x = 0
	if(i >= 3 and i <= 5):
		x = 3
	if(i >= 6 and i <= 9):
		x = 6
	if(j >= 0 and j <= 2):
		y = 0
	if(j >= 3 and j <= 5):
		y = 3
	if(j >= 6 and j <= 9):
		y = 6

	for a in range(x, x + 3):
		for b in range(y, y + 3):
			if(problem[a][b][0] == entry):
				return False

	return True

def toString(problem):
	output = ""
	for i in range(9):
		for j in range(9):
			if(problem[i][j][0] == 0):
				output += "x"
			else:
				output += str(problem[i][j][0])
		output += "\n"
	print(output)

def solve(problem):
	i, j = nextValue(problem, -1, 8)

	found = False

	while(not found):
		for entry in range(problem[i][j][0] + 1, 11):
			if(validEntry(problem, i, j, entry)):
				problem[i][j][0] = entry
				break

		if(problem[i][j][0] == 10):
			problem[i][j][0] = 0
			i, j = prevValue(problem, i, j)
			continue

		if(problem[8][8][0] != 0):
			print("Solution found!")
			toString(problem)
			found = True

		i, j = nextValue(problem, i, j)

problem = readSudoku()

solve(problem)