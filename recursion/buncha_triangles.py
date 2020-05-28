from turtle import *
color("blue")
beg_side_len = 400


def draw_tri(side_len):
    angle = 120
    for i in range(3):
        forward(side_len)
        left(angle)
   
# draw_tri(beg_side_len, 0)

# One iteration for a single quadrant:
def many_tris(side_len, counter):
    if counter == 3:
        return
    for i in range(3):
        # goto bottom left of tri
        if i == 2:
            right(180)
            forward(beg_side_len)
            right(120)
            forward(beg_side_len // 2)
            right(60)
            
        draw_tri(beg_side_len // 2)
        if i != 2:
            forward(beg_side_len // 2)
        counter += 1
    many_tris(side_len // 2, counter1)

many_tris(beg_side_len, 0)

exitonclick()

