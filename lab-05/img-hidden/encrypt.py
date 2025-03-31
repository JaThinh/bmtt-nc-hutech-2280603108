import sys
from PIL import Image

def encode_image(image_path, message):
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: File '{image_path}' not found.")
        return
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    width, height = img.size
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '00000000'  # Ký tự kết thúc chuỗi

    data_index = 0
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))
            for color_channel in range(3):
                if data_index < len(binary_message):
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1
            img.putpixel((col, row), tuple(pixel))
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    encoded_image_path = "encode_image.png"
    img.save(encoded_image_path)
    print(f"Steganography complete. Encoded image saved as {encoded_image_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
    else:
        encode_image(sys.argv[1], sys.argv[2])
