import json
import dearpygui.dearpygui as dpg
dpg.create_context()

STATE_FILENAME = "app-state-dict.json"

def save_state(state):
    with open(STATE_FILENAME, "w") as f:
        json.dump(state, f, indent=4)

def load_state():
    try:
        with open(STATE_FILENAME, "r") as f:
            state = json.load(f)
    except:
        state = {
            "name": "My App",
            "settings": {
                "foo": 0,
                "bar": "DPG is awesome!",
                "baz": 3.1415
            }
        }
    return state


state = load_state()

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)
    dpg.add_text(state["name"])
    dpg.add_slider_int(label="Foo", default_value=state["settings"]["foo"], callback=lambda s, d: state["settings"].__setitem__("foo", d))
    dpg.add_input_text(label="Bar", default_value=state["settings"]["bar"], callback=lambda s, d: state["settings"].__setitem__("bar", d))
    dpg.add_input_float(label="Baz", default_value=state["settings"]["baz"], callback=lambda s, d: state["settings"].__setitem__("baz", d))
    dpg.add_button(label="Print app state", callback=lambda: print(state))

dpg.create_viewport(title="App Persistence Demo using Dict", height=400, width=500)
dpg.setup_dearpygui()
dpg.show_viewport()
try:
    dpg.start_dearpygui()
finally:
    save_state(state)
    dpg.destroy_context()
