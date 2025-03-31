import sys
from PIL import Image

def decode_image(encoded_image_path):
    try:
        img = Image.open(encoded_image_path)
    except FileNotFoundError:
        print(f"Error: File '{encoded_image_path}' not found.")
        return None
    except Exception as e:
        print(f"Error opening image: {e}")
        return None

    width, height = img.size
    binary_message = ""

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for color_channel in range(3):
                binary_message += format(pixel[color_channel], '08b')[-1]

    message = ""
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))
        if char == '\0':  # Dừng khi gặp ký tự NULL
            break
        message += char

    return message if message else "No hidden message found."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
    else:
        decoded_message = decode_image(sys.argv[1])
        if decoded_message:
            print("Decoded message:", decoded_message)
