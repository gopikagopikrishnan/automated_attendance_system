from tkinter import * 

class GUI(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Lab 8")
        self.grid()
        self.canvas_width = 800
        self.canvas_height = 400
        self.canvas = Canvas(self, 
                             width=self.canvas_width, 
                             height=self.canvas_height, 
                             bg="white")
        self.canvas.grid()

        self.ball_diameter = 20
        self.top_x = 2
        self.top_y = 2
        self.canvas.create_oval(self.top_x, 
                                self.top_y, 
                                self.top_x + self.ball_diameter,
                                self.top_y + self.ball_diameter, 
                                fill = "black", tags = "ball")

        self.horizontal_direction = "east"
        self.vertical_direction = "south"
        self.dx = 2
        self.dy = 2

        self.after(10, self.move)


    def move(self):

        if self.horizontal_direction == "east":
            self.canvas.move("ball", self.dx, 0) # move ball horizontally dx pixels to the right/east
            self.top_x += self.dx # dx is 2 because the ball moves 2 pixels horizontally every 15 milliseconds
            if self.top_x >= self.canvas_width - self.ball_diameter: # ball has hit east wall
                self.horizontal_direction = "west" # change direction
        else: # i.e., horizontal_direction is "west"
            self.canvas.move("ball", -self.dx, 0) # move ball horizontally dx pixels to the left/west
            self.top_x -= self.dx 
            if self.top_x <= 0: # ball has hit west wall
                self.horizontal_direction = "east" # change direction

        if self.vertical_direction == "south":
            self.canvas.move("ball", 0, self.dy)
            self.top_y += self.dy
            if self.top_y >= self.canvas_height - self.ball_diameter:
                self.vertical_direction = "north"
        else:
            self.canvas.move("ball", 0, -self.dy)
            self.top_y -= self.dy
            if self.top_y <= 0 :
                self.vertical_direction = "south"

        self.after(10, self.move)


def main():
    GUI().mainloop()

main()