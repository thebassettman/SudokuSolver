def readSudokuLine(lineStr):
	lineArr = []
	for element in range(9):
		lineArr.append(lineStr[element])
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