# Credit @v-ein https://discord.com/channels/736279277242417272/1207174250604011520/1207260729560793129

from contextlib import contextmanager
from typing import Generator, Optional, Tuple, Union
import dearpygui.dearpygui as dpg

dpg.create_context()

dpg.create_viewport(title="Test", width=600, height=600)

dpg.setup_dearpygui()
dpg.show_viewport()

#===============================================================================

with dpg.window(label="Tree nodes", width=200, height=150):
    with dpg.tree_node(label="Root", default_open=True):
        dpg.add_text("Lorem")
        with dpg.tree_node(label="Branch", default_open=True):
            dpg.add_button(label="ipsum")
            dpg.add_tree_node(label="Leaf", leaf=True)

#===============================================================================

with dpg.window(label="Headers", width=200, height=150, pos=(200, 0)):

    with dpg.theme() as tree_like_theme:
        with dpg.theme_component(dpg.mvCollapsingHeader):
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 4, 0)

    with dpg.collapsing_header(label="Root", default_open=True):
        dpg.bind_item_theme(dpg.last_item(), tree_like_theme)
        with dpg.group(indent=20):
            dpg.add_text("Lorem")
            with dpg.collapsing_header(label="Branch", default_open=True):
                with dpg.group(indent=20):
                    dpg.add_button(label="ipsum")
                    dpg.add_collapsing_header(label="Leaf", leaf=True)

#===============================================================================

@contextmanager
def colored_tree_node(label: str, color: Optional[Tuple[int, ...]] = None, leaf: bool = False, **kwargs) -> Generator[Union[int, str], None, None]:
    # We use a separate group to adjust padding, so that the header itself can be
    # customized further by binding a theme directly to it.
    with dpg.group():
        dpg.bind_item_theme(dpg.last_item(), "tree-node-theme")
        with dpg.collapsing_header(label=label, leaf=leaf, indent=(21 if leaf else 0), **kwargs) as node:
            if color:
                with dpg.theme() as color_theme:
                    with dpg.theme_component(dpg.mvCollapsingHeader):
                        dpg.add_theme_color(dpg.mvThemeCol_Header, color)
                        # note: you can add colors for active/hovered, too, e.g. blend them with white
                dpg.bind_item_theme(node, color_theme)
            # We need one more group in order to provide indentation AND to reset padding back to normal.
            # Indent in a normal tree node is determined by dpg.mvStyleVar_IndentSpacing,
            # which defaults to 21.
            with dpg.group(indent=21):
                dpg.bind_item_theme(dpg.last_item(), "default-padding")
                yield node

with dpg.window(label="Wrappers", width=200, height=150, pos=(400, 0)):

    with dpg.theme(tag="tree-node-theme") as tree_like_theme:
        with dpg.theme_component(dpg.mvCollapsingHeader):
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 4, 0)
            # We need the default color here so that nested headers don't pick up
            # the parent's color.
            dpg.add_theme_color(dpg.mvThemeCol_Header, (51, 51, 55, 255))

    with dpg.theme(tag="default-padding"):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 4, 3)

    with colored_tree_node(label="Root", default_open=True) as root:
        dpg.add_text("Lorem")
        with colored_tree_node(label="Branch", default_open=True, color=(192, 0, 0)):
            dpg.add_button(label="ipsum")
            with colored_tree_node(label="Leaf", leaf=True):
                pass


dpg.start_dearpygui()
dpg.destroy_context()