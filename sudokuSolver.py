def readSudokuLine(lineStr):
	lineArr = []
	for element in range(9):
		if (lineStr[element] == 'x'):
			lineArr.append([0, false])
		else:
			lineArr.append([lineStr[element], true])
	return lineArr

def readSudoku():
	problem = []
	problemFile = open("problemFile.txt")

	for x in range(9):
		problemLine = problemFile.readline()
		problemLineArr = readSudokuLine(problemLine)
		problem.append(problemLineArr)

	print(problem)

readSudoku()