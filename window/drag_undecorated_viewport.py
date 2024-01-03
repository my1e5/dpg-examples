# Credit @v-ein - see https://discord.com/channels/736279277242417272/1191409079025930340/1191409079025930340
# see also drag_menu_bar.py
import dearpygui.dearpygui as dpg

dpg.create_context()

def drag_viewport(sender, app_data):
    FRAME_PADDING_Y = 3
    _, drag_dx, drag_dy = app_data

    # Note: at this point, the mouse has already moved off the starting point,
    # but to do a hit-test on the title bar, we need the starting point so we go
    # back to it.
    drag_start_y = dpg.get_mouse_pos(local=False)[1] - drag_dy
    title_bar_height = 2*FRAME_PADDING_Y + dpg.get_text_size("")[1]
    if drag_start_y < title_bar_height:  # only drag the viewport when dragging the title bar
        x_pos, y_pos = dpg.get_viewport_pos()

        # We're limiting the y position so that the viewport doesn't go off the top of the screen
        dpg.set_viewport_pos((x_pos + drag_dx, max(0, y_pos + drag_dy)))

with dpg.handler_registry():
    dpg.add_mouse_drag_handler(button=0, threshold=0.0, callback=drag_viewport)

window_title = "Test title bar"

with dpg.window(label=window_title, on_close=lambda: dpg.stop_dearpygui()) as wnd:
    dpg.add_text("Window contents goes here")

# Need the same title here as the title on dpg.window (otherwise the task bar
# will show a different... this can be used as a feature - to control the task bar
# separately :)).
dpg.create_viewport(title=window_title, width=400, height=300)
dpg.set_primary_window(wnd, True)
dpg.configure_item(wnd, no_title_bar=False)
dpg.set_viewport_decorated(False)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()