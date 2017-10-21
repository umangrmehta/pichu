#!/usr/bin/env python3
# Authors: Umang Mehta, Samanvitha Pradhan & Vaishnavi Srinivasan

import copy
import math


def findPos(board, charToBeFound):
	return [(row, col) for col in range(0, 8, 1) for row in range(0, 8, 1) if board[row][col] == charToBeFound]


def updatePos(board, xPos1, yPos1, xPos2, yPos2, charToReplace, message):
	tempState = copy.deepcopy(board)
	tempState[xPos1][yPos1] = '.'
	tempState[xPos2][yPos2] = charToReplace
	# https://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python
	flatList = [col for row in tempState for col in row]
	flatListString="".join([ row for row in inputBoard ])
	hueristic=evaluation(flatList)
	succDict.setdefault(hueristic,[])
	succDict[hueristic].append(flatListString)
	#succDict[evaluation(flatList)] = flatList
	movesDict.setdefault(flatListString,[])
	movesDict[flatListString].append(message)
	#movesDict[flatListString] = message
	return flatList


def evaluation(board):
	whiteCount = 0
	blackCount = 0
	whiteCount = (whiteCount + board.count('P'))*1
	whiteCount = (whiteCount + board.count('R'))*7
	whiteCount = (whiteCount + board.count('B'))*float(3.5)
	whiteCount = (whiteCount + board.count('N'))*4
	whiteCount = (whiteCount + board.count('Q'))*float(13.5)
	blackCount = (blackCount + board.count('p'))*1
	blackCount = (blackCount + board.count('r'))*7
	blackCount = (blackCount + board.count('b'))*float(3.5)
	blackCount = (blackCount + board.count('n'))*4
	blackCount = (blackCount + board.count('q'))*float(13.5)
	if player == 'w':
		if ('K' in board) and not ('k' in board) :
			turnCount=55
		elif ('k' in board) and not ('K' in board) :
			turnCount=-55
		else :
			turnCount = blackCount - whiteCount
	if player == 'b':
		if ('k' in board) and not ('K' in board) :
			turnCount=55
		elif ('K' in board) and not ('k' in board) :
			turnCount=-55
		else :
			turnCount = whiteCount - blackCount
	return turnCount


def is_terminal(board):
	# TODO: Check if the Board State is a Terminal State
	if "K" in board and "k" in board:
		return False
	return True


