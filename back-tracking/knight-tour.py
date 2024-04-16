# Given a NxN matrix, knight must visit all squares exactly once

n = 8

# checks if potential cell is safe/valid
def isValid(x, y, board):
  if x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1:
    return True
  return False

# prints the solution board
def printSolution(n, board):
  for i in range(n):
    for j in range(n):
      print(board[i][j], end=" ")
    print()


def main():
  board = [[-1 for i in range(n)] for i in range(n)]  
  # inits the valid movements array
  moves_x = [2, 1, -1, -2, -2, -1, 1,  2] 
  moves_y = [1, 2,  2,  1, -1, -2, -2, -1] 
  
  board[0][0] = 0
  counter = 1 # counts how many cells have been visited, will also indicated what turn cell was visited
  
  if (not backtrack(n, 0, 0, moves_x, moves_y, board, counter)):
    print("No successful solution found!")
  else:
    printSolution(n, board)  

# A recursive backtracking loop
def backtrack(n, curr_x, curr_y, moves_x, moves_y, board, counter):
  # checks if all cells have been visited
  if (counter == n**2):
    return True
  
  # try all possible forward moves
  for i in range(8):
    forward_x = curr_x + moves_x[i]
    forward_y = curr_y + moves_y[i]
    if (isValid(forward_x, forward_y, board)):
      board[forward_x][forward_y] = counter
      if (backtrack(n, forward_x, forward_y, moves_x, moves_y, board, counter+1)):
        return True
  
        # backtrack when all possible forward moves are exhausted
      board[forward_x][forward_y] = -1
  return False

if __name__ == '__main__':
  main()