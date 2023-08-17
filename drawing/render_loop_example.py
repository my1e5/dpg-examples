import dearpygui.dearpygui as dpg
import random
dpg.create_context()

CANVAS_SIZE = 300

width, height, channels, data = dpg.load_image("beach.jpg")
with dpg.texture_registry(show=True):
    dpg.add_static_texture(width, height, data, tag="beach")


def update_circle():
    x = random.randint(0, CANVAS_SIZE)
    y = random.randint(0, CANVAS_SIZE)
    dpg.configure_item("circle", center=(x,y))
    
    
with dpg.window(width=400, height=400):
    dpg.set_primary_window(dpg.last_item(), True)

    with dpg.drawlist(width=CANVAS_SIZE, height=CANVAS_SIZE):
        dpg.draw_image(texture_tag="beach", pmin=(0,0), pmax=(width,height))
        dpg.draw_circle((100,100), 10, fill=(255,0,0), tag="circle")
   

dpg.create_viewport(width=800, height=600, title="Render loop example")
dpg.setup_dearpygui()
dpg.show_viewport()
while dpg.is_dearpygui_running():
    update_circle()
    dpg.render_dearpygui_frame()
dpg.destroy_context()