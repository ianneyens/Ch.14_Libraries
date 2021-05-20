import arcade

SW = 600
SH = 600
box_num = 30
BW = 30


class Box:
    def __init__(self, x, y, s, dx, dy, c):
        self.x = x
        self.y = y
        self.s = s
        self.dx = dx
        self.dy = dy
        self.c = c

    def draw_box(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.s, self.s, self.c)

    def update_box(self):
        self.x += self.dx
        self.y += self.dy

        if self.x <= BW + self.s / 2:
            self.dx *= -1
            self.c = arcade.color.RED

        if self.x >= SW - BW - self.s / 2:
            self.dx *= -1
            self.c = arcade.color.YELLOW

        if self.y >= SH - BW - self.s / 2:
            self.dy *= -1
            self.c = arcade.color.GREEN

        if self.y <= BW + self.s / 2:
            self.dy *= -1
            self.c = arcade.color.BLUE
