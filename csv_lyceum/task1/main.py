with open("input.bmp", "rb") as file:
    headers = file.read(54)
    pixels = file.read()

    with open("res.bmp", "wb") as file_to_write:
        file_to_write.write(headers)
        file_to_write.write(bytes([255 - pix for pix in pixels]))
