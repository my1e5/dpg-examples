import dearpygui.dearpygui as dpg
dpg.create_context()

GREY = [128, 128, 128]
RED = [255, 0, 0]

def update_circle(sender, app_data):
    scale = app_data/100
    r = (RED[0]-GREY[0])*scale + GREY[0]
    g = (RED[1]-GREY[1])*scale + GREY[1]
    b = (RED[2]-GREY[2])*scale + GREY[2]
    dpg.configure_item("circle", fill=[r,g,b], color=[r,g,b])

with dpg.window(width=400, height=400):
    dpg.draw_circle(center=[100, 100], radius=50, fill=RED, color=RED, tag="circle")
    dpg.add_slider_float(label="Grey/Red (%)", default_value=100, min_value=0, max_value=100, callback=update_circle)

dpg.create_viewport(width=800, height=600, title="Update fill colour")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()