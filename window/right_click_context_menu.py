import dearpygui.dearpygui as dpg
import pyperclip # pip install pyperclip
dpg.create_context()

def right_click_context_menu(sender, app_data, user_data):
    def cut():
        pyperclip.copy(dpg.get_value(user_data))
        dpg.set_value(user_data, "")
        dpg.delete_item(popup)

    def copy():
        pyperclip.copy(dpg.get_value(user_data))
        dpg.delete_item(popup)

    def paste():
        data = dpg.get_value(user_data)
        dpg.set_value(user_data, data+pyperclip.paste())
        dpg.delete_item(popup)

    with dpg.window(popup=True, no_focus_on_appearing=False) as popup:
        dpg.add_button(label="Cut", callback=cut)
        dpg.add_button(label="Copy", callback=copy)
        dpg.add_button(label="Paste", callback=paste)

def add_text_box(default_value=""):
    text_input = dpg.add_input_text(multiline=True, default_value=default_value)
    with dpg.item_handler_registry() as registry:
        dpg.add_item_clicked_handler(button=dpg.mvMouseButton_Right, callback=right_click_context_menu, user_data=text_input)
    dpg.bind_item_handler_registry(text_input, registry)

with dpg.window() as primary_window:
    add_text_box("Right click me!")
    add_text_box("Right click me too!")

dpg.set_primary_window(primary_window, True)
dpg.create_viewport(width=400, height=300, title="Cut/Copy/Paste Context Menu")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()