# Credit @Quattro - https://discord.com/channels/736279277242417272/1034823864104005703/1035630921166110780
import dearpygui.dearpygui as dpg
dpg.create_context()

DEFAULT_LINE_COLOUR = (0, 119, 200, 153)

with dpg.theme() as coloured_line_theme:
    with dpg.theme_component():
        coloured_line_component = dpg.add_theme_color(dpg.mvPlotCol_Line, DEFAULT_LINE_COLOUR, category=dpg.mvThemeCat_Plots)

def change_colour(_, rgba_values):
    dpg.set_value(coloured_line_component, [value*255 for value in rgba_values])

with dpg.window():
    with dpg.plot():
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis)
        with dpg.plot_axis(dpg.mvYAxis):
            for i in range(4):
                dpg.add_line_series([0, 1], [0, i+1], label=f"line{i}")
                dpg.bind_item_theme(dpg.last_item(), coloured_line_theme)

with dpg.window(pos=(450,0), width=300, height=300):
    dpg.add_color_picker(default_value=DEFAULT_LINE_COLOUR, callback=change_colour)

dpg.create_viewport(width=800, height=600, title="Plot Update Line Colour")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()