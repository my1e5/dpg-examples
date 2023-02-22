import time
import threading
import dearpygui.dearpygui as dpg
dpg.create_context()

running = False
paused = False
progress = 0

def run_task():
    global running
    global paused
    global progress
    print("Running...")
    
    for i in range(1,101):
        while paused:
            time.sleep(0.1)
        if not running:
            return
        progress = i
        print(i)
        dpg.set_value(progress_bar, 1/100 * (i))
        dpg.configure_item(progress_bar, overlay=f"{i}%")
        time.sleep(0.05)

    print("Finished")
    running = False
    dpg.set_item_label(start_pause_resume_button, "Finished")
    dpg.disable_item(start_pause_resume_button)
    dpg.show_item(reset_button)

def start_stop_callback():
    global running
    global paused
    if not running:
        print("Started")
        running = True
        paused = False
        thread = threading.Thread(target=run_task, args=(), daemon=True)
        thread.start()
        dpg.set_item_label(start_pause_resume_button, "Pause")
    else:
        if not paused:
            print("Paused...")
            paused = True
            dpg.set_item_label(start_pause_resume_button, "Resume")
            dpg.show_item(reset_button)
            return
        print("Resuming...")
        paused = False
        dpg.set_item_label(start_pause_resume_button, "Pause")
        dpg.hide_item(reset_button)

def reset_callback():
    global running
    global paused
    global progress
    running = False
    paused = False
    progress = 0
    dpg.set_value(progress_bar, 0)
    dpg.configure_item(progress_bar, overlay="0%")
    dpg.set_item_label(start_pause_resume_button, "Start")
    dpg.enable_item(start_pause_resume_button)
    dpg.hide_item(reset_button)

with dpg.window() as primary_window:
    with dpg.group(horizontal=True):
        start_pause_resume_button = dpg.add_button(label="Start", width=70, callback=start_stop_callback)
        reset_button = dpg.add_button(label="Reset", width=70, callback=reset_callback)
        dpg.hide_item(reset_button)
    progress_bar = dpg.add_progress_bar(default_value=0, width=-1, overlay="0%")

dpg.set_primary_window(primary_window, True)
dpg.create_viewport(width=400, height=300, title="Progress Bar with Pause/Resume")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()