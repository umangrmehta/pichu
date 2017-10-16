#!/usr/bin/env python3
# Authors: Umang Mehta, Samanvitha Pradhan & Vaishnavi Srinivasan


def action():
	# TODO: each successor for pawn, rook, knight, queen, king, bishop
	pass


def evaluation():
	# TODO: Evaluation Function for the Leaf Nodes of the Game Tree
	pass


# TODO: Minimax with Alpha-Beta Pruning


inputBoard=[]
initialPosition="RNBQKBNRPPPPPPPP................................pppppppprnbqkbnr"
for counter in range(0,len(initialPosition),1):
	inputBoard.append(initialPosition[counter])
