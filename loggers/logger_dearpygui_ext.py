# from https://github.com/hoffstadt/DearPyGui_Ext/issues/4
# requires dearpygui_ext to be installed - see https://github.com/hoffstadt/DearPyGui_Ext
import dearpygui.dearpygui as dpg
import dearpygui.demo as demo
from dearpygui_ext.logger import mvLogger

dpg.create_context()
dpg.create_viewport()

log = mvLogger()
log.log("log")
log.log_debug("log debug")
log.log_info("log info")
log.log_warning("log warning")
log.log_error("log error")
log.log_critical("log critical")

demo.show_demo()

with dpg.window(label="tutorial", width=500, height=500, show=False):
    dpg.add_button(label="Press me", callback=lambda:dpg.toggle_viewport_fullscreen())

# main loop
dpg.show_viewport()
dpg.setup_dearpygui()
dpg.start_dearpygui()
dpg.destroy_context()