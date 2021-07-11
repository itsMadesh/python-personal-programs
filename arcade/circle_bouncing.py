import arcade
screen_width=600
screen_height=600
window_title="cirle bouncing"
radius=40
def draw(delta_time):
    arcade.start_render()
    arcade.draw_circle_filled(draw.center_x,draw.center_y,radius,arcade.color.AIR_FORCE_BLUE)
    draw.center_x+=draw.delta_x*delta_time
    draw.center_y+=draw.delta_y*delta_time

    if(draw.center_x < radius or draw.center_x > screen_width-radius):
        draw.delta_x*=-1
    if(draw.center_y < radius or draw.center_y > (screen_height-radius)
            or draw.center_y<300 ):
        draw.delta_y*=-1    
draw.center_x=300
draw.center_y=300
draw.delta_x=0
draw.delta_y=100
def main():
    arcade.open_window(screen_width,screen_height,window_title)
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(draw,1/80)
    arcade.run()
main()    