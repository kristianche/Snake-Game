from tkinter import *
WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20
IN_GAME = True

root = Tk()
c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#ffffff")
c.grid()
c.focus_set()


class Segment(object):
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y, x + SEG_SIZE, y + SEG_SIZE, fill="green")


snake = Segment(500, 2)
root.title("Snake Game")
root.mainloop()