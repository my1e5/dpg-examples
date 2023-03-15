# Credit @Tensor - https://discord.com/channels/736279277242417272/1068600047090016397/1070025491895029760
# Tested on Windows 11
# Check that you have "Transparency effects" enabled in Windows Settings

import ctypes

import dearpygui.dearpygui as dpg

import tools
from windoweffect import window_effect

dpg.create_context()
dpg.create_viewport(decorated=True, resizable=True, clear_color=[0, 0, 0, 0])
dpg.setup_dearpygui()


class MARGINS(ctypes.Structure):
    _fields_ = [
        ("cxLeftWidth", ctypes.c_int),
        ("cxRightWidth", ctypes.c_int),
        ("cyTopHeight", ctypes.c_int),
        ("cyBottomHeight", ctypes.c_int)
    ]


def removeBackground():
    margins = MARGINS(-1, -1, -1, -1)
    ctypes.windll.dwmapi.DwmExtendFrameIntoClientArea(tools.get_hwnd(), margins)


def restoreBackground():
    margins = MARGINS(0, 0, 0, 0)
    ctypes.windll.dwmapi.DwmExtendFrameIntoClientArea(tools.get_hwnd(), margins)


def removeBackgroundEffect():
    window_effect.removeBackgroundEffect(tools.get_hwnd())


def setAeroEffect():
    window_effect.setAeroEffect(tools.get_hwnd())


def setAcrylicEffect():
    gradientColor = list(map(lambda item: int(item), dpg.get_value('color_picker')))
    gradientColor = bytearray(gradientColor).hex().upper()
    enableShadow = dpg.get_value('enable_shadow')
    window_effect.setAcrylicEffect(tools.get_hwnd(), gradientColor=gradientColor, enableShadow=enableShadow)


def setMicaEffect():
    isDarkMode = dpg.get_value('is_dark_mode')
    window_effect.setMicaEffect(tools.get_hwnd(), isDarkMode=isDarkMode)


with dpg.window(label="Background Effect Test", height=500):
    dpg.add_checkbox(label="decorated", default_value=True, callback=lambda _, flag: dpg.set_viewport_decorated(flag))
    with dpg.group(horizontal=True):
        dpg.add_button(label="removeBackground (Transparency)", callback=removeBackground)
        dpg.add_button(label="Restore", callback=restoreBackground)
    dpg.add_button(label="removeBackgroundEffect", callback=removeBackgroundEffect)
    dpg.add_button(label="setAeroEffect", callback=setAeroEffect)
    with dpg.group(horizontal=True):
        dpg.add_button(label="setAcrylicEffect", callback=setAcrylicEffect)
        dpg.add_checkbox(label="enableShadow", default_value=False, tag="enable_shadow")
    with dpg.group(horizontal=True):
        dpg.add_button(label="setMicaEffect", callback=setMicaEffect)
        dpg.add_checkbox(label="isDarkMode", default_value=False, tag="is_dark_mode")
    dpg.add_color_picker(display_type=dpg.mvColorEdit_uint8, picker_mode=dpg.mvColorPicker_bar, alpha_bar=True, tag='color_picker')

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
