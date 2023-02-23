# Credit to @Lucifer - https://discord.com/channels/736279277242417272/852624162396831744/1006905716205965393
import dearpygui.dearpygui as dpg
dpg.create_context()

# A child window cannot have an item clicked handler - you get this error:
# Item Type: mvAppItemType::mvChildWindow
# Message:   Item Handler Registry includes inapplicable handler: mvClickedHandler
# if you consult the source code you will see that mvAppItemType::mvChildWindow is not part of CanItemTypeBeClicked
# https://github.com/hoffstadt/DearPyGui/blob/1651e65a4ac8ecaf3bda5019f2d8c8106b371820/DearPyGui/src/ui/AppItems/mvAppItem.cpp#L466
# The solution is to use a global clicked handler and check if the child window is hovered.

def mouse_click_callback():
    if dpg.is_item_hovered(child_window):
        print(f"{child_window} was clicked!")

with dpg.handler_registry():
    dpg.add_mouse_click_handler(button=0, callback=mouse_click_callback)

with dpg.window(width=500, height=500):
    with dpg.child_window(width=200, height=200) as child_window:
        dpg.add_button(label="Button")
        dpg.add_slider_int()

dpg.create_viewport(width=600, height=600, title="Child Window Clicked Handler")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()