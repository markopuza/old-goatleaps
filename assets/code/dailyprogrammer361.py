'''
    Entry for Reddit's r/dailyprogrammer challenge:
            Challenge #361 [Hard] Sudoku knight's tour
            ( https://www.reddit.com/r/dailyprogrammer/comments/8ked11/20180518_challenge_361_hard_sudoku_knights_tour/ )

    Written by: Goat Leaps ( http://www.goatleaps.xyz/ )
'''

from collections import defaultdict
from random import random, shufflehttps://en.wikipedia.org/wiki/Knight%27s_tour

# size of the board
n = 9

def reverse_insort(a, x, lo=0, hi=None):
    ''' Utility: inserts element x into the array a sorted in reverse order. '''
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x > a[mid]:
            hi = mid
        else:
            lo = mid + 1
    a.insert(lo, x)

# cell_map maps the coordinates into the corresponding "cell" number in sudoku
#
#   0 | 1 | 2
#   ---------
#   3 | 4 | 5
#   ---------
#   6 | 7 | 8
#
# For this to make sense, n should be divisible by 3.
cell_map = {}
for i in range(n):
    for j in range(n):
        if i < n//3:
            if j < n//3:
                cell_map[(i, j)] = 0
            elif j < 2*n//3:
                cell_map[(i, j)] = 1
            else:
                cell_map[(i, j)] = 2
        elif i < 2*n//3:
            if j < n//3:
                cell_map[(i, j)] = 3
            elif j < 2*n//3:
                cell_map[(i, j)] = 4
            else:
                cell_map[(i, j)] = 5
        else:
            if j < n//3:
                cell_map[(i, j)] = 6
            elif j < 2*n//3:
                cell_map[(i, j)] = 7
            else:
                cell_map[(i, j)] = 8

# neighbour_map maps the coordinates to the list of possible positions where
#               a knight can jump
neighbour_map = {}
for i in range(n):
    for j in range(n):
        neighbour_map[(i, j)] = []
        for dx in [-1, 1, -2, 2]:
            for dy in [-1, 1, -2, 2]:
                if abs(dx) != abs(dy):
                    if 0 <= i + dx < n and 0 <= j + dy < n:
                        neighbour_map[(i, j)].append((i + dx, j + dy))

#### DEBUGGING variables
cnt = 0         # counts the number of positions being searched
min_depth = n*n # minimum depth encountered

# In the spirit fo the competiton, we are only trying to improve the maximum score found so far
# (In the search, we will discard anything that cannot improve this number)
best_number = tuple(map(int, '999999988988889778777766756756546654433462355415132251148115632413232234161374822'))
# In order to make search more feasible, we will replicate the first REPLICATE_FIRST digits of
# best_number in a god-like manner. Note that this may (and likely will) discard the optimal solution
REPLICATE_FIRST = 30

