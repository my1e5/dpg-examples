import dearpygui.dearpygui as dpg
dpg.create_context()

def plot_mouse_click_callback():
    x,y = dpg.get_plot_mouse_pos()
    dpg.add_scatter_series([x], [y], parent=yaxis) # different parent to the line series, makes it easy to delete all the points

with dpg.window():
    dpg.add_text("Right click on the plot to add a point.")
    with dpg.plot(no_menus=True, no_box_select=True) as plot: # note the no_menus and no_box_select, so right click doesn't do anything else
        xaxis = dpg.add_plot_axis(dpg.mvXAxis)
        yaxis = dpg.add_plot_axis(dpg.mvYAxis)
        dpg.add_line_series([0, 1], [0, 1], parent=xaxis)

    dpg.add_button(label="Delete last point", callback=lambda: dpg.delete_item(dpg.get_item_children(yaxis)[1][-1]) if len(dpg.get_item_children(yaxis)[1]) > 0 else None)
    dpg.add_button(label="Delete points", callback=lambda: dpg.delete_item(yaxis, children_only=True))
    dpg.add_button(label="Print points x,y data", callback=lambda: print([dpg.get_value(child)[0:2] for child in dpg.get_item_children(yaxis)[1]]))

with dpg.item_handler_registry() as registry:
    dpg.add_item_clicked_handler(button=dpg.mvMouseButton_Right, callback= plot_mouse_click_callback)
dpg.bind_item_handler_registry(plot, registry)


dpg.create_viewport(width=800, height=600, title="Plot with mouse click callback")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
