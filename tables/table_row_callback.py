# Select table row and get data callback
# from https://github.com/DataExplorerUser/tools
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(width=800, height=450)
dpg.setup_dearpygui()

with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvTable):
        dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (255, 0, 0, 100), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (0, 0, 0, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Header, (0, 0, 0, 0), category=dpg.mvThemeCat_Core)

dpg.bind_theme(global_theme)


def clb_selectable(sender, app_data, user_data):
    print(f"Row {user_data}")


with dpg.window(tag="Table"):
    with dpg.table(header_row=True, callback=lambda: print("callback!!!")):
        dpg.add_table_column(label="First")
        dpg.add_table_column(label="Second")
        dpg.add_table_column(label="Third")

        for i in range(20):
            with dpg.table_row():
                for j in range(3):
                    dpg.add_selectable(label=f"Row{i} Column{j}", span_columns=True, callback=clb_selectable, user_data=i)

dpg.show_viewport()
dpg.set_primary_window("Table", True)
dpg.start_dearpygui()
dpg.destroy_context()