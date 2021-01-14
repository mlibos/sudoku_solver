import math
import numpy
import random
import time

class sudoku:
	#a sudoku objective contains information on difficulty, rows, columns, boxes
	def __init__(self,name,difficulty,rows,columns,boxes):
		self.name = name
		self.difficulty = difficulty
		self.rows = rows
		self.columns = columns
		self.boxes = boxes

	def get_box(self,n):
		#grabs the nth box counting from top left across and then down 
		return self.boxes[n]

	def get_row(self,n):
		#grabs the nth row counting from top down
		return self.rows[n]

	def get_column(self,n):
		#grabs the nth column countring from left to right
		return self.columns[n]

	def get_position(self,r,c):
		#given row and column position, returns a single spot in the sudoku
		return self.rows[r][c]

	def get_num_solved(self,objective):
		#given a row, column, or box returns the number of solved digits
		solved = 0
		for digit in objective:
			if digit != 0:
				solved +=1
		return solved

	def pretty_print(self):
		#prints sudoku
		print(self.difficulty,'Sudoku:',self.name)
		for row in self.rows:
			print(row)

def fill_in(sudoku):
	#given rows in a sudoku it fills columns and boxes
	columns = []
	for col in range(9):
		columns.append([0,0,0,0,0,0,0,0,0])
	boxes = []
	for box in range(9):
		boxes.append([0,0,0,0,0,0,0,0,0])
	for y in range(9):
		row = sudoku.get_row(y)
		for x,num in enumerate(row):
			columns[x][y] = num
	i = 0
	j = 0
	for box in range(9):
		n = 0
		for y in range(j,(j+3)):
			for x in range(i,(i+3)):
				boxes[box][n] = sudoku.get_position(y,x)
				n += 1
		i += 3
		if i == 9:
			i = 0
			j += 3
	sudoku.columns = columns
	sudoku.boxes = boxes
	return sudoku		


def check_valid(sudoku,r,c,digit):
	#given a position and a digit in a sudoku checks if placement there is valid, assumes the position contains a 0
	for num in sudoku.get_row(r):
		if num == digit:
			return False
	for num in sudoku.get_column(c):
		if num == digit:
			return False
	if r <= 2:
		if c <= 2:
			box = 0
		elif c <= 5:
			box = 1
		else:
			box = 2
	elif r <= 5:
		if c <= 2:
			box = 3
		elif c <= 5:
			box = 4
		else:
			box = 5		
	else:
		if c <= 2:
			box = 6
		elif c <= 5:
			box = 7
		else:
			box = 8
	for num in sudoku.get_box(box):
		if num == digit:
			return False
	return True


def empty_cell(sudoku):
	#returns an empty cell if one is available, otherwise returns -1,-1
	for r in range(9):
		for c in range(9):
			if sudoku.rows[r][c] == 0:
				return r,c
	return -1,-1


def sudoku_solver(sudoku):
	#takes a sudoku object and solves it using incremental backtracking
	x,y = empty_cell(sudoku)
	if x == -1:
		return True
	#try to place
	for digit in range(1,10):
		if check_valid(sudoku,x,y,digit):

			sudoku.rows[x][y] = digit
			if sudoku_solver(sudoku):
				return True
			sudoku.rows[x][y] = 0
	return False


#manually entered the rows of this easy sudoku, will later have an image processor which can read a sudoku from an image
s1 = sudoku('s1','Easy',[[2,6,3,0,7,1,0,0,5],[0,0,0,0,0,0,9,0,0],[9,1,4,3,0,0,0,0,7],[0,7,0,0,0,0,0,0,0],[5,0,0,0,0,4,0,0,0],[3,0,1,0,0,0,0,9,0],[4,0,0,0,6,0,8,5,0],[0,0,0,8,4,0,0,0,1],[0,5,0,0,0,7,0,6,0]],[],[])
s2 = sudoku('s2','Medium',[[0,0,1,0,0,2,0,0,0],[0,0,0,8,4,0,0,5,0],[0,8,0,0,0,0,0,1,0],[0,6,0,0,0,8,0,0,0],[0,0,7,6,0,0,3,0,0],[0,1,0,9,0,0,0,0,7],[0,2,5,0,0,0,0,8,0],[7,0,0,0,0,4,2,0,0],[0,0,0,0,3,0,0,0,0]],[],[])
s3 = sudoku('s3','Hard',[[9,0,0,0,0,0,0,3,0],[0,0,6,1,0,0,0,0,4],[7,8,2,0,0,6,0,1,0],[0,0,1,0,0,0,3,4,0],[0,0,0,0,7,0,5,8,0],[0,0,0,2,0,0,0,0,0],[8,0,9,0,3,2,0,0,0],[0,0,0,4,0,0,0,0,0],[0,0,0,5,0,0,0,0,0]],[],[])

# s4 = sudoku('s4','Hardest',[[0,0,5,3,0,0,0,0,0],[8,0,0,0,0,0,0,2,0],[0,7,0,0,1,0,5,0,0],[4,0,0,0,0,5,3,0,0],[0,1,0,0,7,0,0,0,6],[0,0,3,2,0,0,0,8,0],[0,6,0,5,0,0,0,0,9],[0,0,4,0,0,0,0,3,0],[0,0,0,0,0,9,7,0,0]],[],[])

# s5 = sudoku('s5','Extreme',[[1,0,0,0,0,7,0,9,0],[0,3,0,0,2,0,0,0,8],[0,0,9,6,0,0,5,0,0],[0,0,5,3,0,0,9,0,0],[0,1,0,0,8,0,0,0,2],[6,0,0,0,0,4,0,0,0],[3,0,0,0,0,0,0,1,0],[0,4,0,0,0,0,0,0,7],[0,0,7,0,0,0,3,0,0]],[],[])
# s6  = sudoku('s6','Blank',[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],[],[])

start = time.time()
fill_in(s1)
sudoku.pretty_print(s1)
sudoku_solver(s1)
sudoku.pretty_print(s1)
end = time.time()
print(end-start)


start = time.time()
fill_in(s2)
sudoku.pretty_print(s2)
sudoku_solver(s2)
sudoku.pretty_print(s2)
end = time.time()
print(end-start)

start = time.time()
fill_in(s3)
sudoku.pretty_print(s3)
sudoku_solver(s3)
sudoku.pretty_print(s3)
end = time.time()
print(end-start)

# start = time.time()
# fill_in(s4)
# sudoku.pretty_print(s4)
# sudoku_solver(s4)
# sudoku.pretty_print(s4)
# end = time.time()
# print(end-start)

# start = time.time()
# fill_in(s5)
# sudoku.pretty_print(s5)
# sudoku_solver(s5)
# sudoku.pretty_print(s5)
# end = time.time()
# print(end-start)

# start = time.time()
# fill_in(s6)
# sudoku.pretty_print(s6)
# sudoku_solver(s6)
# sudoku.pretty_print(s6)
# end = time.time()
# print(end-start)

