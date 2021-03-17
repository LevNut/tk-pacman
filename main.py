import tkinter as tk

from gamelib import Sprite, GameApp, Text

from maze import Maze

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

UPDATE_DELAY = 33


class PacmanGame(GameApp):
    def create_sprites(self):
        pass

    def init_game(self):
        self.create_sprites()

        self.maze = Maze(self, CANVAS_WIDTH, CANVAS_HEIGHT)

    def pre_update(self):
        pass

    def post_update(self):
        pass

    def on_key_pressed(self, event):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monkey Banana Game")
 
    # do not allow window resizing
    root.resizable(False, False)
    app = PacmanGame(root, CANVAS_WIDTH, CANVAS_HEIGHT, UPDATE_DELAY)
    app.start()
    root.mainloop()
