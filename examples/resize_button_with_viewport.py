import dearpygui.dearpygui as dpg
from itertools import chain
dpg.create_context()

texture_data = list(chain.from_iterable([(1, 0, 1, 1) for _ in range(100 * 100)]))
with dpg.texture_registry():
    pink_square = dpg.add_static_texture(width=100, height=100, default_value=texture_data)

with dpg.window() as primary_window:
    dpg.add_text("Resize the viewport to see the button resize.")
    image_button = dpg.add_image_button(pink_square)

def resize_primary_window():
    x,y = dpg.get_item_rect_size(primary_window)
    dpg.set_item_height(image_button, y//10)
    dpg.set_item_width(image_button, x//10)

with dpg.item_handler_registry() as registry:
    dpg.add_item_resize_handler(callback=resize_primary_window)
dpg.bind_item_handler_registry(primary_window, registry)

dpg.set_primary_window(primary_window, True)
dpg.create_viewport(width=800, height=600, title="Resize Button With Viewport")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()