grid_1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

grid_2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

"""Unfinished!!!!"""


def numIslands(grid: list[list[str]]) -> int:
    # go through every address
    rows_amount = len(grid)
    columns_amount = len(grid[0])
    visited = [[False] * columns_amount for i in range(rows_amount)]
    r = 0
    c = 0
    island_counter = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_land(r, c):
        if grid[r][c] == "1":
            return True
        return False

    def is_unexplored(r, c):
        if visited[r][c] == False:
            return True
        return False

    def is_valid(r, c):
        if (0 <= r < rows_amount) and (0 <= c < columns_amount):
            return True
        return False

    def explore(start, grid, visited=visited):
        # for _ in visited:
        # print(_)
        # print("\n")
        row, column = start
        visited[row][column] = True
        for direction in directions:
            vert, hor = direction
            r, c = row + vert, column + hor
            if is_valid(r, c) and is_unexplored(r, c) and is_land(r, c):
                explore([r, c], grid, visited)
        return True

    for row in range(rows_amount):
        for column in range(columns_amount):
            if is_unexplored(row, column) and is_land(row, column):
                explore([row, column], grid, visited)
                island_counter += 1
            else:
                visited[row][column] = True

    return island_counter
    # for direction in direction:
    # vert, hor = direction


if __name__ == "__main__":
    island_counter = numIslands(grid=grid_2)
    print(island_counter)
