#!/usr/bin/env python3
import struct
import zlib
from pathlib import Path


WIDTH = 960
HEIGHT = 720
TRANSPARENT = (0, 0, 0, 0)


def make_canvas():
    return [[TRANSPARENT for _ in range(WIDTH)] for _ in range(HEIGHT)]


def set_px(canvas, x, y, color):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        canvas[y][x] = color


def fill_rect(canvas, x, y, w, h, color):
    for yy in range(y, y + h):
        for xx in range(x, x + w):
            set_px(canvas, xx, yy, color)


def fill_circle(canvas, cx, cy, r, color):
    rr = r * r
    for yy in range(cy - r, cy + r + 1):
        for xx in range(cx - r, cx + r + 1):
            dx = xx - cx
            dy = yy - cy
            if dx * dx + dy * dy <= rr:
                set_px(canvas, xx, yy, color)


def draw_scaled_sprite(canvas, sprite, ox, oy, scale, palette):
    for sy, row in enumerate(sprite):
        for sx, key in enumerate(row):
            if key == ".":
                continue
            fill_rect(canvas, ox + sx * scale, oy + sy * scale, scale, scale, palette[key])


def encode_png(canvas):
    raw = bytearray()
    for row in canvas:
        raw.append(0)
        for r, g, b, a in row:
            raw.extend((r, g, b, a))

    def chunk(tag, data):
        return (
            struct.pack(">I", len(data))
            + tag
            + data
            + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
        )

    png = bytearray(b"\x89PNG\r\n\x1a\n")
    ihdr = struct.pack(">IIBBBBB", WIDTH, HEIGHT, 8, 6, 0, 0, 0)
    png.extend(chunk(b"IHDR", ihdr))
    png.extend(chunk(b"IDAT", zlib.compress(bytes(raw), 9)))
    png.extend(chunk(b"IEND", b""))
    return bytes(png)


def main():
    canvas = make_canvas()

    palette = {
        "K": (20, 22, 28, 255),
        "R": (215, 80, 64, 255),
        "S": (245, 132, 86, 255),
        "P": (255, 198, 123, 255),
        "C": (88, 225, 221, 255),
        "Y": (255, 229, 120, 255),
        "W": (250, 244, 236, 255),
        "B": (69, 108, 196, 255),
        "G": (130, 184, 128, 255),
    }

    sprite = [
        ".......................",
        "..........KKK..........",
        "........KKRRRKK........",
        ".......KRRSSSRRK.......",
        "......KRRSSSSSRRK......",
        ".....KRRRKKKSSSRRK.....",
        "....KRRKKCCC KSSRRK....".replace(" ", "."),
        "...KRRKCCCCC CCKSRRK...".replace(" ", "."),
        "..KRRKCCWWWCWWCKSRRK...".replace(" ", "."),
        "..KRRKCCCCC CCCKSRRK...".replace(" ", "."),
        "..KRRRKCCCCC CKKRRK....".replace(" ", "."),
        "..KRRRRKKK KKKRRRRK....".replace(" ", "."),
        ".KRRSSSRRKKKRRSSSRRK...",
        ".KRRSSSSRRRRRSSSSRRK...",
        ".KRRSSSSSRRRSSSSSRRK...",
        ".KRRSSSSSSRRSSSSSSRK...",
        ".KRRSSSSSSSSSSSSSSRK...",
        ".KRRRSSSSSSSSSSSRRRK...",
        "..KRRRRRRRRRRRRRRRK....",
        "...KRRRRRRRRRRRRRK.....",
        "....KRRSRRRRRRSRK......",
        "...KRR..KRRRK..RRK.....",
        "..KRR...KRRRK...RRK....",
        "..KR....KRRRK....RK....",
        "........KRRRK..........",
        ".......KRK.KRK.........",
        "......KRK...KRK........",
        ".....KRK.....KRK.......",
        "....KK.........KK......",
    ]

    scale = 20
    ox = 250
    oy = 80
    draw_scaled_sprite(canvas, sprite, ox, oy, scale, palette)

    # Left card frame
    fill_rect(canvas, 120, 240, 150, 190, palette["K"])
    fill_rect(canvas, 136, 256, 118, 158, palette["W"])
    fill_rect(canvas, 154, 282, 82, 20, palette["B"])
    fill_rect(canvas, 154, 318, 82, 12, palette["C"])
    fill_rect(canvas, 154, 346, 82, 12, palette["C"])
    fill_rect(canvas, 154, 374, 58, 12, palette["Y"])
    fill_rect(canvas, 190, 418, 24, 48, palette["K"])
    fill_rect(canvas, 166, 438, 72, 16, palette["G"])

    # Right stamp
    fill_rect(canvas, 735, 280, 110, 110, palette["K"])
    fill_rect(canvas, 750, 295, 80, 80, palette["Y"])
    fill_rect(canvas, 768, 313, 44, 44, palette["R"])
    fill_rect(canvas, 786, 244, 8, 48, palette["K"])
    fill_rect(canvas, 770, 226, 40, 24, palette["K"])

    # Chest badge
    fill_rect(canvas, 438, 386, 86, 58, palette["K"])
    fill_rect(canvas, 448, 396, 66, 38, palette["C"])
    fill_circle(canvas, 481, 415, 10, palette["Y"])
    fill_rect(canvas, 475, 403, 12, 24, palette["K"])
    fill_rect(canvas, 469, 409, 24, 12, palette["K"])

    out = Path("output/openclaw-shrimpcard.png")
    out.write_bytes(encode_png(canvas))
    print(f"[OK] Wrote {out}")


if __name__ == "__main__":
    main()
