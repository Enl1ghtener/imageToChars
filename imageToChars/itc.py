from PIL import Image

ascii_char = list("$@%8&#?<>=*+-,. ")

def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return " "
    length = len(ascii_char)
    gray = 0.2126 * r + 0.7152 * g + 0.0722 * b
    unit = 256 / length
    if int(gray / unit) > (length - 7):
        return ascii_char[int(gray / unit)] + "    "
    else:
        return ascii_char[int(gray / unit)] + "   "


def get_new_img(img_path="", image_size=3):
    # When the parameter 'image_size' is set to 5, image is the original size.
    # When the parameter 'image_size' is too large, the image will be distorted
    image = Image.open(img_path)
    width, height = image.size
    print(f"图片原始的宽和高为:{width},{height}")
    if not width or not height:
        pass
    else:
        width = int(width / 5)
        height = int(height / 5)
    width *= image_size
    height *= image_size
    image = image.resize((width, height), Image.ANTIALIAS)
    return image


def size_control(image, horizontal_stretching=1, longitudinal_stretching=1):
    # Stretch parameter takes 0 to 1
    # Images will reduce accuracy in the stretching direction
    width, height = image.size
    width = int(horizontal_stretching * width)
    height = int(longitudinal_stretching * height)
    image = image.resize((width, height), Image.ANTIALIAS)
    return image


def get_str_img(image):
    width, height = image.size  # 获取图片的宽和高
    chars = ""
    for i in range(height):
        for j in range(width):
            chars += get_char(*image.getpixel((j, i)))
        chars += "\n"
    return chars


def print_chars(chars, print_on_terminal=True, output_file_name=None):
    # When the parameter 'print_flag' is set to TURE, the program will directly print the result and will not write
    chars = get_str_img(chars)
    if print_on_terminal:
        print(chars)
    else:
        if output_file_name:
            with open(output_file_name, "w") as file:
                file.write(chars)
        else:
            with open("./output.txt", "w") as file:
                file.write(chars)


def run(img_path, image_size=5, horizontal_stretching=1, longitudinal_stretching=1):
    img = get_new_img(img_path, image_size)
    img = size_control(img, horizontal_stretching, longitudinal_stretching)
    print_chars(img, print_on_terminal=False, output_file_name="")