def successors(board):
	# https://stackoverflow.com/questions/6614891/turning-a-list-into-nested-lists-in-python
	currentState = [board[i:i + 8] for i in range(0, len(board), 8)]
	successor = [[]]
	successor = [row for row in successor if row != []]
	if player == 'w':
		# each successor for pawn
		pawnPos = findPos(currentState, 'P')
		for possiblePositions in range(0, len(pawnPos), 1):
			rowCounter = pawnPos[possiblePositions][0]
			colCounter = pawnPos[possiblePositions][1]
			# move pawn down
			if (rowCounter + 1) <= 7:
				if (currentState[rowCounter + 1][colCounter].islower()) or currentState[rowCounter + 1][colCounter] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + 1, colCounter, 'P','Pawn at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1+1)+' column '+(colCounter+1)))
			if rowCounter == 1:
				if currentState[rowCounter + 1][colCounter] == '.' and currentState[rowCounter + 2][colCounter] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + 2, colCounter, 'P','Pawn at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+2+1)+' column '+(colCounter+1)))
			# move pawn left
			if (colCounter - 1) >= 0:
				if (currentState[rowCounter][colCounter - 1].islower()) or currentState[rowCounter][colCounter - 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, colCounter - 1, 'P','Pawn at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(colCounter-1+1)))
			# move pawn right
			if (colCounter + 1) <= 7:
				if (currentState[rowCounter][colCounter + 1].islower()) or currentState[rowCounter][colCounter + 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, colCounter + 1, 'P','Pawn at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(colCounter+1+1)))
			# move pawn left diagonally
			if (colCounter - 1) >= 0 and (rowCounter + 1) <= 7:
				if (currentState[rowCounter + 1][colCounter - 1].islower()):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + 1, colCounter - 1, 'P','Pawn at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1+1)+' column '+(colCounter-1+1)))
			# move pawn right diagonally
			if (colCounter + 1) <= 7 and (rowCounter + 1) <= 7:
				if (currentState[rowCounter + 1][colCounter + 1].islower()):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + 1, colCounter + 1, 'P','Pawn at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1+1)+' column '+(colCounter+1+1)))
		# each successor for rook
		rookPos = findPos(currentState, 'R')
		for possiblePositions in range(0, len(rookPos), 1):
			rowCounter = rookPos[possiblePositions][0]
			colCounter = rookPos[possiblePositions][1]
			# move rook up
			for i in range(rowCounter - 1, -1, -1):
				if (currentState[i][colCounter].isupper()):
					break
				elif (currentState[i][colCounter].islower()):
					successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, 'R','Rook at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(i+1)+' column '+(colCounter+1)))
					break
				elif currentState[i][colCounter] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, 'R','Rook at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(i+1)+' column '+(colCounter+1)))
				else:
					pass
			# move rook down
			for i in range(rowCounter + 1, 8, 1):
				if (currentState[i][colCounter].isupper()):
					break
				elif (currentState[i][colCounter].islower()):
					successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, 'R','Rook at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(i+1)+' column '+(colCounter+1)))
					break
				elif currentState[i][colCounter] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, 'R','Rook at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(i+1)+' column '+(colCounter+1)))
				else:
					pass
			# move rook left
			for i in range(colCounter - 1, -1, -1):
				if (currentState[rowCounter][i].isupper()):
					break
				elif (currentState[rowCounter][i].islower()):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, 'R','Rook at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(i+1)))
					break
				elif currentState[rowCounter][i] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, 'R','Rook at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(i+1)))
				else:
					pass
			# move rook right
			for i in range(colCounter + 1, 8, 1):
				if (currentState[rowCounter][i].isupper()):
					break
				elif (currentState[rowCounter][i].islower()):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, 'R','Rook at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(i+1)))
					break
				elif currentState[rowCounter][i] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, 'R','Rook at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(i+1)))
				else:
					pass
		# each successor for bishop
		bishopPos = findPos(currentState, 'B')
		for possiblePositions in range(0, len(bishopPos), 1):
			rowCounter = bishopPos[possiblePositions][0]
			colCounter = bishopPos[possiblePositions][1]
			# move bishop to the left
			for r in range(rowCounter, -1, -1):
				if ((rowCounter - r) >= 0 and (colCounter - r) >= 0):
					if (currentState[rowCounter - r][colCounter - r].isupper()):
						break
					elif (currentState[rowCounter - r][colCounter - r].islower()):
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - r, colCounter - r, 'B','Bishop at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-r+1)+' column '+(colCounter-r+1)))
						break
					elif currentState[rowCounter - r][colCounter - r] == '.':
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - r, colCounter - r, 'B','Bishop at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-r+1)+' column '+(colCounter-r+1)))
					else:
						pass
			i = 1
			for r in range(rowCounter, 8, 1):
				if ((rowCounter + i) < 8 and (colCounter + i) < 8):
					if (currentState[rowCounter + i][colCounter + i].isupper()):
						break
					elif (currentState[rowCounter + i][colCounter + i].islower()):
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + i, colCounter + i, 'B','Bishop at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+i+1)+' column '+(colCounter+i+1)))
						break
					elif currentState[rowCounter + i][colCounter + i] == '.':
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + i, colCounter + i, 'B','Bishop at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+i+1)+' column '+(colCounter+i+1)))
					else:
						pass
					i += 1
			i = 0
			# move bishop to the right
			for r in range(rowCounter, -1, -1):
				if ((rowCounter - i) >= 0 and (colCounter + i) < 8):
					if (currentState[rowCounter - i][colCounter + i].isupper()):
						break
					elif (currentState[rowCounter - i][colCounter + i].islower()):
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - i, colCounter + i, 'B','Bishop at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-i+1)+' column '+(colCounter+i+1)))
						break
					elif currentState[rowCounter - i][colCounter + i] == '.':
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - i, colCounter + i, 'B','Bishop at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-i+1)+' column '+(colCounter+i+1)))
					else:
						pass
					i += 1
			i = 1
			for r in range(rowCounter, 8, 1):
				if ((rowCounter + i) < 8 and (colCounter - i) >= 0):
					if (currentState[rowCounter + i][colCounter - i].isupper()):
						break
					elif (currentState[rowCounter + i][colCounter - i].islower()):
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + i, colCounter - i, 'B','Bishop at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+i+1)+' column '+(colCounter-i+1)))
						break
					elif currentState[rowCounter + i][colCounter - i] == '.':
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + i, colCounter - i, 'B','Bishop at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+i+1)+' column '+(colCounter-i+1)))
					else:
						pass
					i += 1
		# each successor for queen
		queenPos = findPos(currentState, 'Q')
		for possiblePositions in range(0, len(queenPos), 1):
			rowCounter = queenPos[possiblePositions][0]
			colCounter = queenPos[possiblePositions][1]
			# move queen to the left
			for r in range(rowCounter, -1, -1):
				if ((rowCounter - r) >= 0 and (colCounter - r) >= 0):
					if (currentState[rowCounter - r][colCounter - r].isupper()):
						break
					elif (currentState[rowCounter - r][colCounter - r].islower()):
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - r, colCounter - r, 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-r+1)+' column '+(colCounter-r+1)))
						break
					elif currentState[rowCounter - r][colCounter - r] == '.':
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - r, colCounter - r, 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-r+1)+' column '+(colCounter-r+1)))
					else:
						pass
			i = 1
			for r in range(rowCounter, 8, 1):
				if ((rowCounter + i) < 8 and (colCounter + i) < 8):
					if (currentState[rowCounter + i][colCounter + i].isupper()):
						break
					elif (currentState[rowCounter + i][colCounter + i].islower()):
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + i, colCounter + i, 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+i+1)+' column '+(colCounter+i+1)))
						break
					elif currentState[rowCounter + i][colCounter + i] == '.':
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + i, colCounter + i, 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+i+1)+' column '+(colCounter+i+1)))
					else:
						pass
					i += 1
			i = 0
			# move queen to the right
			for r in range(rowCounter, -1, -1):
				if ((rowCounter - i) >= 0 and (colCounter + i) < 8):
					if (currentState[rowCounter - i][colCounter + i].isupper()):
						break
					elif (currentState[rowCounter - i][colCounter + i].islower()):
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - i, colCounter + i, 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-i+1)+' column '+(colCounter+i+1)))
						break
					elif currentState[rowCounter - i][colCounter + i] == '.':
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - i, colCounter + i, 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-i+1)+' column '+(colCounter+i+1)))
					else:
						pass
					i += 1
			i = 1
			for r in range(rowCounter, 8, 1):
				if ((rowCounter + i) < 8 and (colCounter - i) >= 0):
					if (currentState[rowCounter + i][colCounter - i].isupper()):
						break
					elif (currentState[rowCounter + i][colCounter - i].islower()):
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + i, colCounter - i, 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+i+1)+' column '+(colCounter-i+1)))
						break
					elif currentState[rowCounter + i][colCounter - i] == '.':
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + i, colCounter - i, 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+i+1)+' column '+(colCounter-i+1)))
					else:
						pass
					i += 1
			# move queen up
			for i in range(rowCounter - 1, -1, -1):
				if (currentState[i][colCounter].isupper()):
					break
				elif (currentState[i][colCounter].islower()):
					successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(i+1)+' column '+(colCounter+1)))
					break
				elif currentState[i][colCounter] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(i+1)+' column '+(colCounter+1)))
				else:
					pass
			# move queen down
			for i in range(rowCounter + 1, 8, 1):
				if (currentState[i][colCounter].isupper()):
					break
				elif (currentState[i][colCounter].islower()):
					successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(i+1)+' column '+(colCounter+1)))
					break
				elif currentState[i][colCounter] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(i+1)+' column '+(colCounter+1)))
				else:
					pass
			# move queen left
			for i in range(colCounter - 1, -1, -1):
				if (currentState[rowCounter][i].isupper()):
					break
				elif (currentState[rowCounter][i].islower()):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(i+1)))
					break
				elif currentState[rowCounter][i] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(i+1)))
				else:
					pass
			# move queen right
			for i in range(colCounter + 1, 8, 1):
				if (currentState[rowCounter][i].isupper()):
					break
				elif (currentState[rowCounter][i].islower()):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(i+1)))
					break
				elif currentState[rowCounter][i] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(i+1)))
				else:
					pass
		# each successor for king
		kingPos = findPos(currentState, 'K')
		for possiblePositions in range(0, len(kingPos), 1):
			rowCounter = kingPos[possiblePositions][0]
			colCounter = kingPos[possiblePositions][1]
			# move king up
			if (rowCounter - 1) >= 0:
				if (currentState[rowCounter - 1][colCounter].islower()) or currentState[rowCounter - 1][colCounter] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - 1, colCounter, 'K','King at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-1+1)+' column '+(colCounter+1)))
			# move king down
			if (rowCounter + 1) <= 7:
				if (currentState[rowCounter + 1][colCounter].islower()) or currentState[rowCounter + 1][colCounter] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + 1, colCounter, 'K','King at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1+1)+' column '+(colCounter+1)))
			# move king left
			if (colCounter - 1) >= 0:
				if (currentState[rowCounter][colCounter - 1].islower()) or currentState[rowCounter][colCounter - 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, colCounter - 1, 'K','King at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(colCounter-1+1)))
			# move king right
			if (colCounter + 1) <= 7:
				if (currentState[rowCounter][colCounter + 1].islower()) or currentState[rowCounter][colCounter + 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, colCounter + 1, 'K','King at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(colCounter+1+1)))
			# move king left diagonally down
			if (rowCounter + 1) <= 7 and (colCounter - 1) >= 0:
				if (currentState[rowCounter + 1][colCounter - 1].islower()) or currentState[rowCounter + 1][colCounter - 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + 1, colCounter - 1, 'K','King at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-1+1)+' column '+(colCounter-1+1)))
			# move king right diagonally down
			if (rowCounter + 1) <= 7 and (colCounter + 1) <= 7:
				if (currentState[rowCounter + 1][colCounter + 1].islower()) or currentState[rowCounter + 1][colCounter + 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + 1, colCounter + 1, 'K','King at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1+1)+' column '+(colCounter+1+1)))
			# move king left diagonally up
			if (rowCounter - 1) >= 0 and (colCounter - 1) >= 0:
				if (currentState[rowCounter - 1][colCounter - 1].islower()) or currentState[rowCounter - 1][colCounter - 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - 1, colCounter - 1, 'K','King at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-1+1)+' column '+(colCounter-1+1)))
			# move king right diagonally up
			if (rowCounter - 1) >= 0 and (colCounter + 1) <= 7:
				if (currentState[rowCounter - 1][colCounter + 1].islower()) or currentState[rowCounter - 1][colCounter + 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - 1, colCounter + 1, 'K','King at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-1+1)+' column '+(colCounter+1+1)))
		# each successor for knight
		knightPos = findPos(currentState, 'N')
		for possiblePositions in range(0, len(knightPos), 1):
			rowCounter = knightPos[possiblePositions][0]
			colCounter = knightPos[possiblePositions][1]
			# move knight up right L
			if (rowCounter - 1) >= 0 and (colCounter + 2) <= 7:
				if (currentState[rowCounter - 1][colCounter + 2].islower()) or currentState[rowCounter - 1][colCounter + 2] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - 1, colCounter + 2, 'N','Knight at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-1+1)+' column '+(colCounter+1+2)))
			if (rowCounter - 2) >= 0 and (colCounter + 1) <= 7:
				if (currentState[rowCounter - 2][colCounter + 1].islower()) or currentState[rowCounter - 2][colCounter + 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - 2, colCounter + 1, 'N','Knight at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-2+1)+' column '+(colCounter+1+1)))
			# move knight up left L
			if (rowCounter - 1) >= 0 and (colCounter - 2) <= 7:
				if (currentState[rowCounter - 1][colCounter - 2].islower()) or currentState[rowCounter - 1][colCounter - 2] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - 1, colCounter - 2, 'N','Knight at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-1+1)+' column '+(colCounter+1-2)))
			if (rowCounter - 2) >= 0 and (colCounter + 1) <= 7:
				if (currentState[rowCounter - 2][colCounter - 1].islower()) or currentState[rowCounter - 2][colCounter - 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - 2, colCounter - 1, 'N','Knight at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-2+1)+' column '+(colCounter+1+1)))
			# move knight down left L
			if (rowCounter + 2) >= 0 and (colCounter + 1) <= 7:
				if (currentState[rowCounter + 2][colCounter + 1].islower()) or currentState[rowCounter + 2][colCounter + 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + 2, colCounter + 1, 'N','Knight at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+2+1)+' column '+(colCounter+1+1)))
			if (rowCounter + 1) >= 0 and (colCounter + 2) <= 7:
				if (currentState[rowCounter + 1][colCounter + 2].islower()) or currentState[rowCounter + 1][colCounter + 2] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + 1, colCounter + 2, 'N','Knight at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1+1)+' column '+(colCounter+1+2)))
			# move knight down left L
			if (rowCounter + 2) >= 0 and (colCounter - 1) <= 7:
				if (currentState[rowCounter + 2][colCounter - 1].islower()) or currentState[rowCounter + 2][colCounter - 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + 2, colCounter - 1, 'N','Knight at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+2+1)+' column '+(colCounter+1-1)))
			if (rowCounter + 1) >= 0 and (colCounter - 2) <= 7:
				if (currentState[rowCounter + 1][colCounter - 2].islower()) or currentState[rowCounter + 1][colCounter - 2] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + 1, colCounter - 2, 'N','Knight at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1+1)+' column '+(colCounter+1-2)))
	if player == 'b':
		# each successor for pawn
		pawnPos = findPos(currentState, 'p')
		for possiblePositions in range(0, len(pawnPos), 1):
			rowCounter = pawnPos[possiblePositions][0]
			colCounter = pawnPos[possiblePositions][1]
			# move pawn up
			if (rowCounter - i) >= 0:
				if (currentState[rowCounter - 1][colCounter].isupper()) or currentState[rowCounter - 1][colCounter] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - 1, colCounter, 'p', 'Pawn at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-1+1)+' column '+(colCounter+1)))
			if rowCounter == 6:
				if currentState[rowCounter - 1][colCounter] == '.' and currentState[rowCounter - 2][colCounter] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - 2, colCounter, 'p', 'Pawn at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-2+1)+' column '+(colCounter+1)))
			# move pawn left
			if (colCounter - 1) >= 0:
				if (currentState[rowCounter][colCounter - 1].isupper()) or currentState[rowCounter][colCounter - 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, colCounter - 1, 'p', 'Pawn at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(colCounter-1+1)))
			# move pawn right
			if (colCounter + 1) <= 7:
				if (currentState[rowCounter][colCounter + 1].isupper()) or currentState[rowCounter][colCounter + 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, colCounter + 1, 'p', 'Pawn at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(colCounter+1+1)))
			# move pawn left diagonally
			if (colCounter - 1) >= 0 and (rowCounter - 1) >= 0:
				if (currentState[rowCounter - 1][colCounter - 1].isupper()):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - 1, colCounter - 1, 'p', 'Pawn at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-1+1)+' column '+(colCounter-1+1)))
			# move pawn right diagonally
			if (colCounter + 1) <= 7 and (rowCounter - 1) >= 0:
				if (currentState[rowCounter - 1][colCounter + 1].isupper()):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - 1, colCounter + 1, 'p', 'Pawn at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-1+1)+' column '+(colCounter+1+1)))
		# each successor for rook
		rookPos = findPos(currentState, 'r')
		for possiblePositions in range(0, len(rookPos), 1):
			rowCounter = rookPos[possiblePositions][0]
			colCounter = rookPos[possiblePositions][1]
			# move rook up
			for i in range(rowCounter - 1, -1, -1):
				if (currentState[i][colCounter].islower()):
					break
				elif (currentState[i][colCounter].isupper()):
					successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, 'r','Rook at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(i+1)+' column '+(colCounter+1)))
					break
				elif currentState[i][colCounter] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, 'r','Rook at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(i+1)+' column '+(colCounter+1)))
				else:
					pass
			# move rook down
			for i in range(rowCounter + 1, 8, 1):
				if (currentState[i][colCounter].islower()):
					break
				elif (currentState[i][colCounter].isupper()):
					successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, 'r','Rook at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(i+1)+' column '+(colCounter+1)))
					break
				elif currentState[i][colCounter] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, 'r','Rook at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(i+1)+' column '+(colCounter+1)))
				else:
					pass
			# move rook left
			for i in range(colCounter - 1, -1, -1):
				if (currentState[rowCounter][i].islower()):
					break
				elif (currentState[rowCounter][i].isupper()):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, 'r','Rook at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(i+1)))
					break
				elif currentState[rowCounter][i] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, 'r','Rook at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(i+1)))
				else:
					pass
			# move rook right
			for i in range(colCounter + 1, 8, 1):
				if (currentState[rowCounter][i].islower()):
					break
				elif (currentState[rowCounter][i].isupper()):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, 'r','Rook at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(i+1)))
					break
				elif currentState[rowCounter][i] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, 'r','Rook at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(i+1)))
				else:
					pass
		# each successor for bishop
		bishopPos = findPos(currentState, 'b')
		for possiblePositions in range(0, len(bishopPos), 1):
			rowCounter = bishopPos[possiblePositions][0]
			colCounter = bishopPos[possiblePositions][1]
			# move bishop to the left
			for r in range(rowCounter, -1, -1):
				if ((rowCounter - r) >= 0 and (colCounter - r) >= 0):
					if (currentState[rowCounter - r][colCounter - r].islower()):
						break
					elif (currentState[rowCounter - r][colCounter - r].isupper()):
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - r, colCounter - r, 'b','Bishop at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-r+1)+' column '+(colCounter-r+1)))
						break
					elif currentState[rowCounter - r][colCounter - r] == '.':
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - r, colCounter - r, 'b','Bishop at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-r+1)+' column '+(colCounter-r+1)))
					else:
						pass
			i = 1
			for r in range(rowCounter, 8, 1):
				if ((rowCounter + i) < 8 and (colCounter + i) < 8):
					if (currentState[rowCounter + i][colCounter + i].islower()):
						break
					elif (currentState[rowCounter + i][colCounter + i].isupper()):
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + i, colCounter + i, 'b','Bishop at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+i+1)+' column '+(colCounter+i+1)))
						break
					elif currentState[rowCounter + i][colCounter + i] == '.':
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + i, colCounter + i, 'b','Bishop at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+i+1)+' column '+(colCounter+i+1)))
					else:
						pass
					i += 1
			i = 0
			# move bishop to the right
			for r in range(rowCounter, -1, -1):
				if ((rowCounter - i) >= 0 and (colCounter + i) < 8):
					if (currentState[rowCounter - i][colCounter + i].islower()):
						break
					elif (currentState[rowCounter - i][colCounter + i].isupper()):
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - i, colCounter + i, 'b','Bishop at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-i+1)+' column '+(colCounter+i+1)))
						break
					elif currentState[rowCounter - i][colCounter + i] == '.':
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - i, colCounter + i, 'b','Bishop at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-i+1)+' column '+(colCounter+i+1)))
					else:
						pass
					i += 1
			i = 1
			for r in range(rowCounter, 8, 1):
				if ((rowCounter + i) < 8 and (colCounter - i) >= 0):
					if (currentState[rowCounter + i][colCounter - i].islower()):
						break
					elif (currentState[rowCounter + i][colCounter - i].isupper()):
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + i, colCounter - i, 'b','Bishop at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+i+1)+' column '+(colCounter-i+1)))
						break
					elif currentState[rowCounter + i][colCounter - i] == '.':
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + i, colCounter - i, 'b','Bishop at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+i+1)+' column '+(colCounter-i+1)))
					else:
						pass
					i += 1
		# each successor for queen
		queenPos = findPos(currentState, 'q')
		for possiblePositions in range(0, len(queenPos), 1):
			rowCounter = queenPos[possiblePositions][0]
			colCounter = queenPos[possiblePositions][1]
			# move queen to the left
			for r in range(rowCounter, -1, -1):
				if ((rowCounter - r) >= 0 and (colCounter - r) >= 0):
					if (currentState[rowCounter - r][colCounter - r].islower()):
						break
					elif (currentState[rowCounter - r][colCounter - r].isupper()):
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - r, colCounter - r, 'q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-r+1)+' column '+(colCounter-r+1)))
						break
					elif currentState[rowCounter - r][colCounter - r] == '.':
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - r, colCounter - r, 'q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-r+1)+' column '+(colCounter-r+1)))
					else:
						pass
			i = 1
			for r in range(rowCounter, 8, 1):
				if ((rowCounter + i) < 8 and (colCounter + i) < 8):
					if (currentState[rowCounter + i][colCounter + i].islower()):
						break
					elif (currentState[rowCounter + i][colCounter + i].isupper()):
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + i, colCounter + i, 'q', 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+i+1)+' column '+(colCounter+i+1)))
						break
					elif currentState[rowCounter + i][colCounter + i] == '.':
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + i, colCounter + i, 'q', 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+i+1)+' column '+(colCounter+i+1)))
					else:
						pass
					i += 1
			i = 0
			# move queen to the right
			for r in range(rowCounter, -1, -1):
				if ((rowCounter - i) >= 0 and (colCounter + i) < 8):
					if (currentState[rowCounter - i][colCounter + i].islower()):
						break
					elif (currentState[rowCounter - i][colCounter + i].isupper()):
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - i, colCounter + i, 'q', 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-i+1)+' column '+(colCounter+i+1)))
						break
					elif currentState[rowCounter - i][colCounter + i] == '.':
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - i, colCounter + i, 'q', 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-i+1)+' column '+(colCounter+i+1)))
					else:
						pass
					i += 1
			i = 1
			for r in range(rowCounter, 8, 1):
				if ((rowCounter + i) < 8 and (colCounter - i) >= 0):
					if (currentState[rowCounter + i][colCounter - i].islower()):
						break
					elif (currentState[rowCounter + i][colCounter - i].isupper()):
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + i, colCounter - i, 'q', 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+i+1)+' column '+(colCounter-i+1)))
						break
					elif currentState[rowCounter + i][colCounter - i] == '.':
						successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + i, colCounter - i, 'q', 'Q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+i+1)+' column '+(colCounter-i+1)))
					else:
						pass
					i += 1
			# move queen up
			for i in range(rowCounter - 1, -1, -1):
				if (currentState[i][colCounter].islower()):
					break
				elif (currentState[i][colCounter].isupper()):
					successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, 'q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(i+1)+' column '+(colCounter+1)))
					break
				elif currentState[i][colCounter] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, 'q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(i+1)+' column '+(colCounter+1)))
				else:
					pass
			# move queen down
			for i in range(rowCounter + 1, 8, 1):
				if (currentState[i][colCounter].islower()):
					break
				elif (currentState[i][colCounter].isupper()):
					successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, 'q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(i+1)+' column '+(colCounter+1)))
					break
				elif currentState[i][colCounter] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, 'q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(i+1)+' column '+(colCounter+1)))
				else:
					pass
			# move queen left
			for i in range(colCounter - 1, -1, -1):
				if (currentState[rowCounter][i].islower()):
					break
				elif (currentState[rowCounter][i].isupper()):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, 'q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(i+1)))
					break
				elif currentState[rowCounter][i] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, 'q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(i+1)))
				else:
					pass
			# move queen right
			for i in range(colCounter + 1, 8, 1):
				if (currentState[rowCounter][i].islower()):
					break
				elif (currentState[rowCounter][i].isupper()):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, 'q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(i+1)))
					break
				elif currentState[rowCounter][i] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, 'q','Queen at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(i+1)))
				else:
					pass
		# each successor for king
		kingPos = findPos(currentState, 'k')
		for possiblePositions in range(0, len(kingPos), 1):
			rowCounter = kingPos[possiblePositions][0]
			colCounter = kingPos[possiblePositions][1]
			# move king up
			if (rowCounter - 1) >= 0:
				if (currentState[rowCounter - 1][colCounter].isupper()) or currentState[rowCounter - 1][colCounter] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - 1, colCounter, 'k','King at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-1+1)+' column '+(colCounter+1)))
			# move king down
			if (rowCounter + 1) <= 7:
				if (currentState[rowCounter + 1][colCounter].isupper()) or currentState[rowCounter + 1][colCounter] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + 1, colCounter, 'k','King at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1+1)+' column '+(colCounter+1)))
			# move king left
			if (colCounter - 1) >= 0:
				if (currentState[rowCounter][colCounter - 1].isupper()) or currentState[rowCounter][colCounter - 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, colCounter - 1, 'k','King at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(colCounter+1-1)))
			# move king right
			if (colCounter + 1) <= 7:
				if (currentState[rowCounter][colCounter + 1].isupper()) or currentState[rowCounter][colCounter + 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, colCounter + 1, 'k','King at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1)+' column '+(colCounter+1+1)))
			# move king left diagonally down
			if (rowCounter + 1) <= 7 and (colCounter - 1) >= 0:
				if (currentState[rowCounter + 1][colCounter - 1].isupper()) or currentState[rowCounter + 1][colCounter - 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + 1, colCounter - 1, 'k','King at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1+1)+' column '+(colCounter+1-1)))
			# move king right diagonally down
			if (rowCounter + 1) <= 7 and (colCounter + 1) <= 7:
				if (currentState[rowCounter + 1][colCounter + 1].isupper()) or currentState[rowCounter + 1][colCounter + 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + 1, colCounter + 1, 'k','King at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1+1)+' column '+(colCounter+1+1)))
			# move king left diagonally up
			if (rowCounter - 1) >= 0 and (colCounter - 1) >= 0:
				if (currentState[rowCounter - 1][colCounter - 1].isupper()) or currentState[rowCounter - 1][colCounter - 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - 1, colCounter - 1, 'k','King at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-1+1)+' column '+(colCounter-1+1)))
			# move king right diagonally up
			if (rowCounter - 1) >= 0 and (colCounter + 1) <= 7:
				if (currentState[rowCounter - 1][colCounter + 1].isupper()) or currentState[rowCounter - 1][colCounter + 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - 1, colCounter + 1, 'k','King at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-1+1)+' column '+(colCounter+1+1)))
		# each successor for knight
		knightPos = findPos(currentState, 'n')
		for possiblePositions in range(0, len(knightPos), 1):
			rowCounter = knightPos[possiblePositions][0]
			colCounter = knightPos[possiblePositions][1]
			# move knight up right L
			if (rowCounter - 1) >= 0 and (colCounter + 2) <= 7:
				if (currentState[rowCounter - 1][colCounter + 2].isupper()) or currentState[rowCounter - 1][colCounter + 2] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - 1, colCounter + 2, 'n','Knight at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-1+1)+' column '+(colCounter+1+2)))
			if (rowCounter - 2) >= 0 and (colCounter + 1) <= 7:
				if (currentState[rowCounter - 2][colCounter + 1].isupper()) or currentState[rowCounter - 2][colCounter + 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - 2, colCounter + 1, 'n','Knight at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-2+1)+' column '+(colCounter+1+1)))
			# move knight up left L
			if (rowCounter - 1) >= 0 and (colCounter - 2) <= 7:
				if (currentState[rowCounter - 1][colCounter - 2].isupper()) or currentState[rowCounter - 1][colCounter - 2] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - 1, colCounter - 2, 'n','Knight at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-1+1)+' column '+(colCounter+1-2)))
			if (rowCounter - 2) >= 0 and (colCounter + 1) <= 7:
				if (currentState[rowCounter - 2][colCounter - 1].isupper()) or currentState[rowCounter - 2][colCounter - 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter - 2, colCounter - 1, 'n','Knight at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter-2+1)+' column '+(colCounter+1+1)))
			# move knight down left L
			if (rowCounter + 2) >= 0 and (colCounter + 1) <= 7:
				if (currentState[rowCounter + 2][colCounter + 1].isupper()) or currentState[rowCounter + 2][colCounter + 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + 2, colCounter + 1, 'n','Knight at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+2+1)+' column '+(colCounter+1+1)))
			if (rowCounter + 1) >= 0 and (colCounter + 2) <= 7:
				if (currentState[rowCounter + 1][colCounter + 2].isupper()) or currentState[rowCounter + 1][colCounter + 2] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + 1, colCounter + 2, 'n','Knight at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1+1)+' column '+(colCounter+1+2)))
			# move knight down left L
			if (rowCounter + 2) >= 0 and (colCounter - 1) <= 7:
				if (currentState[rowCounter + 2][colCounter - 1].isupper()) or currentState[rowCounter + 2][colCounter - 1] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + 2, colCounter - 1, 'n','Knight at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+2+1)+' column '+(colCounter+1-1)))
			if (rowCounter + 1) >= 0 and (colCounter - 2) <= 7:
				if (currentState[rowCounter + 1][colCounter - 2].isupper()) or currentState[rowCounter + 1][colCounter - 2] == '.':
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter + 1, colCounter - 2, 'n','Knight at row '+(rowCounter+1)+' column '+(colCounter+1)+' to row '+(rowCounter+1+1)+' column '+(colCounter+1-2)))


# TODO: Minimax with Alpha-Beta Pruning
def decision():
	return max(successors(inputBoard), key=lambda successor: min_value(successor, -math.inf, math.inf, 1))


def max_value(board, alpha, beta, level):
	if is_terminal(board) or level == horizon:
		return evaluation(board)
	else:
		for successor in successors(board):
			value = min_value(successor, alpha, beta, level + 1)
			if value > alpha:
				alpha = value
			if alpha >= beta:
				return alpha
		return alpha


def min_value(board, alpha, beta, level):
	if is_terminal(board) or level == horizon:
		return evaluation(board)
	else:
		for successor in successors(board):
			value = max_value(successor, alpha, beta, level + 1)
			if value < beta:
				beta = value
			if alpha >= beta:
				return beta
		return beta


inputBoard = []
initialPosition = "RNBQKBNRPPPPPPPP................................pppppppprnbqkbnr"
player = 'w'
# player = 'b'
for counter in range(0, len(initialPosition), 1):
	inputBoard.append(initialPosition[counter])

# currentState = [inputBoard[i:i + 8] for i in range(0, len(inputBoard), 8)]

horizon = 3
