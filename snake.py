from turtle import Turtle
POSITION = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        super().__init__()
        self.segment_list = []
        for i in range(3):
            new_seg = Turtle('square')
            new_seg.color('yellow')
            new_seg.penup()
            new_seg.goto(POSITION[i])
            self.segment_list.append(new_seg)
        self.head = self.segment_list[0]

    def move(self):
        for seg in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[seg-1].xcor()
            new_y = self.segment_list[seg-1].ycor()
            self.segment_list[seg].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def left(self):
        self.head.setheading(180)
    def right(self):
        self.head.setheading(0)