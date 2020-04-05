# tiles.py by Kira DeGraw
# helper for tilesSearch.py

import sys

class TileGame:
    def __init__(self, board=[], dim=None):

        # goal for each dimension of puzzle
        if len(board) == 9 or dim == 3:
            self.dim = 3
            self.legalMoves = legalMoves3
            self.goal = ['1', '2', '3', '4', '5', '6', '7', '8', '0']
        elif len(board) == 16 or dim == 4:
            self.dim = 4
            self.legalMoves = legalMoves4
            self.goal = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '0']
        elif len(board) == 25 or dim == 5:
            self.dim = 5
            self.legalMoves = legalMoves5
            self.goal = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                         '18', '19', '20', '21', '22', '23', '24', '0']
        else:
            print("Invalid dimension or sample board")
            sys.exit(1)

        # verify board can be solved
        if board and sorted(board) != sorted(self.goal):
            print("Invalid sample board")
            sys.exit(1)

    # get the legal moves for the current space (0) position
    def getMoves(self, board):
        empty = board.index('0')
        return empty, self.legalMoves[empty]

    # switch space (0) and the second given position
    def makeMove(self, board, empty, mov):
        board = list(board)
        board[empty], board[mov] = board[mov], board[empty]
        return board

    # counts number of misplaced tiles on the board
    def heuristic1(self, board):
        misplaced = 0
        for pos in range(self.dim * self.dim):
            occupant = board[pos]
            if self.goal[pos] != occupant:
                misplaced += 1
        return misplaced

    # cost = sum of distances of every tile to its goal position
    # does not count the blank space
    def heuristic2(self, board):
        cost = 0
        for pos in range(self.dim * self.dim):
            occupant = int(board[pos])
            goal = self.goal.index(str(occupant))

            if occupant != 0:
                row = abs(pos % self.dim - goal % self.dim)
                col = abs(pos//self.dim - goal//self.dim)
                cost += (row+col)
        return cost

    # prints a given board in a readable format with correct rows and columns
    def printBoard(self, board):
        expand = ["%02s" % x for x in board]
        rows = [0] * self.dim
        for i in range(self.dim):
            rows[i] = "|" + " ".join(expand[self.dim * i:self.dim * (i + 1)]) + " |"
        print("\n".join(rows))
        print("\r")


# legal moves for each dimension
legalMoves3 = (  # for a 3x3 board
    (1, 3),  # these can slide into square 0
    (0, 4, 2),  # these can slide into square 1
    (1, 5),  # these can slide into square 2
    (0, 4, 6),  # these can slide into square 3
    (1, 3, 5, 7),  # these can slide into square 4
    (2, 4, 8),  # these can slide into square 5
    (3, 7),  # these can slide into square 6
    (4, 6, 8),  # these can slide into square 7
    (5, 7))  # these can slide into square 8

legalMoves4 = (  # for a 4x4 board
    (1, 4),  # these can slide into square  0
    (0, 5, 2),  # these can slide into square  1
    (1, 6, 3),  # these can slide into square  2
    (2, 7),  # these can slide into square  3
    (0, 5, 8),  # these can slide into square  4
    (1, 4, 6, 9),  # these can slide into square  5
    (2, 5, 7, 10),  # these can slide into square  6
    (3, 6, 11),  # these can slide into square  7
    (4, 9, 12),  # these can slide into square  8
    (5, 8, 10, 13),  # these can slide into square  9
    (6, 9, 11, 14),  # these can slide into square 10
    (7, 10, 15),  # these can slide into square 11
    (8, 13),  # these can slide into square 12
    (9, 12, 14),  # these can slide into square 13
    (10, 13, 15),  # these can slide into square 14
    (11, 14))  # these can slide into square 15

legalMoves5 = (  # for a 5x5 board
    (1, 5),  # these can slide into square  0
    (0, 2, 6),  # these can slide into square  1
    (1, 3, 7),  # these can slide into square  2
    (2, 4, 8),  # these can slide into square  3
    (3, 9),  # these can slide into square  4
    (0, 6, 10),  # these can slide into square  5
    (1, 5, 7, 11),  # these can slide into square  6
    (2, 6, 8, 12),  # these can slide into square  7
    (3, 7, 9, 13),  # these can slide into square  8
    (4, 8, 14),  # these can slide into square  9
    (5, 11, 15),  # these can slide into square 10
    (6, 10, 12, 16),  # these can slide into square 11
    (7, 11, 13, 17),  # these can slide into square 12
    (8, 12, 14, 18),  # these can slide into square 13
    (9, 13, 19),  # these can slide into square 14
    (10, 16, 20),  # these can slide into square 15
    (11, 15, 17, 21),  # these can slide into square 16
    (12, 16, 18, 22),  # these can slide into square 17
    (13, 17, 19, 23),  # these can slide into square 18
    (14, 18, 24),  # these can slide into square 19
    (15, 21),  # these can slide into square 20
    (16, 20, 22),  # these can slide into square 21
    (17, 21, 23),  # these can slide into square 22
    (18, 22, 24),  # these can slide into square 23
    (19, 23))  # these can slide into square 24
