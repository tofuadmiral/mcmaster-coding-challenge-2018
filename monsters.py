## first grab dimensions
dimensions = str.split(raw_input())
rows = int(dimensions[0])
cols = int(dimensions[1])

## initialize the grid of booleans
grid = []
grid = [[True for x in range(cols+1)] for y in range(rows+1)] 
paths = [[0 for x in range(cols+1)] for y in range(rows+1)] ## initialize paths for memoization


## populate the grid with monsters
## next line is number of monsters
numMonsters = int(raw_input())

## loop while there are still monsters, each line shld be coords of the next monster
for i in range(numMonsters):
    coords = str.split(raw_input())
    rowCoord = int(coords[0])
    colCoord = int(coords[1])
    grid[rowCoord-1][colCoord-1] = False ## -1 bc starts from index 0 
    
## figure out if we're at the end of the grid or not
def isAtEnd(grid, row, col):
    if len(grid)-2 == row and len(grid[0])-2 == col:
        return True
    else:
        return False

## create a recursive function to find how many paths there are
def countPaths(grid, row, col, paths):
    if (grid[row][col]) == False: ## we're at a monster so return 0 
        return 0
    elif isAtEnd(grid, row, col): ## we're at the end so add one path 
        return 1
    elif row > len(grid)-2 or col>len(grid[0])-2: ## we're out of bounds, return 0
        return 0
    elif paths[row][col] == 0: ## memoization so we store and don't double count 
        paths[row][col] = countPaths(grid, row+1, col, paths) + countPaths(grid, row, col+1, paths)
    return paths[row][col]

## print number of paths
print countPaths(grid, 0, 0, paths)
