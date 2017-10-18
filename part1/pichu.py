#!/usr/bin/env python3
# Authors: Umang Mehta, Samanvitha Pradhan & Vaishnavi Srinivasan


def action():
	# TODO: each successor for pawn, rook, knight, queen, king, bishop
	pass


def evaluation(board):
	# TODO: Evaluation Function for the Leaf Nodes of the Game Tree
	pass


def is_terminal(board):
	# TODO: Check if the Board State is a Terminal State
	pass


def successors(board):
	# TODO: Generate all successor board to th given board
	pass


# TODO: Minimax with Alpha-Beta Pruning


inputBoard = []
initialPosition="RNBQKBNRPPPPPPPP................................pppppppprnbqkbnr"
for counter in range(0,len(initialPosition),1):
	inputBoard.append(initialPosition[counter])

horizon = 3

