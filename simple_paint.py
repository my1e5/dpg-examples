import dearpygui.dearpygui as dpg
dpg.create_context()

with dpg.theme() as canvas_theme, dpg.theme_component():
    dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 0,0)
    dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (255,255,255,255))

def draw(_, app_data):
    x,y = dpg.get_mouse_pos()
    while dpg.is_mouse_button_down(button=dpg.mvMouseButton_Left):
        new_x,new_y = dpg.get_mouse_pos()
        if new_x != x or new_y != y:
            dpg.draw_line((x,y), (new_x,new_y), parent=app_data[1], color=dpg.get_value(color_picker), thickness=dpg.get_value(line_thickness))
            x,y = new_x,new_y

with dpg.window() as window:
    dpg.add_text("Click and drag to draw.")
    with dpg.group(horizontal=True):

        with dpg.child_window(width=500, height=500) as canvas:
            dpg.bind_item_theme(canvas, canvas_theme)
            drawlist = dpg.add_drawlist(width=500, height=500)
            with dpg.item_handler_registry() as registry:
                dpg.add_item_clicked_handler(button=dpg.mvMouseButton_Left, callback=draw)
            dpg.bind_item_handler_registry(drawlist, registry)

        with dpg.child_window(border=False):
            dpg.add_button(label="Clear Canvas", callback=lambda: dpg.delete_item(drawlist, children_only=True))
            line_thickness = dpg.add_slider_int(label="Line Thickness", width=200, default_value=2, min_value=1, max_value=3)
            color_picker = dpg.add_color_picker(width=200)

dpg.set_primary_window(window, True)
dpg.create_viewport(width=900, height=600, title="Simple Paint")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()