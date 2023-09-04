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


def numIslands(grid: list[list[str]]) -> int:
    from collections import deque

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

    dq = deque()
    for _row in range(rows_amount):
        for _column in range(columns_amount):
            for _ in visited:
                print(_)
            print("\n")

            if is_unexplored(_row, _column) and is_land(_row, _column):
                island_counter += 1
                dq.append((_row, _column))
                while len(dq) > 0:
                    row, column = dq.popleft()
                    visited[row][column] = True
                    for direction in directions:
                        ver, hor = direction
                        r, c = row + ver, column + hor
                        if not is_valid(r, c):
                            continue
                        if is_unexplored(r, c) and is_land(r, c):
                            dq.append((r, c))
            else:
                visited[_row][_column] = True

    return island_counter


if __name__ == "__main__":
    island_counter = numIslands(grid=grid_2)
    print(island_counter)
