import dearpygui.dearpygui as dpg
from .constants import FONT_TAG, BEACH_IMAGE_TAG


class MyButton:
    def __init__(self, label):
        self.label = label
        self.count = 0
        dpg.add_button(label=label, callback=lambda s, d, u: self.callback(s, d, u))

    def callback(self, sender, app_data, user_data):
        self.count += 1
        dpg.configure_item(sender, label=f"{self.label} clicked {self.count} times")


def create_gui():
    with dpg.window():
        dpg.set_primary_window(dpg.last_item(), True)
        dpg.add_text("Hello world")
        dpg.add_button(label="Save")
        dpg.add_slider_float(width=200)
        dpg.add_image(BEACH_IMAGE_TAG)
        dpg.add_text("Hello world in a different font")
        dpg.bind_item_font(dpg.last_item(), FONT_TAG)
        MyButton("My button")
