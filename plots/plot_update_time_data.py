import dearpygui.dearpygui as dpg
import math
import time
import random
from collections import deque
dpg.create_context()

DEQUE_MAX_LEN = 200
data_x = deque(maxlen=DEQUE_MAX_LEN)
data_y = deque(maxlen=DEQUE_MAX_LEN)

def generate_data():
    data_x.append(time.time())
    data_y.append(math.sin(data_x[-1]) + random.uniform(-0.1, 0.1))
    return list(data_x), list(data_y)

def update_plot():
    updated_data_x, updated_data_y = generate_data()
    dpg.configure_item('line', x=updated_data_x, y=updated_data_y)
    if dpg.get_value("auto_fit_checkbox"):
        dpg.fit_axis_data("xaxis")

with dpg.window():
    with dpg.plot(height=400, width=500):
        dpg.add_plot_axis(dpg.mvXAxis, label="Time", tag="xaxis", time=True, no_tick_labels=True)
        dpg.add_plot_axis(dpg.mvYAxis, label="Amplitude", tag="yaxis")
        dpg.add_line_series([], [], tag='line', parent="yaxis")
        dpg.set_axis_limits("yaxis", -1.5, 1.5)
    dpg.add_checkbox(label="Auto-fit x-axis limits", tag="auto_fit_checkbox", default_value=True)

dpg.create_viewport(width=900, height=600, title='Updating plot data')
dpg.setup_dearpygui()
dpg.show_viewport()
while dpg.is_dearpygui_running():
    update_plot() # updating the plot directly from the running loop
    dpg.render_dearpygui_frame()
dpg.destroy_context()