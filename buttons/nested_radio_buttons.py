import dearpygui.dearpygui as dpg
dpg.create_context()

buttons = {
    "1": {"checked": True, "nested": {"1a":False, "1b":True, "1c":False, "1d":False}},
    "2": {"checked": False, "nested": {}},
    "3": {"checked": False, "nested": {"3a":True}},
}

def checkbox_callback(sender):
    for button in buttons.keys():
        if not button == sender:
            buttons[button]["checked"] = False
            dpg.set_value(button, False)
        else:
            buttons[button]["checked"] = True
            if not dpg.get_value(sender):
                dpg.set_value(sender, True)

def radio_button_callback(sender):
    for nested_button in buttons[sender.split("_")[0]]["nested"].keys():
        buttons[sender.split("_")[0]]["nested"][nested_button] = False
    buttons[sender.split("_")[0]]["nested"][dpg.get_value(sender)] = True

with dpg.window():
    for button, values in buttons.items():
        dpg.add_checkbox(
            tag=button,
            label=button,
            default_value=values["checked"],
            callback=checkbox_callback,
        )
        if values["nested"]:
            dpg.add_radio_button(
                tag=button + "_nested",
                items=list(values["nested"].keys()),
                indent=24,
                callback=radio_button_callback,
            )
            for nested_button, nested_values in values["nested"].items():
                if nested_values:
                    dpg.set_value(button + "_nested", nested_button)

    dpg.add_spacer(height=20)
    dpg.add_button(label="Print buttons state", callback=lambda: print(buttons))


dpg.create_viewport(width=800, height=600, title="Nested Radio Buttons Demo")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
