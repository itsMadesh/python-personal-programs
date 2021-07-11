import arcade
from arcade.window_commands import start_render
arcade.open_window(600,600,"heart")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
# for i in range(0,601,100):
#     arcade.draw_line(0,i,600,i,arcade.color.BLACK,3)
# for j in range(0,601,50):
#     arcade.draw_line(j,0,j,600,arcade.color.BLACK,3)
   
arcade.draw_arc_filled(200,400,200,200,arcade.color.RED_DEVIL,0,190)    
arcade.draw_arc_filled(400,400,200,200,arcade.color.RED_DEVIL,-190,0,180)
arcade.draw_line(300,100,100,390,arcade.color.RED_DEVIL)
arcade.draw_line(300,100,500,390,arcade.color.RED_DEVIL)
arcade.draw_triangle_filled(300,100,200,400,400,400,arcade.color.RED_DEVIL)
arcade.draw_triangle_filled(300,100,100,390,200,400,arcade.color.RED_DEVIL)
arcade.draw_triangle_filled(300,100,400,400,500,390,arcade.color.RED_DEVIL)
arcade.finish_render()
arcade.run()