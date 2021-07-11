import arcade 
from arcade import Texture  

def draw_point(x, y):
    arcade.draw_point(x, y, arcade.color.RED, 5)


def draw_points(x, y):
    a = [[0, 0], [0, 0], [0, 0]]
    for i in range(0, 3, 1):
        k = i*10
        for j in range(0, 2, 1):
            if(j == 0):
                a[i][j] = x
            else:
                a[i][j] = y+k
    print(a)
    arcade.draw_points(a, arcade.color.RED_DEVIL, 5)
    # arcade.draw_point(x,y+i,arcade.color.RED,10)
    # arcade.draw_point(x+30,y+i,arcade.color.RED,10)
    # i=i+30


def draw_line(x, y):
    arcade.draw_line(x, y, x, y+90, arcade.color.BLUE, 5)


def draw_lines(x, y):
    a = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    for i in range(0, 6, 1):
        k = i+1
        for j in range(0, 2, 1):
            if(k % 2 != 0):
                if(j == 0):
                    a[i][j] = x
                else:
                    y += 20*j
                    a[i][j] = y
            else:
                if(j == 0):
                    a[i][j] = x+60
                else:
                    a[i][j] = y
    print(a)
    arcade.draw_lines(a, arcade.color.BLUE, 5)


def draw_line_strip(x, y):
    a = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    for i in range(0, 6, 1):
        k = i+1
        for j in range(0, 2, 1):
            if(k % 2 != 0):
                if(j == 0):
                    a[i][j] = x
                else:
                    y += 20*j
                    a[i][j] = y
            else:
                if(j == 0):
                    a[i][j] = x+60
                else:
                    a[i][j] = y
    print(a)
    arcade.draw_line_strip(a, arcade.color.COOL_BLACK, 5)


def draw_polygon_outline(x, y):
    a = [[x, y], [x+30, y], [x+45, y+10],
         [x+45, y+40-10], [x+30, y+40], [x, y+40]]
    arcade.draw_polygon_outline(a, arcade.color.ALLOY_ORANGE, 5)


def draw_polygon_filled(x, y):
    a = [[x, y], [x+30, y], [x+45, y+10],
         [x+45, y+40-10], [x+30, y+40], [x, y+40]]
    arcade.draw_polygon_filled(a, arcade.color.ALLOY_ORANGE)


def draw_circle_outline(x, y):
    arcade.draw_circle_outline(x, y, 50, arcade.color.AQUA, 4)


def draw_circle_filled(x, y):
    arcade.draw_circle_filled(x, y, 50, arcade.color.AQUA)


def draw_ellipse_outline(x, y):
    arcade.draw_ellipse_outline(x, y,50,30,arcade.color.BLACK,2,45)



def draw_ellipse_filled(x, y):
    arcade.draw_ellipse_filled(x, y,50,30,arcade.color.BABY_PINK, 45)
def draw_arc_outline(x,y):
    arcade.draw_arc_outline(x,y,50,100,arcade.color.BLUE,0,360) 
def draw_arc_filled(x,y):
    arcade.draw_arc_filled(x,y,40,50,arcade.color.BLUE,0,90)
def draw_rect_outline(x,y):
    arcade.draw_rectangle_outline(x,y,40,50,arcade.color.APPLE_GREEN,5)
    # arcade.draw_rectangle_outline(x+40,y,40,50,arcade.color.APPLE_GREEN,5)

def draw_rect_filled(x,y):
    arcade.draw_rectangle_filled(x,y,40,50,arcade.color.ARMY_GREEN)               
    arcade.draw_rectangle_filled(x,y+60,40,50,arcade.color.ARMY_GREEN)               
def draw_bitmap():
    texture=arcade.load_texture("personal/arcade/images/ss.PNG")
    scale=.2

    arcade.draw_scaled_texture_rectangle(540,100,texture,scale,0)
    arcade.draw_scaled_texture_rectangle(540,150,texture,scale,0)



def main():
    arcade.open_window(600, 600, 'PRIMITIVE')
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()
    # Draw column
    for column in range(0, 601, 120):
        arcade.draw_line(column, 0, column, 600, arcade.color.BLACK, 2)
    # Draw row
    for row in range(0, 601, 200):
        arcade.draw_line(0, row, 600, row, arcade.color.BLACK, 2)
    arcade.draw_text("draw_point", 0, 405, arcade.color.BLACK, 10)
    arcade.draw_text("draw_points", 120, 405, arcade.color.BLACK, 10)
    arcade.draw_text("draw_line", 240, 405, arcade.color.BLACK, 10)
    arcade.draw_text("draw_lines", 360, 405, arcade.color.BLACK, 10)
    arcade.draw_text("draw_line_strip", 480, 405, arcade.color.BLACK, 10)
    arcade.draw_text("draw_polygon_outline", 0, 205, arcade.color.BLACK, 10)
    arcade.draw_text("draw_polygon_filled", 120, 205, arcade.color.BLACK, 10)
    arcade.draw_text("draw__circle_outline", 240, 205, arcade.color.BLACK, 10)
    arcade.draw_text("draw_circle_filled", 360, 205, arcade.color.BLACK, 10)
    arcade.draw_text("draw_ellipse_outline", 480, 205, arcade.color.BLACK, 10)
    arcade.draw_text("draw_ellipse_filled", 0, 5, arcade.color.BLACK, 10)
    arcade.draw_text("draw_arc_outline", 120, 5, arcade.color.BLACK, 10)
    arcade.draw_text("draw_rect_outline", 240, 5, arcade.color.BLACK, 10)
    arcade.draw_text("draw_rect_filled", 360, 5, arcade.color.BLACK, 10)
    arcade.draw_text("draw_bitmap", 480, 5, arcade.color.BLACK, 10)
    draw_point(60, 500)
    draw_points(160, 490)
    draw_points(180, 490)
    draw_line(300, 500)
    draw_lines(380, 500)
    draw_line_strip(500, 500)
    draw_polygon_outline(30, 250)
    draw_polygon_filled(150, 250)
    draw_circle_outline(300, 300)
    draw_circle_filled(420, 300)
    draw_ellipse_outline(540,300)
    draw_ellipse_filled(60,100)
    draw_arc_outline(180,100)
    draw_arc_filled(195,150)
    draw_rect_outline(280,100)
    draw_rect_filled(420,100)
    draw_bitmap()
    arcade.finish_render()
    arcade.run()


main()
