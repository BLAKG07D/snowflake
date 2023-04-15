import turtle


def setup_Turtle():
    """ turtle setup"""
    t = turtle.Turtle()
    t.speed(0)
    turtle.bgcolor("white")
    t.pencolor("green")
    t.pensize(2)
    return t

def chain(t,length):
    """
    A method to create a chain
    """
    t.forward(length)


def slip_stitch(t,length):
    """
    A method to draw a 'slip-stitch'
    """
    t.penup()
    t.forward(length)
    t.pendown()

def draw_snowflake_point(t):
    t.right(60)
    slip_stitch(t,20)
    chain(t,20)
    t.right(120)
    slip_stitch(t,20)
    t.left(60)
    chain(t,10)
    t.left(60)

def draw_snowflake_center(t):
    for _ in range(6):
        draw_snowflake_point(t)

def draw_snowflake():
    t=setup_Turtle()
    t.penup()
    t.goto(0, 100)
    t.pendown()

    draw_snowflake_center(t)
    draw_snowflake_point(t)

if __name__ == "__main__":
    draw_snowflake()







