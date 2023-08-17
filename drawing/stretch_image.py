# Credit Quattro - https://github.com/QuattroMusic/Bots-Game/blob/main/src/DPG/textures.py
import dearpygui.dearpygui as dpg
dpg.create_context()


def stretch_image(data, width: int, height: int, stretch: int) -> tuple[int, int, list[int]]:
    res = [0 for _ in range(width * height * 4 * stretch * stretch)]
    dataValues = [data[i] for i in range(len(data))]

    for pixelIndex in range(len(dataValues) // 4):
        nIndex = ((pixelIndex % width) + ((pixelIndex - (pixelIndex % width)) // width) * width * stretch) * stretch
        for x in range(stretch):
            for y in range(stretch):
                res[(nIndex + x + (y * width * stretch)) * 4 + 0] = dataValues[(pixelIndex * 4) + 0]
                res[(nIndex + x + (y * width * stretch)) * 4 + 1] = dataValues[(pixelIndex * 4) + 1]
                res[(nIndex + x + (y * width * stretch)) * 4 + 2] = dataValues[(pixelIndex * 4) + 2]
                res[(nIndex + x + (y * width * stretch)) * 4 + 3] = dataValues[(pixelIndex * 4) + 3]

    return width * stretch, height * stretch, res


with dpg.window(width=500, height=500):

    width, height, channels, data = dpg.load_image("beach.jpg")
    width_stretched, height_stretched, data_stretched = stretch_image(data, width, height, 2)

    with dpg.texture_registry():
        dpg.add_static_texture(width, height, data, tag="beach_original")
        dpg.add_static_texture(width_stretched, height_stretched, data_stretched, tag="beach_stretched")

    dpg.add_image(texture_tag="beach_original", width=width, height=height)
    dpg.add_image(texture_tag="beach_stretched", width=width_stretched, height=height_stretched)



dpg.create_viewport(width=800, height=600, title="Stretch image by integer factor")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()