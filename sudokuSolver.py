def invalidProblem():
	print("Problem has no valid solution.")
	quit()

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

problem = readSudoku()
i, j = nextValue(problem, 6, 1)
print(i)
print(j)