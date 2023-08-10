import dearpygui.dearpygui as dpg
from itertools import chain
dpg.create_context()

GREY = [128/255, 128/255, 128/255, 255/255]
RED = [255/255, 0/255, 0/255, 255/255]
TRANSPARENT = [0, 0, 0, 0]
WIDTH = 50

def create_circle_texture(fill_level):
    data = []
    radius = WIDTH//2
    for x in range(0, WIDTH):
        for y in range(0, WIDTH):
            if (x-radius)**2 + (y-radius)**2 < radius**2:
                if (WIDTH-x)/WIDTH > fill_level/100:
                    data.append(GREY)
                else:
                    data.append(RED)
            else:
                data.append(TRANSPARENT)
    data = list(chain.from_iterable(data))
    return data

def update_circle(sender, app_data):
    data = create_circle_texture(app_data)
    dpg.set_value("circle_texture", data)
    
data = create_circle_texture(50)
with dpg.texture_registry():
    dpg.add_dynamic_texture(WIDTH, WIDTH, data, tag="circle_texture")

with dpg.window(width=400, height=400):
    dpg.add_image(texture_tag="circle_texture", width=WIDTH, height=WIDTH)
    dpg.add_slider_int(label="Grey/Red (%)", default_value=50, min_value=0, max_value=100, callback=update_circle)


dpg.create_viewport(width=800, height=600, title="Update dynamic texture")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()