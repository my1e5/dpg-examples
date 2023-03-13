import dearpygui.dearpygui as dpg
dpg.create_context()

with dpg.theme() as button_clicked_theme:
    with dpg.theme_component():
        dpg.add_theme_color(dpg.mvThemeCol_Button, (255, 0, 0))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (225, 0, 0))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (205, 0, 0))


def toggle_button_colour(sender):
    if dpg.get_item_theme(sender) == button_clicked_theme:
        dpg.bind_item_theme(sender, None)
    else:
        dpg.bind_item_theme(sender, button_clicked_theme)

with dpg.window():
    dpg.add_button(label="Click me!", callback=toggle_button_colour)


dpg.create_viewport(width=800, height=600, title="Change button colour when clicked")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
