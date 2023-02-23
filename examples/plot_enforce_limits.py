import dearpygui.dearpygui as dpg
from math import sin
dpg.create_context()

data_x = [i for i in range(200)]
data_y = [0.5 + 0.5 * sin(50 * i / 1000) for i in data_x]
    
Y_MAX = 1
Y_MIN = 0
X_MAX = 200
X_MIN = 0

def enforce_plot_limits(sender, app_data, user_data):
    plot, xaxis, yaxis = user_data
    while dpg.is_mouse_button_down(button=dpg.mvMouseButton_Left) or dpg.is_item_hovered(plot):
        xmin, xmax = dpg.get_axis_limits(xaxis)
        if xmin < X_MIN:
            xmin = X_MIN
            dpg.set_axis_limits(xaxis, xmin, xmax)
        if xmax > X_MAX:
            xmax = X_MAX
            dpg.set_axis_limits(xaxis, xmin, xmax)
        dpg.split_frame()
        dpg.set_axis_limits_auto(xaxis)

        ymin, ymax = dpg.get_axis_limits(yaxis)
        if ymin < Y_MIN:
            ymin = Y_MIN
            dpg.set_axis_limits(yaxis, ymin, ymax)
        if ymax > Y_MAX:
            ymax = Y_MAX
            dpg.set_axis_limits(yaxis, ymin, ymax)
        dpg.split_frame()
        dpg.set_axis_limits_auto(yaxis)

with dpg.window():
    with dpg.plot(height=400, width=500) as plot:
        xaxis = dpg.add_plot_axis(dpg.mvXAxis, label="x")
        yaxis = dpg.add_plot_axis(dpg.mvYAxis, label="y")
        dpg.add_line_series(data_x, data_y, parent=yaxis)
        
        with dpg.item_handler_registry() as item_handler_registry:
            dpg.add_item_hover_handler(user_data = (plot, xaxis, yaxis), callback=enforce_plot_limits)
        dpg.bind_item_handler_registry(plot, item_handler_registry)

dpg.create_viewport(width=900, height=600, title='Plot Enforce Limits')
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()