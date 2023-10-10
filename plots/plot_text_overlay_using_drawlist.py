import dearpygui.dearpygui as dpg
from random import random
dpg.create_context()

def add_plot_data():
    dpg.add_scatter_series([random() for i in range(10)], [random() for i in range(10)], parent="x-axis")
    dpg.hide_item("overlay_text")

def clear_plot():
    dpg.delete_item("x-axis", children_only=True)
    dpg.show_item("overlay_text")

with dpg.window(tag="primary_window"):
    dpg.set_primary_window(dpg.last_item(), True)

    with dpg.group(horizontal=True):
        with dpg.child_window(width=200):
            dpg.add_button(label="Add plot data", callback=add_plot_data)
            dpg.add_button(label="Clear plot", callback=clear_plot)
        
        with dpg.plot(width=-1, height=-1, tag="plot"):
            dpg.add_plot_axis(dpg.mvXAxis, label="x-axis", tag="x-axis")
            dpg.add_plot_axis(dpg.mvYAxis, label="y-axis", tag="y-axis")

def set_overlay_text_position():
    x,y = dpg.get_item_pos("plot")
    w,h = dpg.get_item_rect_size("plot")
    x_offset = -38 # needs a little manual adjustment to center
    y_offset = -25
    dpg.configure_item("overlay_text", pos=(x + w/2 + x_offset, y + h/2 + y_offset))

with dpg.viewport_drawlist():
    dpg.draw_text(pos=(100, 100), text="No Data Available", size=13, tag="overlay_text")

with dpg.item_handler_registry() as registry:
    dpg.add_item_resize_handler(callback=set_overlay_text_position)
dpg.bind_item_handler_registry("primary_window", registry) 


dpg.create_viewport(width=800, height=600, title="Plot text using drawlist overlay")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
