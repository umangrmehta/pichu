#!/usr/bin/env python3
# Authors: Umang Mehta, Samanvitha Pradhan & Vaishnavi Srinivasan

import math


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
initialPosition="RNBQKBNRPPPPPPPP................................pppppppprnbqkbnr"
for counter in range(0,len(initialPosition),1):
	inputBoard.append(initialPosition[counter])

horizon = 3

