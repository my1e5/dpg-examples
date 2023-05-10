# https://discord.com/channels/736279277242417272/1105417341560438844/1105420268287033375
import dearpygui.dearpygui as dpg
dpg.create_context()

def dpg_screenshot():
    dpg.output_frame_buffer('screenshot.png')

with dpg.window(width=200, height=200):
    dpg.add_button(label='Screenshot', callback=dpg_screenshot)

dpg.create_viewport(width=400, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()