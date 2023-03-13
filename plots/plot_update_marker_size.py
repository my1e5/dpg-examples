import random
import dearpygui.dearpygui as dpg
dpg.create_context()

with dpg.theme() as plot_theme:
    with dpg.theme_component(dpg.mvScatterSeries):
        marker_size = dpg.add_theme_style(dpg.mvPlotStyleVar_MarkerSize, 1, category=dpg.mvThemeCat_Plots)

def change_marker_size(_, app_data):
    dpg.set_value(marker_size, [app_data])

with dpg.window():
    dpg.add_slider_int(label="Marker Size", min_value=1, max_value=10, default_value=1, callback=change_marker_size)
    with dpg.plot():
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis)
        with dpg.plot_axis(dpg.mvYAxis):
            for _ in range(3):
                dpg.add_scatter_series([random.random() for _ in range(10)],[random.random() for _ in range(10)])
                dpg.bind_item_theme(dpg.last_item(), plot_theme)

dpg.create_viewport(width=600, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()