def search(grid, row_available, col_available, cell_available, path, pos, place_here, number, depth, free_neighs, digits_available):
    ''' Performs the search for the best sudoku/knight tour. Only searches valid positions.
        Parameters:
            - grid: sudoku numbers with numbers filled in so far. 0 denotes empty position
            - row_available: contains numbers still available at each row (in order to create a valid sudoku)
            - col_available: contains numbers still available at each row (in order to create a valid sudoku)
            - cell_available: contains numbers still available at each cell (in order to create a valid sudoku)
            - path: contains path taken by the knight up until this point
            - pos: current position of the knight
            - place_here: number to be placed at current position
            - number: score achieved thus far
            - depth: number of positions that still remain empty in the grid
            - free_neighs: for each position in the grid, contains count of how many
                           neighbours are reachable with a knight move
            - digits_available: (reverse sorted) list of digits that still weren't put into the sudoku grid

        Returns 1 if in the current branch, a valid knight tour doesn't exist. Otherwise, returns nothing.
        Saves any improved solution into a file.
    '''
    ### LOGGING
    global cnt, best_number, min_depth
    cnt += 1
    if cnt % 10000 == 0:
        print('Iteration:', cnt)
        print('Minimum depth encountered:', min_depth)

    # Place place_here at the current position and do all of the necessary bookkeeping
    x, y = pos
    min_depth = min(min_depth, depth)
    grid[x][y] = place_here
    for nx, ny in neighbour_map[(x, y)]:
        free_neighs[nx][ny] -= 1
    path.append((x, y))
    row_available[x].remove(place_here)
    col_available[y].remove(place_here)
    cell_available[cell_map[pos]].remove(place_here)
    digits_available.remove(place_here)
    number.append(place_here)

    # This variable will remain True if the current branch of the search inevitably leads
    # to a knight failure -- a valid knight tour does not exist in this branch
    knight_failure = True

    if depth == 0:
        ## A valid solution was found. Hoorray!
        if tuple(number) >= best_number:
            print()
            if tuple(number) > best_number:
                print(' IMPROVED!!!')
                ## Save the improved solution into a file
                with open('result.txt', 'w') as f:
                    f.write(str(grid) + '\n' + str(path) + '\n' + str(number))
                print(' --> ', best_number)
            else:
                print('Maximal known solution reached just now.')
            best_number = tuple(number)
    else:
        # Some PRUNING awaits us.
        # The following if condition checks whether the best possible score that we can possibly
        # reach in this branch improves best_number
        if tuple(number + digits_available) >= best_number:

            nxt = defaultdict(list) # This will be a defaultdict of all possible next moves
            for nx, ny in neighbour_map[pos]:
                if not grid[nx][ny]:
                    knight_failure = False # We have a place to move to

                    # aval_here is the set of all possible numbers we can put into [nx][ny]
                    # so it complies with the sudoku rules
                    aval_here = row_available[nx] & col_available[ny] & cell_available[cell_map[(nx, ny)]]

                    if depth > n*n - 1 - REPLICATE_FIRST:
                        # force to use the corresponding digit of best_number here
                        aval_here &= set([int(best_number[81 - depth])])
                    ### Uncomment the following in order to force NOT USING REPLICATE-th digit of best_number here
                    # elif depth == n*n - 1 - REPLICATE_FIRST:
                    #     aval_here -= set([int(best_number[81 - depth])])

                    for a in aval_here:
                        nxt[a].append((nx, ny))

            # Sort all of our available options by the highest digit that we can place
            nxt_sorted = list(nxt.items())
            nxt_sorted.sort(key=lambda x: -x[0])

            # Of all our options, this will store the coordinates where finding a knights tour *fails*
            badvs = set()

            for ii in range(len(nxt_sorted)):
                # Some form of the Warnsdorf's rule heuristic
                # -> Visit first the positions that have the fewest empty neighbours available
                nxt_sorted[ii][1].sort(key=lambda x: free_neighs[x[0]][x[1]])

                ### You may even decide to discard positions that have "too many" empty neighbours available
                # if depth <= 50:
                #     while len(nxt_sorted[ii][1]) > (1 if random() < 0.8 else 2):
                #         del nxt_sorted[ii][1][-1]

            ####
            # PRUNING PRUNING PRUNING
            ###
            # Lots of additional pruning here. At these depths, we will PRUNE.
            if 2 <= depth <= 3*n//4 or (depth > 3*n//4 and depth % 2 == 0):
                # will count the number of empty positions that have exactly one empty neighbour
                ones = 0
                # True at i-th position will mean that i-th row/column contains an empty position in the grid
                rfree, cfree = [False for _ in range(n)], [False for _ in range(n)]

                for i in range(n):
                    for j in range(n):
                        if grid[i][j] == 0: # [i][j] is empty
                            rfree[i] = True
                            cfree[j] = True

                            if len(row_available[i] & col_available[j] & cell_available[cell_map[(i, j)]]) == 0:
                                # This position doesn't have any available numbers that can be put here according
                                # to sudoku rules. Abort! Discard all of the next possible moves.
                                nxt_sorted = []
                                break

                            # Count the number of empty neighbours of this position
                            neighs = 0
                            for nx, ny in neighbour_map[(i, j)]:
                                if grid[nx][ny] == 0 or (nx, ny) == pos:
                                    neighs += 1
                                    if neighs > 1:
                                        break

                            # If there are no empty neighbours, well, this position is unreachable. Abort!
                            if neighs == 0:
                                nxt_sorted = []
                                break
                            elif neighs == 1:
                                ones += 1

                            # If there are two positions with only one available neigbour, we are doomed. Abort!
                            if ones > 2:
                                nxt_sorted = []
                                break
                    if nxt_sorted == []:
                        break

                # If there are two consecutive rows without any available empty positions,
                # such that both on the left and right of these, there ARE empty positions,
                # we have no way of jumping in between these two "islands". We are doomed.
                #
                # Same goes for columns.
                if depth <= n//2:
                    for arr in [rfree, cfree]:
                        for k in range(n):
                            if arr[k]:
                                until = 0
                                finito = False
                                for l in range(k+1, n):
                                    if not arr[l]:
                                        until += 1
                                    else:
                                        finito = True
                                        break
                                if finito and until >= 2:
                                    # Abort!!
                                    nxt_sorted = []
                                    break
            # END OF PRUNING

            # now go through the next possible steps
            failed = 0 # will count how many next steps don't have a valid knight tour
            VS = set() # just for the sake of counting how many possible next coordinates there are
            for i, vs in nxt_sorted:
                for v in vs:
                    VS.add(v)
                    if not v in badvs:
                        # Recursively perform search
                        if search(grid, row_available, col_available, cell_available, path, v, i, number, depth-1, free_neighs, digits_available) == 1:
                            # if 1 was returned, no valid knight tour exists in this branch
                            badvs.add(v)
                            failed += 1
            knight_failure = knight_failure or (0 < failed and failed == len(VS))

    # The search of this branch is done. Undo all of the necessary bookkeeping now!
    del path[-1]
    grid[x][y] = 0
    row_available[x].add(place_here)
    col_available[y].add(place_here)
    cell_available[cell_map[pos]].add(place_here)
    reverse_insort(digits_available, place_here)
    del number[-1]
    for nx, ny in neighbour_map[(x, y)]:
        free_neighs[nx][ny] += 1

    if depth > 0 and knight_failure:
        return 1

