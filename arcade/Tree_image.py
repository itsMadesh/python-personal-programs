import arcade
def draw_tree(x,y):
    i=0
    while(i<100):
        arcade.draw_triangle_filled(x+50,y+150,x,y+i-100,x+100,y+i-100,arcade.color.DARK_GREEN)
        arcade.draw_lrtb_rectangle_filled(x+40,x+60,y-100,y-140,arcade.color.ZINNWALDITE_BROWN)
        i=i+20

def draw_bird(x,y):
    arcade.draw_arc_outline(x,y,30,30,arcade.color.BLACK,0,90)
    arcade.draw_arc_outline(x+30,y,30,30,arcade.color.BLACK,90,180)

def main():
    arcade.open_window(600,600,"Tree")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()
    arcade.draw_lrtb_rectangle_filled(0,600,300,0,arcade.color.GO_GREEN)
    draw_tree(50,200)
    draw_tree(200,200)
    draw_tree(350,200)
    draw_tree(500,200)
    draw_tree(0,350)
    draw_tree(150,350)
    draw_tree(300,350)
    draw_tree(450,350)
    draw_bird(50,500)
    draw_bird(300,500)
    draw_bird(550,500)
    draw_bird(210,550)
    draw_bird(410,550)
    arcade.finish_render()
    arcade.run()
main()
