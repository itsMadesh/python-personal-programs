import arcade
width = 600
height = 600
screen_title = "Bouncing rectangle"

rect_width = 50
rect_height = 50


def on_draw(delta_time):
    global center_x, center_y, delta_x, delta_y
    arcade.start_render()
    arcade.draw_rectangle_filled(
        center_x, center_y, rect_width, rect_height, arcade.color.BLUE)
    center_x += delta_x * delta_time
    center_y += delta_y * delta_time
    if center_x < rect_width // 2 or center_x > width - rect_width // 2:
        delta_x *= -1
    if center_y < rect_height // 2 or center_y > height - rect_height // 2:
        delta_y *= -1


center_x = 300
center_y = 300
delta_x = 115
delta_y = 115


def main():
    arcade.open_window(width, height, screen_title)
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_draw, 0.001)
    arcade.run()


main()
