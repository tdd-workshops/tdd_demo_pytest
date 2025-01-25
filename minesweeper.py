def gridHasIndex(gridSize, row, col):
    if row < 0 or col < 0 or col > (gridSize[0]-1) or row > (gridSize[1]-1):
        return False

    return True


def minesweeper(gridSize=[], mines=[]):
    grid = []

    for _ in range(gridSize[1]):
        grid.append(["."] * gridSize[0])

    for mine in mines:
        col = mine[0]
        row = mine[1]
        cellCandidate = grid[row][col]

        if cellCandidate == "." or int(cellCandidate) == cellCandidate:
            grid[row][col] = "*"

            # Find my neighbours
            neighbours = [
                [row-1, col-1], [row-1, col], [row-1, col+1],
                [row, col-1],                 [row, col+1],
                [row+1, col-1], [row+1, col], [row+1, col+1]
            ]

            for cellCoord in neighbours:
                if gridHasIndex(gridSize, cellCoord[0], cellCoord[1]):
                    cellValue = grid[cellCoord[0]][cellCoord[1]]
                    if cellValue == "*":
                        next
                    elif cellValue == ".":
                        grid[cellCoord[0]][cellCoord[1]] = 1
                    else:
                        grid[cellCoord[0]][cellCoord[1]] += 1

    return grid
