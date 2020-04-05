# tilesSearch.py by Kira DeGraw
# CS580 Assignment 1
# This program solves 8-puzzle, 16-puzzle, 24-puzzle boards using various searching methods.

import time, queue, sys
from tiles import TileGame


def main():
    inputBoard = sys.argv[1] # initial board given by user
    data = inputBoard.split() # split initial board into list

    game = TileGame(data) # creates a new game with given initial board
    print("--- Initial Board ---")
    game.printBoard(data) # print initial board
    path = search(game, data) # implementation in search function

    print("Moves =", len(path)-1) # number of moves in solution
    print("--- Final Path ---")
    for entry in path:
        game.printBoard(entry[2]) # print each move that was made

# searches for the solution using a given method
def search(game, board):
    closed = []

    # loop to verify user entered a valid search number (1-4)
    valid = False
    while valid is False:
        print("1: BFS")
        print("2: DFS")
        print("3: h1 - Number of Misplaced Tiles")
        print("4. h2 - Sum of Distances to Goal Position")
        val = input("Enter your value: ")

        if val == '1':
            q = queue.Queue() # regular queue used for BFS
            valid = True
            print("\n----- Breadth-First Search -----")
        elif val == '2':
            q = queue.LifoQueue() # LIFO queue used for DFS
            valid = True
            print("\n----- Depth-First Search -----")
        elif val == '3':
            q = queue.PriorityQueue() # priority queue used for misplaced tiles cost
            valid = True
            print("\n----- h1: Number of Misplaced Tiles -----")
        elif val == '4':
            q = queue.PriorityQueue() # priority queue used for distance to goal cost
            valid = True
            print("\n----- h2: Sum of Distances to Goal Position -----")
        else:
            print("\nInvalid Selection. Please select a number 1-4") # asks user to select a different number

    startTime = time.time() # starts time of computation
    orig = (0, 0, board, None)  # (cost, moves, board, parent)
    q.put(orig) # add original to queue
    closed.append(board) # list of already visited boards
    expanded = 0 # keep track of how many boards have been expanded
    solution = None
    while q and not solution:
        parent = q.get() # pop original board
        expanded += 1 # expand original board
        (parCost, parMoves, parBoard, ancester) = parent
        empty, moves = game.getMoves(parBoard) # find legal moves allowed for parent
        print("--- Possible moves for parent ---")
        game.printBoard(parBoard) # print parent board
        for mov in moves:
            childBoard = game.makeMove(parBoard, empty, mov) # make each possible move

            if childBoard in closed:
                print("Child Already Visited:") # don't add to queue if visited
                game.printBoard(childBoard)
                continue
            print("Child Added to Queue:")
            game.printBoard(childBoard)
            closed.append(childBoard) # add to closed list
            childMoves = parMoves + 1
            if val == '3':
                childCost = game.heuristic1(childBoard)
                print("^ Child Cost:", childCost, "\n") # find cost for h1
            elif val == '4':
                childCost = game.heuristic2(childBoard) # find cost for h2
                print("^ Child Cost:", childCost, "\n")
            else:
                 childCost = 0 # cost isn't relevant for bfs, dfs
            child = (childCost, childMoves, childBoard, parent)
            q.put(child) # add child to queue
            if childBoard == game.goal: solution = child

    if solution:
        endTime = time.time() - startTime # total time
        print("Solution Found!")
        print(expanded, "entries expanded. Queue still has", q.qsize(), "entries")
        print("Search took", endTime, "seconds")
        # find the path leading to this solution
        path = []
        while solution:
            path.append(solution[0:3])  # drop the parent
            solution = solution[3]  # to grandparent
        path.reverse() # put path in order
        return path
    else:
        return []



if __name__ == "__main__":
    main()
