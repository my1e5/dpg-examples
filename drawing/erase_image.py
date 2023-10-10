import dearpygui.dearpygui as dpg
from math import sqrt
dpg.create_context()

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
ERASE_COLOUR = (0,0,0,0)

width, height, channels, data = dpg.load_image("beach.jpg")
with dpg.texture_registry():
    dpg.add_dynamic_texture(width, height, data, tag="beach")

with dpg.theme() as canvas_theme, dpg.theme_component():
    dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 0,0)

def erase():
    image_data = dpg.get_value("beach")
    radius = dpg.get_value(circle_thickness)
    while dpg.is_mouse_button_down(button=dpg.mvMouseButton_Left):
        mouse_x,mouse_y = dpg.get_mouse_pos()
        x = int(mouse_x/CANVAS_WIDTH * width)
        y = int(mouse_y/CANVAS_HEIGHT * height)

        for i in range(width):
            for j in range(height):
                distance = sqrt(((i / width) - (x / width))**2 + ((j / height) - (y / height))**2)
                if distance <= radius / max(width, height):
                    index = (j * width + i) * 4
                    image_data[index] = ERASE_COLOUR[0]
                    image_data[index + 1] = ERASE_COLOUR[1]
                    image_data[index + 2] = ERASE_COLOUR[2]
                    image_data[index + 3] = ERASE_COLOUR[3]
        
        dpg.set_value("beach", image_data)


def reset_image():
    dpg.set_value("beach", data)

with dpg.window() as window:
    dpg.add_text("Click and drag to erase.")
    with dpg.group(horizontal=True):

        with dpg.child_window(width=CANVAS_WIDTH, height=CANVAS_HEIGHT) as canvas:
            dpg.bind_item_theme(canvas, canvas_theme)
            
            with dpg.drawlist(width=CANVAS_WIDTH, height=CANVAS_HEIGHT) as drawlist:
                dpg.draw_image(texture_tag="beach", pmin=(0,0), pmax=(CANVAS_WIDTH,CANVAS_HEIGHT))
            
            with dpg.item_handler_registry() as registry:
                dpg.add_item_clicked_handler(button=dpg.mvMouseButton_Left, callback=erase)
            dpg.bind_item_handler_registry(drawlist, registry)

        with dpg.child_window(border=False):
            circle_thickness = dpg.add_slider_int(label="Circle Thickness", width=200, default_value=10, min_value=1, max_value=30)
            dpg.add_button(label="Reset image", callback=reset_image)
        

dpg.set_primary_window(window, True)
dpg.create_viewport(width=900, height=600, title="Erase image")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()