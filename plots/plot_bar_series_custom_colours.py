import dearpygui.dearpygui as dpg
dpg.create_context()


with dpg.theme() as blue_theme:
    with dpg.theme_component():
        dpg.add_theme_color(
            dpg.mvPlotCol_Fill, (0, 119, 200, 255), category=dpg.mvThemeCat_Plots
        )

with dpg.theme() as red_theme:
    with dpg.theme_component():
        dpg.add_theme_color(
            dpg.mvPlotCol_Fill, (210, 4, 45, 255), category=dpg.mvThemeCat_Plots
        )

with dpg.theme() as yellow_theme:
    with dpg.theme_component():
        dpg.add_theme_color(
            dpg.mvPlotCol_Fill, (253, 218, 13, 255), category=dpg.mvThemeCat_Plots
        )


with dpg.window():
    with dpg.plot():
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis)
        with dpg.plot_axis(dpg.mvYAxis):
            dpg.add_bar_series([10, 20, 30], [30, 75, 90], label="Foo", weight=1)
            dpg.bind_item_theme(dpg.last_item(), blue_theme)
            dpg.add_bar_series([11, 21, 31], [45, 65, 72], label="Bar", weight=1)
            dpg.bind_item_theme(dpg.last_item(), red_theme)
            dpg.add_bar_series([12, 22, 32], [20, 85, 80], label="Baz", weight=1)
            dpg.bind_item_theme(dpg.last_item(), yellow_theme)


dpg.create_viewport(width=800, height=600, title="Bar Series Custom Colours")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
