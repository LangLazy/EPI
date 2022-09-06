import collections


Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))
def search_maze(maze: list[list[int]], s: Coordinate,
                e: Coordinate) -> list[Coordinate]:
    def isValid(h,v):
        return h >= 0 and h < len(maze) and v >= 0 and v< len(maze[0])
    def recur(h,v):
        if not isValid(h,v) or maze[h][v] > 0:
            return False
        if h == e[0] and v == e[1]:
            return True
        maze[h][v] = 2        
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        for dh,dv in dirs:
            if recur(h+dh, v+dv):
                return True
        return False
    return recur(s[0], s[1])
maze = [[0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 1, 1, 0, 1], [1, 0, 0, 0, 0], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 0, 0, 0], [1, 0, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [1, 0, 0, 1, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 1, 1]]
print(search_maze(maze, [8, 3], [17, 1]))