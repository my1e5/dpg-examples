import time
import threading
import dearpygui.dearpygui as dpg
dpg.create_context()

def add_start_stop_button(target: callable, parent: int | str = None, user_data: any = None):
    StartStopButton(target, parent, user_data)

class StartStopButton:
    def __init__(self, target: callable, parent: int | str = None, user_data: any = None):
        self.parent = parent or dpg.last_container()
        self.button = dpg.add_button(label="Start", parent=self.parent, callback=self.start_stop_callback)
        self.target = target
        self.user_data = user_data
        self.running = False

    def start_stop_callback(self):
        if not self.running:
            print(f"Started {self.user_data}")
            self.running = True
            thread = threading.Thread(target=self.target, args=(self,self.user_data), daemon=True)
            thread.start()
            dpg.set_item_label(self.button, "Stop")
        else:
            print(f"Stopped {self.user_data}")
            self.running = False
            dpg.set_item_label(self.button, "Start")

def run_task(self, user_data):
    while self.running:
        print(f"Running... {user_data}")
        time.sleep(1)

with dpg.window() as primary_window:
    dpg.add_text("Check the terminal for output")
    with dpg.group(horizontal=True):
        dpg.add_text("Task 1")
        add_start_stop_button(target=run_task, user_data="Task 1")
    with dpg.group(horizontal=True):
        dpg.add_text("Task 2")
        add_start_stop_button(target=run_task, user_data="Task 2")

dpg.set_primary_window(primary_window, True)
dpg.create_viewport(width=300, height=200, title="Multiple Start/Stop Buttons")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()