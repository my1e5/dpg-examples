# Using tables it is straightforward to implement layouts with horizontally adjustable containers.
# However, it is not possible to do the same vertically using tables. This is a quick experimental 
# implementation of a vertically adjustable separator using an image texture and a clicked handler. 
# It's not perfect and might be a bit buggy, but it might be useful for someone.
# Limitations - you have to click accurately on the separator to adjust it, it only adjusts the
# height of the child window above it, and the mouse cursor doesn't change to indicate that it is
# adjustable.

from itertools import chain
import dearpygui.dearpygui as dpg
dpg.create_context()

def adjustable_separator(child_window, width=3840, height=5, colour=(255, 255, 255, 50)):
    with dpg.texture_registry():
        data = list(chain.from_iterable([[c / 255 for c in colour] for _ in range(width*height)]))
        separator_texture = dpg.add_static_texture(width=width, height=height, default_value=data)
    separator = dpg.add_image(separator_texture)
    def clicked_callback():
        while dpg.is_mouse_button_down(0):
            y_pos = dpg.get_mouse_pos()[1]
            dpg.split_frame(delay=10)
            y_delta = y_pos - dpg.get_mouse_pos()[1]
            height = dpg.get_item_height(child_window) - y_delta
            if height < 1: height = 1
            dpg.configure_item(child_window, height=height)
    with dpg.item_handler_registry() as item_handler:
        dpg.add_item_clicked_handler(callback=clicked_callback)
    dpg.bind_item_handler_registry(item=separator, handler_registry=item_handler)

with dpg.window(height=500, width=600, no_scrollbar=True):
    with dpg.table(header_row=False, resizable=True):
        dpg.add_table_column(width_fixed=True, init_width_or_weight=200)
        dpg.add_table_column()
        with dpg.table_row():
            with dpg.child_window() as child_window_1:
                dpg.add_text("Child Window 1")
            with dpg.group():
                with dpg.child_window(height=200) as child_window_2:
                    dpg.add_text("Child Window 2")
                adjustable_separator(child_window_2)
                with dpg.child_window(height=100) as child_window_3:
                    dpg.add_text("Child Window 3")
                adjustable_separator(child_window_3)
                with dpg.child_window() as child_window_4:
                    dpg.add_text("Child Window 4")

dpg.create_viewport(title="Adjustable Separators", width=900, height=700)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()