# from https://discord.com/channels/736279277242417272/1085585441757077514/1085585441757077514
import dearpygui.dearpygui as dpg
dpg.create_context()

with dpg.colormap_registry():
    dpg.add_colormap([(255, 50, 50), (50, 50, 255)], False, tag='colormap')

WINDOW_PADDING_X = 8 # default window padding
ITEM_SPACING_X = 8 # default item spacing
COLORMAP_WIDTH = 75

plots = []

def add_new_plot():
    with dpg.group(horizontal=True, parent=plot_group):
        with dpg.plot(height=-1, width=-1) as plot:
            plots.append(plot)
            dpg.add_plot_axis(dpg.mvXAxis, label="x")
            y_axis = dpg.add_plot_axis(dpg.mvYAxis, label="y")
        dpg.add_colormap_scale(min_scale=0, max_scale=1, width=COLORMAP_WIDTH, height=-1, colormap='colormap')
        dpg.bind_colormap(plot, 'colormap')
    resize_plots()

def resize_plots():
    n_plots = len(plots)
    plot_width = (dpg.get_item_width(window) - WINDOW_PADDING_X*2 - ITEM_SPACING_X*(n_plots-1)) //n_plots
    for plot in plots:
        dpg.configure_item(plot, width=(plot_width - COLORMAP_WIDTH - ITEM_SPACING_X))

with dpg.window(width=450, height=550) as window:
    dpg.add_button(label="add new plot", callback=add_new_plot)
    with dpg.group(horizontal=True) as plot_group:
        add_new_plot()
     
with dpg.item_handler_registry() as item_handler_registry:
    dpg.add_item_resize_handler(callback=resize_plots)
dpg.bind_item_handler_registry(window, item_handler_registry)

dpg.create_viewport(title='Plots with colormap sizing', width=1200, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()