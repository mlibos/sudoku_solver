import math
import numpy
import random


class sudoku:
	def __init__(self,difficulty,rows,columns,boxes):
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

s1 = sudoku('Easy',[[2,6,3,0,7,1,0,0,5],[0,0,0,0,0,0,9,0,0],[9,1,4,3,0,0,0,0,7],[0,7,0,0,0,0,0,0,0],[5,0,0,0,0,4,0,0,0],[3,0,1,0,0,0,0,9,0],[4,0,0,0,6,0,8,5,0],[0,0,0,8,4,0,0,0,1],[0,5,0,0,0,7,0,6,0]],[],[])
def fill_in(sudoku):
	#given rows in a sudoku it returns columns and boxes
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
	
fill_in(s1)


def sudoku_solver(sudoku):
	#takes a sudoku object and solves it
	pass