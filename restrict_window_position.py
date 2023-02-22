import dearpygui.dearpygui as dpg
dpg.create_context()

def clamp(n, min_n, max_n):
    return max(min(max_n, n), min_n)

def drag_callback():
    if dpg.is_item_hovered(window) and dpg.get_value(checkbox):
        x, y = dpg.get_item_pos(window)
        w, h = dpg.get_item_rect_size(window)
        vw, vh = dpg.get_viewport_client_width(), dpg.get_viewport_client_height()
        cx, cy = clamp(x, 0, vw - w), clamp(y, 0, vh - h)
        if cx != x or cy != y:
            dpg.set_item_pos(window, (cx, cy))

with dpg.handler_registry():
    dpg.add_mouse_drag_handler(button=0, callback=drag_callback)

with dpg.window() as window:
    dpg.add_text("Drag this window to the\n edge of the viewport and\n it will not exceed the bounds")
    checkbox = dpg.add_checkbox(label="Restrict window", default_value=True)

dpg.create_viewport(width=800, height=600, title="Restrict Window Position")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()