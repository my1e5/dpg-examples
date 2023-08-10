import time
import dearpygui.dearpygui as dpg
dpg.create_context()

def long_process():
    for i in range(10):
        time.sleep(1)
        dpg.add_button(label=f"Button {i}", parent=main_window)

def startup():
    with dpg.window(modal=True, no_move=True, no_close=True, no_title_bar=True, no_resize=True) as loading_window:
        dpg.add_text("Loading...")
        dpg.add_loading_indicator()
    long_process()
    dpg.delete_item(loading_window)

with dpg.window() as main_window:
    pass

dpg.set_frame_callback(1, startup)
dpg.set_primary_window(main_window, True)
dpg.create_viewport(width=800, height=600, title="Loading indicator on startup")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()