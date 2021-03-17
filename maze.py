from gamelib import Sprite

class Dot(Sprite):
    def __init__(self, app, x, y):
        super().__init__(app, 'images/dot.png', x, y)


class Wall(Sprite):
    def __init__(self, app, x, y):
        super().__init__(app, 'images/wall.png', x, y)


class Maze:
    MAP = [
        "####################",
        "#..................#",
        "#.###.###..###.###.#",
        "#.#...#......#...#.#",
        "#.#.###.####.###.#.#",
        "#.#.#..........#.#.#",
        "#.....###..###.....#",
        "#.#.#..........#.#.#",
        "#.#.###.####.###.#.#",
        "#.#...#......#...#.#",
        "#.###.###..###.###.#",
        "#..................#",
        "####################",    
    ]

    def piece_center(self, r, c):
        return (c*40 + 20, self.canvas_height - (r * 40) - 60)

    def init_maze_sprites(self):
        self.dots = []
        self.walls = []

        for i in range(self.get_height()):
            for j in range(self.get_width()):
                x, y = self.piece_center(i, j)

                if self.has_wall_at(i, j):
                    wall = Wall(self.app, x, y)
                    self.walls.append(wall)

                if self.has_dot_at(i, j):
                    dot = Dot(self.app, x, y)
                    self.dots.append(dot)            

    def __init__(self, app, canvas_width, canvas_height):
        self.app = app
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        self.init_maze_sprites()

    def init_element(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def has_wall_at(self, r, c):
        return Maze.MAP[r][c] == '#'

    def has_dot_at(self, r, c):
        return Maze.MAP[r][c] == '.'

    def get_height(self):
        return len(Maze.MAP)

    def get_width(self):
        return len(Maze.MAP[0])

