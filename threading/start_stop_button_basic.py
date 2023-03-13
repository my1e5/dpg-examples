import time
import threading
import dearpygui.dearpygui as dpg
dpg.create_context()

running = False

def run_task():
    while running:
        print("Running...")
        time.sleep(1)

def start_stop_callback():
    global running
    if not running:
        print("Started")
        running = True
        thread = threading.Thread(target=run_task, args=(), daemon=True)
        thread.start()
        dpg.set_item_label(start_stop_button, "Stop")
    else:
        print("Stopped")
        running = False
        dpg.set_item_label(start_stop_button, "Start")

with dpg.window() as primary_window:
    dpg.add_text("Check the terminal for output")
    start_stop_button = dpg.add_button(label="Start", callback=start_stop_callback)

dpg.set_primary_window(primary_window, True)
dpg.create_viewport(width=300, height=200, title="Basic Start/Stop Button")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()