from turtle import Turtle
# from food import Food
# food = Food()

STARTING_BODY_COORDINATES = ((0,0), (-20,0), (-40,0))
DISTANCE = 20


class Snake():
    def __init__(self):
        self.snakelist = []
        self.create_snake()
        self.snakehead = self.snakelist[0]

    def create_snake(self):
        for coordinate in STARTING_BODY_COORDINATES:
            self.add_body(coordinate)

    def turn_left(self):
        if self.snakehead.heading() != 0:
            self.snakehead.seth(180)
    def turn_right(self):
        if self.snakehead.heading() != 180:
            self.snakehead.seth(0)
    def turn_up(self):
        if self.snakehead.heading() != 270:
            self.snakehead.seth(90)
    def turn_down(self):
        if self.snakehead.heading() != 90:
            self.snakehead.seth(270)

    def move_snake_head(self):
        self.snakehead.forward(20)
        self.move_body()

    def move_body(self):
        for segm_num in range(len(self.snakelist) -1 ,0,-1 ):
            self.snakelist[segm_num].goto(self.snakelist[segm_num-1].pos())
        self.snakehead.forward(20)

    def add_body(self, coordinate):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(coordinate)
        self.snakelist.append(new_segment)

    def check_collision(self):
        for segment in self.snakelist[2:]:
            if self.snakehead.distance(segment.pos()) < 20 :
                return True

    def reset_snake(self):
        self.send_snake()
        # self.clear()
        self.snakelist.clear()
        self.create_snake()
        self.snakehead = self.snakelist[0]

    def send_snake(self):
        for seg in self.snakelist:
            seg.goto(1000,1000)
