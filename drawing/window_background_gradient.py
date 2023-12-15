# Credit @v-ein (see https://discord.com/channels/736279277242417272/1184967921051635883/1184967921051635883)
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(width=600, height=600)
dpg.setup_dearpygui()

with dpg.theme() as no_paddding_theme:
    with dpg.theme_component(dpg.mvWindowAppItem):
        dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 0, 0)

with dpg.window(label="tutorial", width=500, height=500) as wnd:
    dpg.bind_item_theme(dpg.last_item(), no_paddding_theme)

    dpg.draw_rectangle(
        (0, 0), (500, 500),
        color_bottom_right=(0, 0, 0),
        color_bottom_left=(0, 0, 0),
        color_upper_right=(128, 128, 160),
        color_upper_left=(128, 128, 192),
        color=(0, 0, 0, 0),
        multicolor=True,
        fill=True
    )
    with dpg.child_window(pos=(8, 28)):
        dpg.add_checkbox(label=dpg.get_dearpygui_version())
        dpg.add_button(label="Lorem ipsum", callback=lambda: print("dolor sit"))

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()