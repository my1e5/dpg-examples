# Credit @v-ein - https://discord.com/channels/736279277242417272/736279277242417275/1241101468631695513
from contextlib import suppress
from random import random, randrange
import textwrap
from typing import Any, Union
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Test", width=900, height=700)

class HexEditor:
    data: bytearray
    start_addr: int
    stride: int
    group_size: int
    encoding: str
    unprintable_trans: Any

    container: Union[int, str] = 0
    edit_completed_handler: Union[int, str] = 0
    click_handler: Union[int, str] = 0
    # Horizontal offset, in pixels, of the first byte from the start of the line
    first_byte_offset: float = 0.0

    def __init__(self,
            data: bytearray,
            start_addr: int = 0,
            stride: int = 16,
            group_size: int = 8,
            encoding: str ="iso8859-1",
            **kwargs) -> None:

        self.data = data
        self.start_addr = start_addr
        self.stride = stride
        self.group_size = group_size
        self.encoding = encoding

        self.unprintable_trans = str.maketrans({char_code: "." for char_code in range(0, 32)})

        # Now go create the UI
        self.create(**kwargs)

    def create(self, **kwargs) -> None:
        # Create the themes
        with dpg.theme() as main_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 4, 0)
                dpg.add_theme_style(dpg.mvStyleVar_CellPadding, 4, 0)
            with dpg.theme_component(dpg.mvInputText):
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 0, 0)

        # Create the handlers
        with dpg.item_handler_registry() as self.edit_completed_handler:
            dpg.add_item_edited_handler(callback=self.on_edit_change)
            dpg.add_item_deactivated_handler(callback=self.on_edit_deactivated)

        with dpg.item_handler_registry() as self.click_handler:
            dpg.add_item_clicked_handler(callback=self.on_byte_clicked)

        # Do some calculations
        self.first_byte_offset = dpg.get_text_size("0000: ")[0]

        # Now go create the content
        with dpg.table(
                header_row=False,
                borders_innerV=True,
                policy=dpg.mvTable_SizingFixedFit,
                no_host_extendX=True,
                **kwargs) as self.container:

            dpg.bind_item_theme(dpg.last_item(), main_theme)

            dpg.add_table_column()
            dpg.add_table_column()

            for line_ofs in range(0, len(self.data), self.stride):
                line_addr = self.start_addr + line_ofs
                line_bytes = self.data[line_ofs : line_ofs + self.stride]
                with dpg.table_row():
                    # The group provides us with a container to which we'll be
                    # adding absolutely-positioned edit fields
                    with dpg.group(horizontal=True, horizontal_spacing=0):
                        line = self.format_hex(line_bytes, line_addr)
                        dpg.add_text(line, user_data=line_addr)
                        dpg.bind_item_handler_registry(dpg.last_item(), self.click_handler)
                    dpg.add_text(self.format_text(line_bytes))

    def format_hex(self, line_bytes: bytes, line_addr: int) -> str:
        # `line_bytes` is only passed here for performance; we could get it from `self.data` as well.
        groups = [
            line_bytes[addr : addr + self.group_size].hex(" ", 1)
                for addr in range(0, self.stride, self.group_size)
        ]
        bytes_str = "  ".join(groups)
        # Note: the trailing space is specifically to allow input widgets some space
        # for the text cursor.
        return f"{line_addr:04X}: {bytes_str.upper()} "

    def format_text(self, line_bytes: bytes) -> str:
        # `line_bytes` is only passed here for performance; we could get it from `self.data` as well.
        return line_bytes.decode(self.encoding).translate(self.unprintable_trans)

    def on_byte_clicked(self, sender, app_data) -> None:
        widget = app_data[1]
        line_addr = dpg.get_item_user_data(widget)
        mouse_pos = dpg.get_mouse_pos(local=False)
        widget_pos = dpg.get_item_rect_min(widget)
        click_offset = mouse_pos[0] - widget_pos[0] - self.first_byte_offset
        group_width = dpg.get_text_size("00 " * self.group_size + " ")[0]
        clicked_group = click_offset // group_width
        # Adjusting for extra space between groups
        click_offset -= clicked_group * dpg.get_text_size(" ")[0]
        byte_width = dpg.get_text_size("00 ")[0]
        clicked_addr = line_addr + int(click_offset // byte_width)
        self.edit_byte(clicked_addr)

    def get_row_by_addr(self, addr: int) -> Union[int, str]:
        row_idx = (addr - self.start_addr) // self.stride
        return dpg.get_item_children(self.container, slot=1)[row_idx]

    def edit_byte(self, byte_addr: int) -> None:
        byte_ofs = byte_addr - self.start_addr
        byte_hex = self.data[byte_ofs : byte_ofs + 1].hex().upper()
        row = self.get_row_by_addr(byte_addr)
        # This gives us the group where the hex resides
        parent = dpg.get_item_children(row, slot=1)[0]
        widget_pos = dpg.get_item_pos(parent)
        byte_width = dpg.get_text_size("00 ")[0]
        byte_idx = byte_ofs % self.stride
        group_idx = byte_idx // self.group_size
        space_width = dpg.get_text_size(" ")[0]
        pos = (widget_pos[0] + self.first_byte_offset + byte_idx * byte_width + group_idx * space_width, widget_pos[1])
        dpg.add_input_text(
            default_value=byte_hex,
            hexadecimal=True,
            parent=parent,
            pos=pos,
            width=byte_width,
            callback=self.on_edit_completed,
            on_enter=True,
            user_data=(byte_addr, byte_hex))

        dpg.bind_item_handler_registry(dpg.last_item(), self.edit_completed_handler)
        dpg.focus_item(dpg.last_item())

    def commit_change(self, edit_widget: Union[int, str]) -> None:
        with dpg.mutex():
            byte_addr = dpg.get_item_user_data(edit_widget)[0]
            byte_ofs = byte_addr - self.start_addr
            byte_str = dpg.get_value(edit_widget)
            # Make sure we don't commit it again in the deactivated callback
            dpg.delete_item(edit_widget)
            with suppress(ValueError):
                self.data[byte_ofs] = int(byte_str[-2:], 16)
            # Now refresh the hex/text display
            line_ofs = byte_ofs - (byte_ofs % self.stride)
            line_bytes = self.data[line_ofs : line_ofs + self.stride]
            row = self.get_row_by_addr(byte_addr)
            cells = dpg.get_item_children(row, slot=1)
            line_widget = dpg.get_item_children(cells[0], slot=1)[0]
            dpg.set_value(line_widget, self.format_hex(line_bytes, line_ofs + self.start_addr))
            dpg.set_value(cells[1], self.format_text(line_bytes))
            # Edit next byte, if any
            if byte_addr < self.start_addr + len(self.data):
                self.edit_byte(byte_addr + 1)

    def on_edit_change(self, sender, widget) -> None:
        if len(dpg.get_value(widget)) >= 2:
            self.commit_change(widget)

    def on_edit_completed(self, sender, new_value, user_data) -> None:
        self.commit_change(sender)

    def on_edit_deactivated(self, sender, widget) -> None:
        # Unfortunately the deactivated handler gets called before the edit callback
        # in the same frame.  To properly detect and handle Enter, we need to delay
        # item deletion for one frame.  However, we can't use split_frame for this
        # because we need to give `on_edit_completed` a chance to run first.  That's
        # why we're delaying execution in such a weird way (also, 2 frames are
        # specified for stability reasons).
        with dpg.mutex():
            dpg.set_frame_callback(dpg.get_frame_count() + 2, self.handle_deactivated_event, user_data=widget)

    def handle_deactivated_event(self, frame, a, widget) -> None:
        if not dpg.does_item_exist(widget):
            # Nothing to do - already been committed and deleted
            return
        # Only committing if new value differs from the old one: this way we can
        # detect when Esc is pressed, and don't edit next byte.
        init_value = dpg.get_item_user_data(widget)[1]
        if dpg.get_value(widget) != init_value:
            self.commit_change(widget)
        dpg.delete_item(widget)


def add_hex_edit(
        data: bytearray,
        start_addr: int = 0xc000,
        stride: int = 16,
        group_size: int = 8,
        encoding: str ="iso8859-1",
        **kwargs) -> Union[int, str]:

    editor = HexEditor(data, start_addr, stride, group_size, encoding, **kwargs)
    return editor.container


def deferred_init():
    # Create the main window
    with dpg.window(label="RAM", height=300) as wnd:
        test_text = textwrap.dedent("""
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
            cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat
            non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.  
        """).strip().replace("\n", " ")
        test_bytes = bytes([(randrange(0, 256) if random() < 0.1 else 0) for i in range(0, 256)])
        test_data = bytearray(test_bytes + test_text.encode("iso8859-1"))

        add_hex_edit(test_data)

# Since the hex edit uses get_text_size, we have to wait 1 frame
dpg.set_frame_callback(1, callback=deferred_init)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.show_item_registry()
dpg.start_dearpygui()
dpg.destroy_context()