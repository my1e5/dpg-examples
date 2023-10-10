import dearpygui.dearpygui as dpg
from random import random
dpg.create_context()

def add_plot_data():
    dpg.add_scatter_series([random() for i in range(10)], [random() for i in range(10)], parent="x-axis")
    if dpg.does_item_exist("no_data_annotation"):
        dpg.delete_item("no_data_annotation")
        dpg.set_axis_limits_auto("x-axis") # unlock axis limits
        dpg.set_axis_limits_auto("y-axis")

def clear_plot():
    dpg.delete_item("x-axis", children_only=True)
    dpg.set_axis_limits("x-axis", 0, 1) 
    dpg.set_axis_limits("y-axis", 0, 1)
    if not dpg.does_item_exist("no_data_annotation"):
        dpg.add_plot_annotation(label="No Data Available", default_value=(0.5, 0.5), tag="no_data_annotation", parent="plot")

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)

    with dpg.group(horizontal=True):
        with dpg.child_window(width=200):
            dpg.add_button(label="Add plot data", callback=add_plot_data)
            dpg.add_button(label="Clear plot", callback=clear_plot)
        
        with dpg.plot(width=-1, height=-1, tag="plot"):
            dpg.add_plot_axis(dpg.mvXAxis, label="x-axis", tag="x-axis")
            dpg.add_plot_axis(dpg.mvYAxis, label="y-axis", tag="y-axis")
            dpg.set_axis_limits("x-axis", 0, 1) # lock axis limits so annotation is centered
            dpg.set_axis_limits("y-axis", 0, 1)
            dpg.add_plot_annotation(label="No Data Available", default_value=(0.5, 0.5), tag="no_data_annotation")
  
dpg.create_viewport(width=800, height=600, title="Plot text annotations")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
