import json
from dataclasses import dataclass, field, asdict
import dearpygui.dearpygui as dpg
dpg.create_context()


@dataclass
class Settings:
    foo: int = 0
    bar: str = "DPG is awesome!"
    baz: float = 3.1415


@dataclass
class State:  # Store app state in a dataclass, which can include nested dataclasses
    name: str = "My App"
    settings: Settings = field(default_factory=Settings)

    def __post_init__(self):  
        if type(self.settings) is dict: # This will be a dict if loading from JSON, so need to convert it to a Settings object
            self.settings = Settings(**self.settings)


try:
    with open("app-state.json", "r") as f:
        state = State(**json.load(f))
except:
    state = State()


with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)
    dpg.add_text(state.name)
    dpg.add_slider_int(label="Foo", default_value=state.settings.foo, callback=lambda s, d: setattr(state.settings, "foo", d))
    dpg.add_input_text(label="Bar", default_value=state.settings.bar, callback=lambda s, d: setattr(state.settings, "bar", d))
    dpg.add_input_float(label="Baz", default_value=state.settings.baz, callback=lambda s, d: setattr(state.settings, "baz", d))
    dpg.add_button(label="Print app state", callback=lambda: print(state))


dpg.create_viewport(title="App Persistance Demo", height=400, width=500)
dpg.setup_dearpygui()
dpg.show_viewport()
try:
    dpg.start_dearpygui()
finally:
    with open("app-state.json", "w") as f:
        json.dump(asdict(state), f, indent=4)
    dpg.destroy_context()
