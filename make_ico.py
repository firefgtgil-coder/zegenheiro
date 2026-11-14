import struct

# Create a valid 16x16 uncompressed 32-bit RGBA ICO file
# ICO Header: 2 bytes reserved (0), 2 bytes type (1 for ICO), 2 bytes image count (1)
ico_header = struct.pack('<HHH', 0, 1, 1)

width = 16
height = 16
# Colors: Fire Red (#DC2626 -> B=38, G=38, R=220, A=255) and Gold (#F59E0B -> B=11, G=158, R=245, A=255)
# BMP InfoHeader: 40 bytes
# biHeight in ICO is double the height (height*2) because it contains XOR mask + AND mask
bmp_header = struct.pack('<IiiHHIIiiII', 40, width, height * 2, 1, 32, 0, width * height * 4, 0, 0, 0, 0)

xor_mask = bytearray()
for y in range(height):
    for x in range(width):
        # Draw a firefighter helmet shape
        # Crown at center, brim at bottom
        dx = abs(x - 7.5)
        dy = 15 - y  # y=0 is bottom in BMP
        if dy >= 3 and dy <= 12 and dx <= (10 - dy*0.6):
            if dy >= 6 and dx <= 2:
                # Gold crest
                xor_mask.extend([11, 158, 245, 255])
            else:
                # Fire red
                xor_mask.extend([38, 38, 220, 255])
        elif dy < 3 and dx <= 7:
            # Dark brim
            xor_mask.extend([30, 41, 59, 255])
        else:
            # Transparent
            xor_mask.extend([0, 0, 0, 0])

# AND mask: 1 bit per pixel, 16 pixels = 2 bytes per row, padded to 4 bytes per row
and_mask = bytearray([0x00, 0x00, 0x00, 0x00] * height)

img_data = bmp_header + bytes(xor_mask) + bytes(and_mask)

# Directory Entry: width, height, colors(0), reserved(0), planes(1), bpp(32), size, offset
dir_entry = struct.pack('<BBBBHHII', width, height, 0, 0, 1, 32, len(img_data), 6 + 16)

with open(r"C:\Users\firef\.gemini\antigravity\scratch\zegenheiro-landing-page\assets\favicon.ico", "wb") as f:
    f.write(ico_header + dir_entry + img_data)

print("favicon.ico generated successfully!")

