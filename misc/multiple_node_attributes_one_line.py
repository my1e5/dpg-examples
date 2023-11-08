# Credit v-ein - see https://discord.com/channels/736279277242417272/1171760109270073375/1171760109270073375
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=500, height=400)

dpg.setup_dearpygui()
with dpg.window(pos=(0, 30), width=500, height=350, no_title_bar=False):
    def on_delink(sender, link_item):
        link_info = dpg.get_item_configuration(link_item)
        node1 = link_info['attr_1']
        node2 = link_info['attr_2']
        print(f"Attempting to delete the link between nodes {node1} and {node2}")
        dpg.delete_item(link_item)

    def on_link(sender, app_data):
        dpg.add_node_link(app_data[0], app_data[1], parent=sender)

    with dpg.theme() as no_padding_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 0, 0) 
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 0, 0) 

    with dpg.node_editor(callback=on_link, 
                        delink_callback=on_delink, minimap=True, minimap_location=dpg.mvNodeMiniMap_Location_BottomRight):

        with dpg.node(label="Node 1", pos=[10, 10]):

            FONT_SIZE = 13
            ITEM_SPACING_Y = 4
            # ImNodes has a hardcoded frame padding for attributes, 1 pixel on each side
            ATTR_FRAME_PADDING = 1
            anchor = dpg.generate_uuid()
            target = dpg.generate_uuid()

            def adjust_position():
                dpg.set_item_pos(target, dpg.get_item_pos(anchor))

            with dpg.item_handler_registry() as move_handler:
                dpg.add_item_visible_handler(callback=adjust_position)

            # Offsetting the dots to the supposed middle of the line
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                # Can't get position of a spacer, so wrapping it into a group to get pos
                with dpg.group(tag=anchor):
                    dpg.bind_item_handler_registry(dpg.last_item(), move_handler)
                    # Instead of subtracting item spacing, one could set item 
                    # spacing to zero on the entire node, but that would affect
                    # other attributes, too.
                    dpg.add_spacer(height=(FONT_SIZE/2 + ATTR_FRAME_PADDING - ITEM_SPACING_Y ))

            # An empty, zero-height input attribute
            with dpg.node_attribute():
                dpg.bind_item_theme(dpg.last_item(), no_padding_theme)

            # An empty, zero-height output attribute
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output):
                dpg.bind_item_theme(dpg.last_item(), no_padding_theme)

            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                with dpg.group(horizontal=True, tag=target):
                    dpg.add_input_float(label="F3", width=80)
                    dpg.add_input_float(label="F4", width=80)

        with dpg.node(label="Node 2", pos=[300, 10]):

            with dpg.node_attribute() as na2:
                dpg.add_input_float(label="F3", width=100)

            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_input_float(label="F4", width=100)

dpg.show_viewport()
dpg.show_item_registry()
dpg.show_style_editor()
dpg.start_dearpygui()
dpg.destroy_context()