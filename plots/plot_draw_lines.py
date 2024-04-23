import dearpygui.dearpygui as dpg
dpg.create_context()

def lock_axis(axis):
    xmin, xmax = dpg.get_axis_limits(axis)
    dpg.set_axis_limits(axis, xmin, xmax)

def unlock_axis(axis):
    dpg.set_axis_limits_auto(axis)

def plot_mouse_click_callback():
    if not dpg.get_value(drawing_mode):
        return
    lock_axis(xaxis), lock_axis(yaxis)
    dpg.delete_item(xaxis, children_only=True) # delete the previous line series

    x,y = dpg.get_plot_mouse_pos()
    data_x, data_y, lines = [x],[y],[]
    while dpg.is_mouse_button_down(button=0): #and dpg.is_key_down(dpg.mvKey_Control):
        new_x,new_y  = dpg.get_plot_mouse_pos()
        if new_x != x or new_y != y:
            if new_x < x: # only if the mouse is dragged left
                continue

            data_x.append(new_x), data_y.append(new_y)
            lines.append(dpg.draw_line([x,y], [new_x,new_y], parent=plot))
            x,y = new_x, new_y

    for line in lines: # delete the lines we just drew
        dpg.delete_item(line)
    # at this point you could do further processing on the data, e.g. smooth it.
    dpg.add_line_series(data_x, data_y, parent=xaxis) # add the data as a line series

    unlock_axis(yaxis), unlock_axis(xaxis)

with dpg.window():
    dpg.add_text("Left click and drag on the plot to add a line series.\nIt only works if you drag left to right.")
    drawing_mode = dpg.add_checkbox(label="Drawing mode", default_value=True)
    with dpg.plot(anti_aliased=True) as plot: 
        xaxis = dpg.add_plot_axis(dpg.mvXAxis)
        yaxis = dpg.add_plot_axis(dpg.mvYAxis)
        dpg.set_axis_limits(xaxis, 0, 100)
        dpg.set_axis_limits(yaxis, 0, 100)

    with dpg.item_handler_registry() as registry:
        dpg.add_item_clicked_handler(button=dpg.mvMouseButton_Left, callback=plot_mouse_click_callback)
    dpg.bind_item_handler_registry(plot, registry)

dpg.create_viewport(width=800, height=600, title="Plot with mouse click callback")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