## END of search function

# Initialize the bookkeeping variables
grid = [[0 for _ in range(n)] for _ in range(n)]
row_available = [set(range(1, n*n//9+1)) for _ in range(n)]
col_available = [set(range(1, n*n//9+1)) for _ in range(n)]
cell_available = [set(range(1, n*n//9+1)) for _ in range(9)]
digits_available = []
for i in range(n, 0, -1):
    for _ in range(n):
        digits_available.append(i)
free_neighs = [[len(neighbour_map[(i, j)]) for j in range(n)] for i in range(n)]

# Place number 9 on position [1][1] and off go the search!
# Empirically, only starting with [1][1] can produce an optimal result.
search(grid, row_available, col_available, cell_available, [], (1, 1), n*n//9, [], n*n-1, free_neighs, digits_available)


# Best solution found:
#
# 999999988988889778777766756756546654433462355415132251148115632413232234161374822
#
# [[8, 5, 3, 2, 1, 7, 6, 4, 9], [2, 9, 1, 6, 4, 8, 7, 5, 3], [7, 4, 6, 9, 3, 5, 2, 8, 1], [4, 2, 5, 1, 8, 9, 3, 7, 6], [1, 6, 8, 3, 7, 4, 5, 9, 2], [9, 3, 7, 5, 6, 2, 8, 1, 4], [6, 1, 4, 8, 5, 3, 9, 2, 7], [3, 8, 2, 7, 9, 1, 4, 6, 5], [5, 7, 9, 4, 2, 6, 1, 3, 8]]
# [(1, 1), (2, 3), (3, 5), (4, 7), (6, 6), (7, 4), (8, 2), (6, 3), (7, 1), (5, 0), (4, 2), (3, 4), (1, 5), (2, 7), (0, 8), (1, 6), (3, 7), (5, 6), (4, 4), (5, 2), (7, 3), (8, 1), (6, 0), (4, 1), (2, 0), (0, 1), (1, 3), (0, 5), (1, 7), (3, 8), (4, 6), (5, 8), (7, 7), (8, 5), (6, 4), (8, 3), (6, 2), (7, 0), (5, 1), (3, 0), (2, 2), (0, 3), (2, 4), (3, 2), (5, 3), (4, 5), (5, 7), (7, 8), (8, 6), (6, 5), (8, 4), (7, 2), (8, 0), (6, 1), (4, 0), (2, 1), (0, 0), (1, 2), (0, 4), (2, 5), (0, 6), (1, 8), (2, 6), (0, 7), (2, 8), (3, 6), (5, 5), (4, 3), (3, 1), (1, 0), (0, 2), (1, 4), (3, 3), (5, 4), (7, 5), (8, 7), (6, 8), (7, 6), (8, 8), (6, 7), (4, 8)]
# [9, 9, 9, 9, 9, 9, 9, 8, 8, 9, 8, 8, 8, 8, 9, 7, 7, 8, 7, 7, 7, 7, 6, 6, 7, 5, 6, 7, 5, 6, 5, 4, 6, 6, 5, 4, 4, 3, 3, 4, 6, 2, 3, 5, 5, 4, 1, 5, 1, 3, 2, 2, 5, 1, 1, 4, 8, 1, 1, 5, 6, 3, 2, 4, 1, 3, 2, 3, 2, 2, 3, 4, 1, 6, 1, 3, 7, 4, 8, 2, 2]
