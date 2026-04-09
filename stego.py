from PIL import Image
import io

HEADER = "STEGO>>>"
FOOTER = "<<<STEGO"

def hide_message(image_bytes, message):
    img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    full = HEADER + message + FOOTER
    msg_bytes = full.encode('utf-8')
    length = len(msg_bytes)
    payload = length.to_bytes(4, 'big') + msg_bytes
    binary = ''.join(format(b, '08b') for b in payload)
    pixels = list(img.getdata())

    if len(binary) > len(pixels) * 3:
        raise ValueError("Message too long! Please use a larger image.")

    new_pixels = []
    idx = 0
    for pixel in pixels:
        r, g, b = pixel
        if idx < len(binary):
            r = (r & ~1) | int(binary[idx]); idx += 1
        if idx < len(binary):
            g = (g & ~1) | int(binary[idx]); idx += 1
        if idx < len(binary):
            b = (b & ~1) | int(binary[idx]); idx += 1
        new_pixels.append((r, g, b))

    new_img = Image.new('RGB', img.size)
    new_img.putdata(new_pixels)

    output = io.BytesIO()
    new_img.save(output, format='PNG')
    output.seek(0)
    return output


def reveal_message(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    pixels = list(img.getdata())

    binary = ''
    for pixel in pixels:
        for channel in pixel:
            binary += str(channel & 1)

    all_bytes = []
    for i in range(0, len(binary) - 7, 8):
        all_bytes.append(int(binary[i:i+8], 2))

    if len(all_bytes) < 4:
        raise ValueError("No hidden message found!")

    length = int.from_bytes(bytes(all_bytes[:4]), 'big')

    if length <= 0 or length > len(all_bytes) - 4:
        raise ValueError("No hidden message found in this image!")

    try:
        text = bytes(all_bytes[4:4+length]).decode('utf-8')
    except:
        raise ValueError("No hidden message found in this image!")

    if HEADER not in text or FOOTER not in text:
        raise ValueError("No hidden message found in this image!")

    start = text.index(HEADER) + len(HEADER)
    end = text.index(FOOTER)
    return text[start:end]