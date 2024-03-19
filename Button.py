import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.button_x = 400
        self.button_y = 300
        self.button_width = 200
        self.button_height = 50
        self.button_text = "Restart"
        self.is_button_pressed = False

        self.button_x1 = 400
        self.button_y1 = 240
        self.button_text1 = "Back"
        self.is_button_pressed1 = False

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(
            "Game Over",
            self.button_width+200,
            self.button_height+300,
            arcade.color.WHITE,
            30,
            anchor_x="center",
        )
        # Рисуем кнопку
        arcade.draw_rectangle_filled(self.button_x, self.button_y,
                                     self.button_width, self.button_height,
                                     arcade.color.LIGHT_GRAY)
        arcade.draw_text(self.button_text, self.button_x - 43, self.button_y - 10,
                         arcade.color.BLACK, font_size=20)
        arcade.draw_rectangle_filled(self.button_x1, self.button_y1,
                                     self.button_width, self.button_height,
                                     arcade.color.LIGHT_GRAY)
        arcade.draw_text(self.button_text1, self.button_x1 - 30, self.button_y1 - 10,
                         arcade.color.BLACK, font_size=20)

    def on_mouse_press(self, x, y, button, modifiers):
        if (self.button_x - self.button_width / 2 < x < self.button_x + self.button_width / 2 and
                self.button_y - self.button_height / 2 < y < self.button_y + self.button_height / 2):
            self.is_button_pressed = True
        if (self.button_x1 - self.button_width / 2 < x < self.button_x1 + self.button_width / 2 and
                self.button_y1 - self.button_height / 2 < y < self.button_y1 + self.button_height / 2):
            self.is_button_pressed1 = True

    def on_mouse_release(self, x, y, button, modifiers):
        if self.is_button_pressed:
            print("Кнопка нажата!")
            self.is_button_pressed = False
        if self.is_button_pressed1:
            print("BACK")
            self.is_button_pressed1 = False


def main():
    window = MyGame(800, 600, "Button Example")
    arcade.run()


if __name__ == "__main__":
    main()
