import dearpygui.dearpygui as dpg
dpg.create_context()

with dpg.window(label="Background Window", width=200, height=200, no_bring_to_front_on_focus=True):
    dpg.add_button(label="Open info window", callback=lambda: dpg.show_item(info_window))

with dpg.window(label="Info", show=False) as info_window:
    dpg.add_text("I'm always on top")

dpg.create_viewport(width=400, height=300, title="Window Always On Top")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()