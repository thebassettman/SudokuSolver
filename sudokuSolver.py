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
			if(i > 8):
				invalidProblem()
		else:
			j += 1

		if(not problem[i][j][1]):
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

	print(problem)
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

problem = readSudoku()

print(validEntry(problem, 0, 0, 2))
print(validEntry(problem, 0, 0, 1))
print(validEntry(problem, 0, 1, 7))