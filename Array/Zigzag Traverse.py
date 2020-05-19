# O(n) time | O(n) space
def zigzagTraverse(array):
	height = len(array) - 1
	width = len(array[0]) - 1
	row, col = 0, 0
	result = []
	goingDown = True
	while not isOutOfBounds(row, col, height, width):
		result.append(array[row][col])
		if goingDown:
			if row == height or col == 0:
				goingDown = False
				if row == height:
					col += 1
				else:
					row += 1
			else:
				row += 1
				col -= 1
		else:
			if row == 0 or col == width:
				goingDown = True
				if row == 0:
					col += 1
				else:
					row += 1
			else:
				row -= 1
				col += 1
	return result

def isOutOfBounds(row, col, height, width):
	return row < 0 or row > height or col < 0 or col > width
		

print(zigzagTraverse([[1,3,4,10], [2,5,9,11], [6,8,12,15], [7,13,14,16]]))