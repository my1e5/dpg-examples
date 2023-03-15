import json
import dearpygui.dearpygui as dpg
dpg.create_context()

try:
    previous_state = None
    with open("app-state.json", "r") as f:
        previous_state = json.load(f)
except:
    pass
state = {"windows": {}}   

def create_new_window(sender, app_data, user_data):
    def delete_window(sender):
        del state["windows"][sender]
    tag = dpg.generate_uuid()
    width, height, pos, text, slider = user_data if user_data else (200,50,(10,10),'', 0)
    with dpg.window(width=width, height=height, pos=pos, tag=tag, on_close=delete_window):
        state["windows"][tag] = {}
        state["windows"][tag]["text"] = dpg.add_input_text(hint="Enter text here", default_value=text)
        state["windows"][tag]["slider"] = dpg.add_slider_float(default_value=slider)

with dpg.window(width=200):
    dpg.add_button(label="Create new window", callback=create_new_window)
    dpg.add_text("Move the new windows around, resize them, enter some text, and move the slider. Then close the app and reopen it.", wrap=190)

if previous_state:
    for values in previous_state["windows"].values():
        create_new_window(None, None, (values["width"], values["height"], values["pos"], values["text"], values["slider"]))
    
dpg.create_viewport(title="Persistence of Windows Demo", height=700, width=1200)
dpg.setup_dearpygui()
dpg.show_viewport()
try:
    dpg.start_dearpygui()
finally:
    for tag, values in state["windows"].items():
        values["pos"] = dpg.get_item_pos(tag)
        values["width"] = dpg.get_item_width(tag)
        values["height"] = dpg.get_item_height(tag)
        values["text"] = dpg.get_value(values["text"])
        values["slider"] = dpg.get_value(values["slider"])
    with open("app-state.json", "w") as f:
        json.dump(state, f, indent=4)
    dpg.destroy_context()
