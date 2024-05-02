import imageToChars

if __name__ == '__main__':
    # When the parameter 'image_size' is set to 5, image is the original size.
    # When the parameter 'image_size' is too large, the image will be distorted
    img = imageToChars.get_new_img(img_path="./test_images/image.png", image_size=3)
    # Stretch parameter takes 0 to 1
    # Images will reduce accuracy in the stretching direction
    img = imageToChars.size_control(img, horizontal_stretching=1, longitudinal_stretching=1)
    # When the parameter 'print_flag' is set to TURE, the program will directly print the result and will not write
    imageToChars.print_chars(img, print_on_terminal=False, output_file_name="")

    # imageToChars.run(img_path="./test_images/image3.png")