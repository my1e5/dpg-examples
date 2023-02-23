# Credit to @Quattro - https://discord.com/channels/736279277242417272/761721971129843712/1005966507114758224
import dearpygui.dearpygui as dpg
dpg.create_context()

def auto_align(item, alignment_type: int, x_align: float = 0.5, y_align: float = 0.5):
    def _center_h(_s, _d, data):
        parent = dpg.get_item_parent(data[0])
        while dpg.get_item_info(parent)['type'] != "mvAppItemType::mvWindowAppItem":
            parent = dpg.get_item_parent(parent)
        parent_width = dpg.get_item_rect_size(parent)[0]
        width = dpg.get_item_rect_size(data[0])[0]
        new_x = (parent_width // 2 - width // 2) * data[1] * 2
        dpg.set_item_pos(data[0], [new_x, dpg.get_item_pos(data[0])[1]])

    def _center_v(_s, _d, data):
        parent = dpg.get_item_parent(data[0])
        while dpg.get_item_info(parent)['type'] != "mvAppItemType::mvWindowAppItem":
            parent = dpg.get_item_parent(parent)
        parent_width = dpg.get_item_rect_size(parent)[1]
        height = dpg.get_item_rect_size(data[0])[1]
        new_y = (parent_width // 2 - height // 2) * data[1] * 2
        dpg.set_item_pos(data[0], [dpg.get_item_pos(data[0])[0], new_y])

    if 0 <= alignment_type <= 2:
        with dpg.item_handler_registry():
            if alignment_type == 0:
                # horizontal only alignment
                dpg.add_item_visible_handler(callback=_center_h, user_data=[item, x_align])
            elif alignment_type == 1:
                # vertical only alignment
                dpg.add_item_visible_handler(callback=_center_v, user_data=[item, y_align])
            elif alignment_type == 2:
                # both horizontal and vertical alignment
                dpg.add_item_visible_handler(callback=_center_h, user_data=[item, x_align])
                dpg.add_item_visible_handler(callback=_center_v, user_data=[item, y_align])

        dpg.bind_item_handler_registry(item, dpg.last_container())

with dpg.window():
    item = dpg.add_button(label="I'm a button!")
    auto_align(item, 2, x_align=0.5, y_align=0.5)

dpg.create_viewport(width=600, height=600, title="Spacing Using Auto Align")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()