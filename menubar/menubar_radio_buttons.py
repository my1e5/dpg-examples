# Credit @v-ein - see https://discord.com/channels/736279277242417272/1178380567260180541/1178380567260180541
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Test', width=800, height=600)
dpg.setup_dearpygui()

with dpg.window(label="Radio menu", width=700, height=500) as wnd:
    with dpg.menu_bar():
        with dpg.menu(label="Examples"):
            dpg.add_menu_item(label="Save")
            with dpg.menu(label="Lang"):

                def on_sel_clicked(sender):
                    # reset the selectable to unselected state
                    dpg.set_value(sender, False)
                    # switch the radio button
                    dpg.set_value("lang-radio", dpg.get_item_label(sender))

                with dpg.theme() as nopad_theme:
                    with dpg.theme_component(dpg.mvAll):
                        dpg.add_theme_style(dpg.mvStyleVar_CellPadding, 4, 0)
                with dpg.theme() as sel_theme:
                    with dpg.theme_component(dpg.mvAll):
                        dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 0, 10)
                with dpg.table(header_row=False, policy=dpg.mvTable_SizingFixedFit):
                    dpg.bind_item_theme(dpg.last_item(), nopad_theme)

                    dpg.add_table_column()
                    dpg.add_table_column(init_width_or_weight=20)
                    with dpg.table_row():
                        with dpg.group(horizontal=True, horizontal_spacing=0):
                            dpg.add_text()
                            with dpg.group():
                                dpg.bind_item_theme(dpg.last_item(), sel_theme)
                                dpg.add_selectable(label="en_US",   span_columns=True, callback=on_sel_clicked, disable_popup_close=True)
                                dpg.add_selectable(label="en_GB",   span_columns=True, callback=on_sel_clicked, disable_popup_close=True)
                                dpg.add_selectable(label="cn",      span_columns=True, callback=on_sel_clicked, disable_popup_close=True)
                                dpg.add_selectable(label="jp",      span_columns=True, callback=on_sel_clicked, disable_popup_close=True)
                                dpg.add_selectable(label="whatnot", span_columns=True, callback=on_sel_clicked, disable_popup_close=True)
                        dpg.add_radio_button(("en_US", "en_GB", "cn", "jp", "whatnot"), tag="lang-radio")

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()