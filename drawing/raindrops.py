from dataclasses import dataclass
import dearpygui.dearpygui as dpg
dpg.create_context()

@dataclass
class Raindrop:
    x: int
    y: int
    size: int
    color: tuple

raindrops = []


def update_raindrops(raindrops):
    dpg.delete_item(drawlist, children_only=True)
    speed_value = dpg.get_value(speed)
    raindrops = [raindrop for raindrop in raindrops if raindrop.y <= dpg.get_item_height(drawlist)]
    for raindrop in raindrops:
        dpg.draw_circle((raindrop.x,raindrop.y), raindrop.size, parent=drawlist, fill=raindrop.color, color=raindrop.color)
        raindrop.y += speed_value
    return raindrops
            

def create_raindrop():
    x,y = dpg.get_mouse_pos()
    raindrops.append(Raindrop(x,y,5,dpg.get_value(color_picker)))
    dpg.split_frame(delay=200)
    while dpg.is_mouse_button_down(button=dpg.mvMouseButton_Left):
        dpg.split_frame(delay=100)
        x,y = dpg.get_mouse_pos()
        raindrops.append(Raindrop(x,y,5,dpg.get_value(color_picker)))


with dpg.theme() as canvas_theme, dpg.theme_component():
    dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 0,0)

with dpg.window() as window:
    dpg.add_text("Click to create raindrops.")
    with dpg.group(horizontal=True):

        with dpg.child_window(width=500, height=500) as canvas:
            dpg.bind_item_theme(canvas, canvas_theme)
            drawlist = dpg.add_drawlist(width=500, height=500)
            with dpg.item_handler_registry() as registry:
                dpg.add_item_clicked_handler(button=dpg.mvMouseButton_Left, callback=create_raindrop)
            dpg.bind_item_handler_registry(drawlist, registry)

        with dpg.child_window(border=False):
            speed = dpg.add_slider_int(label="Speed", width=200, default_value=1, min_value=1, max_value=10)
            color_picker = dpg.add_color_picker(width=200, default_value=(0,0,255,255))
            dpg.add_button(label="print raindrops", callback=lambda: print(raindrops))

dpg.set_primary_window(window, True)
dpg.create_viewport(width=900, height=600, title="Raindrops")
dpg.setup_dearpygui()
dpg.show_viewport()
while dpg.is_dearpygui_running():
    raindrops = update_raindrops(raindrops)
    dpg.render_dearpygui_frame()
dpg.destroy_context()
