import dearpygui.dearpygui as dpg
dpg.create_context()

width, height, channels, data = dpg.load_image("beach.jpg")
with dpg.texture_registry():
    dpg.add_dynamic_texture(width, height, data, tag="mytexture")

with dpg.window() as primary_window:
    dpg.add_text("Resize the viewport to see the image resize.")
    dpg.add_image(texture_tag="mytexture", tag="myimage")

def resize_primary_window():
    x,y = dpg.get_item_rect_size(primary_window)
    dpg.set_item_height("myimage", y//3)
    dpg.set_item_width("myimage", x//3)

with dpg.item_handler_registry() as registry:
    dpg.add_item_resize_handler(callback=resize_primary_window)
dpg.bind_item_handler_registry(primary_window, registry)

dpg.set_primary_window(primary_window, True)
dpg.create_viewport(width=800, height=600, title="Resize Image With Viewport")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()