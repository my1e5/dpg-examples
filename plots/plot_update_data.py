import dearpygui.dearpygui as dpg
dpg.create_context()

M = 1
C = 0

def generate_data(m: float, c: float):
    data_x, data_y = [], []
    for x in range(0, 100):
        data_x.append(x)
        data_y.append(m*x + c)
    return data_x, data_y

def update_plot():
    data_x, data_y = generate_data(dpg.get_value("m_slider"), dpg.get_value("c_slider"))
    dpg.configure_item('line', x=data_x, y=data_y)
    if dpg.get_value("auto_fit_checkbox"):
        dpg.fit_axis_data("xaxis")
        dpg.fit_axis_data("yaxis")

with dpg.window(pos=(10,10)):
    with dpg.plot(label="y = mx + c", height=400, width=500):
        dpg.add_plot_axis(dpg.mvXAxis, label="x", tag="xaxis")
        dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="yaxis")
        data_x, data_y = generate_data(M, C)
        dpg.add_line_series(data_x, data_y, tag='line', parent="yaxis")
        
    dpg.add_slider_float(label="m", tag="m_slider", default_value=M, min_value=0, max_value=10, callback=update_plot)
    dpg.add_slider_float(label="c", tag="c_slider", default_value=C, min_value=-50, max_value=50, callback=update_plot)
    dpg.add_checkbox(label="Auto-fit axis limits", tag="auto_fit_checkbox", default_value=False)

dpg.create_viewport(width=900, height=600, title='Updating plot data')
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()