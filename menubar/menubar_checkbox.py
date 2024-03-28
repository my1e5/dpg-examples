# Credit @v-ein - https://discord.com/channels/736279277242417272/1219151962185142272/1219192226031210527
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Test", width=600, height=300)

def checkbox_menu_item(label: str, **kwargs):
    # This is what actually toggles the checkbox.  Because of this, we can't
    # use the checkbox's callback.  If you need a callback, add it as an argument
    # to `checkbox_menu_item`, and forward the call to it in on_selectable.
    def on_selectable(sender, app_data, user_data):
        dpg.set_value(sender, False)
        # user_data is our checkbox UUID
        dpg.set_value(user_data, not dpg.get_value(user_data))

    with dpg.group(horizontal=True, horizontal_spacing=0):
        selectable = dpg.add_selectable(disable_popup_close=True, callback=on_selectable)
        checkbox = dpg.add_menu_item(label=label, check=True, **kwargs)
    dpg.set_item_user_data(selectable, checkbox)

    # You can return a different widget if you need (e.g. the container or the selectable)
    return checkbox


# Create the main window
with dpg.window() as wnd:
    with dpg.menu_bar(parent=wnd):
        with dpg.menu(label="Test menu"):
            dpg.add_menu_item(label="Native menu item", check=True)
            checkbox_menu_item(label="Non-closing checkbox")
            checkbox_menu_item(label="Another non-closing")

    dpg.add_child_window(border=False, height=-30)  # offset the help message to the bottom
    dpg.add_text("Go into the menu and try to click every item")


dpg.setup_dearpygui()
dpg.set_primary_window(wnd, True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()