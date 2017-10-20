#!/usr/bin/env python3
# Authors: Umang Mehta, Samanvitha Pradhan & Vaishnavi Srinivasan
import copy

def findPos(board, charToBeFound):
	return [(row, col) for col in range(0,8,1) for row in range(0,8,1) if board[row][col] == charToBeFound ]

def updatePos(board, charToReplace, xPos1, yPos1, xPos2, yPos2):
	tempState=copy.deepcopy(board)
	tempState[xPos1][yPos1]='.'
	tempState[xPos2][yPos2]=charToReplace
	return tempState

def action():
	# TODO: each successor for pawn, rook, knight, queen, king, bishop
	pass


def evaluation(board):
	# TODO: Evaluation Function for the Leaf Nodes of the Game Tree
	pass


def is_terminal(board):
	# TODO: Check if the Board State is a Terminal State
	pass


def successors(currentState):
	#https://stackoverflow.com/questions/6614891/turning-a-list-into-nested-lists-in-python
	currentState = [board[i:i+8] for i in range(0, len(board), 8)]
	successor=[[]]
	successor = [row for row in pawnSuccessor if row != []]
	#each successor for pawn
	if actionState="Parakeet":
		pawnPos=findPos(currentState, 'P')
		for possiblePositions in range(0,len(pawnPos),1):
			rowCounter=pawnPos[possiblePositions][0]
			colCounter=pawnPos[possiblePositions][1]
			#move pawn down
			if (rowCounter+1) <= 7 :
				if (currentState[rowCounter+1][colCounter].islower()) or currentState[rowCounter+1][colCounter] == '.' :
					successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter+1,colCounter,'P'))
			if rowCounter == 1 :
				if currentState[rowCounter+1][colCounter] == '.'  and currentState[rowCounter+2][colCounter] == '.' :
					successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter+2,colCounter,'P'))
			#move pawn left
			if (colCounter-1) >= 0 :
				if (currentState[rowCounter][colCounter-1].islower()) or currentState[rowCounter][colCounter-1] == '.':
					successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter,colCounter-1,'P'))
			#move pawn right
			if (colCounter+1) <= 7 :
				if (currentState[rowCounter][colCounter+1].islower()) or currentState[rowCounter][colCounter+1] == '.' :
					successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter,colCounter+1,'P'))
			#move pawn left diagonally
			if (colCounter-1) >= 0 and (rowCounter+1) <= 7 :
				if (currentState[rowCounter+1][colCounter-1].islower()) :
					successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter+1,colCounter-1,'P'))
			#move pawn right diagonally
			if (colCounter+1) <= 7 and (rowCounter+1) <= 7 :
				if (currentState[rowCounter+1][colCounter+1].islower()) :
					successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter+1,colCounter+1,'P'))
	#each successor for rook
	if actionState="Robin":
		rookPos=findPos(currentState, 'R')
		for possiblePositions in range(0,len(rookPos),1):
			rowCounter=rookPos[possiblePositions][0]
			colCounter=rookPos[possiblePositions][1]
			#move rook up
			for i in range(rowCounter-1,-1,-1):
				if (currentState[i][colCounter].isupper()) :
					break
				elif (currentState[i][colCounter].islower()) :
					successor.append(updatePos(currentState,rowCounter,colCounter,i,colCounter,'R'))
					break
				elif currentState[i][colCounter] == '.' :
					successor.append(updatePos(currentState,rowCounter,colCounter,i,colCounter,'R'))
				else:
					pass
			#move rook down
			for i in range(rowCounter+1,8,1):
				if (currentState[i][colCounter].isupper()) :
					break
				elif (currentState[i][colCounter].islower()) :
					successor.append(updatePos(currentState,rowCounter,colCounter,i,colCounter,'R'))
					break
				elif currentState[i][colCounter] == '.' :
					successor.append(updatePos(currentState,rowCounter,colCounter,i,colCounter,'R'))
				else:
					pass
			#move rook left
			for i in range(colCounter-1,-1,-1):
				if (currentState[rowCounter][i].isupper()) :
					break
				elif (currentState[rowCounter][i].islower()) :
					successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter,i,'R'))
					break
				elif currentState[rowCounter][i] == '.' :
					successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter,i,'R'))
				else:
					pass
			#move rook right
			for i in range(colCounter+1,8,1):
				if (currentState[rowCounter][i].isupper()) :
					break
				elif (currentState[rowCounter][i].islower()) :
					successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter,i,'R'))
					break
				elif currentState[rowCounter][i] == '.' :
					successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter,i,'R'))
				else:
					pass
	#each successor for bishop
	if actionState="Blue jay":
		bishopPos=findPos(currentState, 'B')
		for possiblePositions in range(0,len(bishopPos),1):
			rowCounter=bishopPos[possiblePositions][0]
			colCounter=bishopPos[possiblePositions][1]
			#move bishop to the left
			for r in range(rowCounter,-1,-1):
				if ((rowCounter-r) >= 0  and (colCounter-r) >= 0):
					if (currentState[rowCounter-r][colCounter-r].isupper()) :
						break
					elif (currentState[rowCounter-r][colCounter-r].islower()) :
						successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter-r,colCounter-r,'B'))
						break
					elif currentState[rowCounter-r][colCounter-r] == '.' :
						successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter-r,colCounter-r,'B'))
					else:
						pass
			i=1
			for r in range(rowCounter,8,1):
				if ((rowCounter+i) < 8 and (colCounter+i) < 8):
					if (currentState[rowCounter+i][colCounter+i].isupper()) :
						break
					elif (currentState[rowCounter+i][colCounter+i].islower()) :
						successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter+i,colCounter+i,'B'))
						break
					elif currentState[rowCounter+i][colCounter+i] == '.' :
						successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter+i,colCounter+i,'B'))
					else:
						pass
					i+=1
			i=0
			#move bishop to the right
			for r in range(rowCounter,-1,-1):
				if ((rowCounter-i) >= 0  and (colCounter+i) < 8):
					if (currentState[rowCounter-i][colCounter+i].isupper()) :
						break
					elif (currentState[rowCounter-i][colCounter+i].islower()) :
						successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter-i,colCounter+i,'B'))
						break
					elif currentState[rowCounter-i][colCounter+i] == '.' :
						successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter-i,colCounter+i,'B'))
					else:
						pass
					i+=1
			i=1
			for r in range(rowCounter,8,1):
				if ((rowCounter+i) < 8 and (colCounter-i) >= 0):
					if (currentState[rowCounter+i][colCounter-i].isupper()) :
						break
					elif (currentState[rowCounter+i][colCounter-i].islower()) :
						successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter+i,colCounter-i,'B'))
						break
					elif currentState[rowCounter+i][colCounter-i] == '.' :
						successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter+i,colCounter-i,'B'))
					else:
						pass
					i+=1
	#each successor for queen
	if actionState="Quetzal":
		queenPos=findPos(currentState, 'Q')
		queenSuccessor=[[]]
		queenSuccessor = [row for row in queenSuccessor if row != []]
		for possiblePositions in range(0,len(queenPos),1):
			rowCounter=queenPos[possiblePositions][0]
			colCounter=queenPos[possiblePositions][1]
			#move queen to the left
			for r in range(rowCounter,-1,-1):
				if ((rowCounter-r) >= 0  and (colCounter-r) >= 0):
					if (currentState[rowCounter-r][colCounter-r].isupper()) :
						break
					elif (currentState[rowCounter-r][colCounter-r].islower()) :
						tempState=copy.deepcopy(currentState)
						tempState[rowCounter][colCounter]='.'
						tempState[rowCounter-r][colCounter-r]='Q'
						queenSuccessor.append(tempState)
						break
					elif currentState[rowCounter-r][colCounter-r] == '.' :
						tempState=copy.deepcopy(currentState)
						tempState[rowCounter][colCounter]='.'
						tempState[rowCounter-r][colCounter-r]='Q'
						queenSuccessor.append(tempState)
					else:
						pass
			i=1
			for r in range(rowCounter,8,1):
				if ((rowCounter+i) < 8 and (colCounter+i) < 8):
					if (currentState[rowCounter+i][colCounter+i].isupper()) :
						break
					elif (currentState[rowCounter+i][colCounter+i].islower()) :
						tempState=copy.deepcopy(currentState)
						tempState[rowCounter][colCounter]='.'
						tempState[rowCounter+i][colCounter+i]='Q'
						queenSuccessor.append(tempState)
						break
					elif currentState[rowCounter+i][colCounter+i] == '.' :
						tempState=copy.deepcopy(currentState)
						tempState[rowCounter][colCounter]='.'
						tempState[rowCounter+i][colCounter+i]='Q'
						queenSuccessor.append(tempState)
					else:
						pass
					i+=1
			i=0
			#move queen to the right
			for r in range(rowCounter,-1,-1):
				if ((rowCounter-i) >= 0  and (colCounter+i) < 8):
					if (currentState[rowCounter-i][colCounter+i].isupper()) :
						break
					elif (currentState[rowCounter-i][colCounter+i].islower()) :
						tempState=copy.deepcopy(currentState)
						tempState[rowCounter][colCounter]='.'
						tempState[rowCounter-i][colCounter+i]='Q'
						queenSuccessor.append(tempState)
						break
					elif currentState[rowCounter-i][colCounter+i] == '.' :
						tempState=copy.deepcopy(currentState)
						tempState[rowCounter][colCounter]='.'
						tempState[rowCounter-i][colCounter+i]='Q'
						queenSuccessor.append(tempState)
					else:
						pass
					i+=1
			i=1
			for r in range(rowCounter,8,1):
				if ((rowCounter+i) < 8 and (colCounter-i) >= 0):
					if (currentState[rowCounter+i][colCounter-i].isupper()) :
						break
					elif (currentState[rowCounter+i][colCounter-i].islower()) :
						tempState=copy.deepcopy(currentState)
						tempState[rowCounter][colCounter]='.'
						tempState[rowCounter+i][colCounter-i]='Q'
						queenSuccessor.append(tempState)
						break
					elif currentState[rowCounter+i][colCounter-i] == '.' :
						tempState=copy.deepcopy(currentState)
						tempState[rowCounter][colCounter]='.'
						tempState[rowCounter+i][colCounter-i]='Q'
						queenSuccessor.append(tempState)
					else:
						pass
					i+=1
			#move queen up
			for i in range(rowCounter-1,-1,-1):
				if (currentState[i][colCounter].isupper()) :
					break
				elif (currentState[i][colCounter].islower()) :
					tempState=copy.deepcopy(currentState)
					tempState[rowCounter][colCounter]='.'
					tempState[i][colCounter]='Q'
					queenSuccessor.append(tempState)
					break
				elif currentState[i][colCounter] == '.' :
					tempState=copy.deepcopy(currentState)
					tempState[rowCounter][colCounter]='.'
					tempState[i][colCounter]='Q'
					queenSuccessor.append(tempState)
				else:
					pass
			#move queen down
			for i in range(rowCounter+1,8,1):
				if (currentState[i][colCounter].isupper()) :
					break
				elif (currentState[i][colCounter].islower()) :
					tempState=copy.deepcopy(currentState)
					tempState[rowCounter][colCounter]='.'
					tempState[i][colCounter]='Q'
					queenSuccessor.append(tempState)
					break
				elif currentState[i][colCounter] == '.' :
					tempState=copy.deepcopy(currentState)
					tempState[rowCounter][colCounter]='.'
					tempState[i][colCounter]='Q'
					queenSuccessor.append(tempState)
				else:
					pass
			#move queen left
			for i in range(colCounter-1,-1,-1):
				if (currentState[rowCounter][i].isupper()) :
					break
				elif (currentState[rowCounter][i].islower()) :
					tempState=copy.deepcopy(currentState)
					tempState[rowCounter][colCounter]='.'
					tempState[rowCounter][i]='Q'
					queenSuccessor.append(tempState)
					break
				elif currentState[rowCounter][i] == '.' :
					tempState=copy.deepcopy(currentState)
					tempState[rowCounter][colCounter]='.'
					tempState[rowCounter][i]='Q'
					queenSuccessor.append(tempState)
				else:
					pass
			#move queen right
			for i in range(colCounter+1,8,1):
				if (currentState[rowCounter][i].isupper()) :
					break
				elif (currentState[rowCounter][i].islower()) :
					tempState=copy.deepcopy(currentState)
					tempState[rowCounter][colCounter]='.'
					tempState[rowCounter][i]='Q'
					queenSuccessor.append(tempState)
					break
				elif currentState[rowCounter][i] == '.' :
					tempState=copy.deepcopy(currentState)
					tempState[rowCounter][colCounter]='.'
					tempState[rowCounter][i]='Q'
					queenSuccessor.append(tempState)
				else:
					pass
	#each successor for king
	if actionState="Kingfisher":
		kingPos=findPos(currentState, 'K')
		for possiblePositions in range(0,len(kingPos),1):
			rowCounter=kingPos[possiblePositions][0]
			colCounter=kingPos[possiblePositions][1]
			#move king up
			if (currentState[rowCounter-1][colCounter].islower()) or currentState[rowCounter-1][colCounter] == '.' :
				successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter-1,colCounter,'K'))
			#move king down
			if (currentState[rowCounter+1][colCounter].islower()) or currentState[rowCounter+1][colCounter] == '.' :
				successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter+1,colCounter,'K'))
			#move king left
			if (currentState[rowCounter][colCounter-1].islower()) or currentState[rowCounter][colCounter-1] == '.' :
				successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter,colCounter-1,'K'))
			#move king right
			if (currentState[rowCounter][colCounter+1].islower()) or currentState[rowCounter][colCounter+1] == '.' :
				successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter,colCounter+1,'K'))
			#move king left diagonally down
			if (currentState[rowCounter+1][colCounter-1].islower()) or currentState[rowCounter+1][colCounter-1] == '.' :
				successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter+1,colCounter-1,'K'))
			#move king right diagonally down
			if (currentState[rowCounter+1][colCounter+1].islower()) or currentState[rowCounter+1][colCounter+1] == '.' :
				successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter+1,colCounter+1,'K'))
			#move king left diagonally up
			if (currentState[rowCounter-1][colCounter-1].islower()) or currentState[rowCounter-1][colCounter-1] == '.' :
				successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter-1,colCounter-1,'K'))
			#move king right diagonally up
			if (currentState[rowCounter-1][colCounter+1].islower()) or currentState[rowCounter-1][colCounter+1] == '.' :
				successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter-1,colCounter+1,'K'))
	#each successor for knight
	if actionState="Nighthawk":
		knightPos=findPos(currentState, 'N')
		for possiblePositions in range(0,len(knightPos),1):
			rowCounter=knightPos[possiblePositions][0]
			colCounter=knightPos[possiblePositions][1]
			#move knight up right L
			if (rowCounter-1) >= 0 and (colCounter+2) <= 7  :
				if (currentState[rowCounter-1][colCounter+2].islower()) or currentState[rowCounter-1][colCounter+2] == '.' :
					successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter-1,colCounter+2,'N'))
			if (rowCounter-2) >= 0 and (colCounter+1) <= 7  :
				if (currentState[rowCounter-2][colCounter+1].islower()) or currentState[rowCounter-2][colCounter+1] == '.' :
					successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter-2,colCounter+1,'N'))
			#move knight up left L
			if (rowCounter-1) >= 0 and (colCounter-2) <= 7  :
				if (currentState[rowCounter-1][colCounter-2].islower()) or currentState[rowCounter-1][colCounter-2] == '.' :
					successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter-1,colCounter-2,'N'))
			if (rowCounter-2) >= 0 and (colCounter+1) <= 7  :
				if (currentState[rowCounter-2][colCounter-1].islower()) or currentState[rowCounter-2][colCounter-1] == '.' :
					successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter-2,colCounter-1,'N'))
			#move knight down left L
			if (rowCounter+2) >= 0 and (colCounter+1) <= 7  :
				if (currentState[rowCounter+2][colCounter+1].islower()) or currentState[rowCounter+2][colCounter+1] == '.' :
					successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter+2,colCounter+1,'N'))
			if (rowCounter+1) >= 0 and (colCounter+2) <= 7  :
				if (currentState[rowCounter+1][colCounter+2].islower()) or currentState[rowCounter+1][colCounter+2] == '.' :
					successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter+1,colCounter+2,'N'))
			#move knight down left L
			if (rowCounter+2) >= 0 and (colCounter-1) <= 7  :
				if (currentState[rowCounter+2][colCounter-1].islower()) or currentState[rowCounter+2][colCounter-1] == '.' :
					successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter+2,colCounter-1,'N'))
			if (rowCounter+1) >= 0 and (colCounter-2) <= 7  :
				if (currentState[rowCounter+1][colCounter-2].islower()) or currentState[rowCounter+1][colCounter-2] == '.' :
					successor.append(updatePos(currentState,rowCounter,colCounter,rowCounter+1,colCounter-2,'N'))

# TODO: Minimax with Alpha-Beta Pruning


inputBoard = []
initialPosition="RNBQKBNRPPPPPPPP................................pppppppprnbqkbnr"
for counter in range(0,len(initialPosition),1):
	inputBoard.append(initialPosition[counter])

currentState = [inputBoard[i:i+8] for i in range(0, len(inputBoard), 8)]
successors(currentState)

horizon = 3

