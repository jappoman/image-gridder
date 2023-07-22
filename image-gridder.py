import os
from PIL import Image, ImageDraw, ImageFont

def draw_grid(image_path):
    # Open the original image
    original_image = Image.open(image_path)

    # Get the image resolution in DPI (dots per inch)
    dpi = original_image.info.get('dpi')

    # Calculate the number of pixels per centimeter based on the DPI
    pixels_per_cm = dpi[0] / 2.54

    # Calculate the size in pixels for 16 cm
    size_in_pixel = int(pixels_per_cm * 16)

    # Create a new image with the calculated size
    new_image = Image.new('RGB', (size_in_pixel, size_in_pixel), 'white')

    # Resize the original image to the desired size
    resized_image = original_image.resize((size_in_pixel, size_in_pixel))

    # Copy the resized image into the new image
    new_image.paste(resized_image, (0, 0))

    # Create an ImageDraw object to draw on the new image
    draw = ImageDraw.Draw(new_image)

    # Calculate the size of each square
    square_size = size_in_pixel // 16

    # Set the thickness and color of the lines and numbers
    line_width = 5
    line_color = 'red'
    font_size = font_size = int(pixels_per_cm * 0.4)

    # Load a font with the desired size
    font = ImageFont.truetype("arial.ttf", font_size)

    # Draw the grid with numbering
    for i in range(16):
        for j in range(16):
            x = j * square_size
            y = (15 - i) * square_size
            draw.line([(x, 0), (x, size_in_pixel)], fill=line_color, width=line_width)
            draw.line([(0, y), (size_in_pixel, y)], fill=line_color, width=line_width)
            draw.text((x + 2, y + 2), f'{j},{i}', fill=line_color, font=font)  # Swap j with i

    # Get the path of the original image
    image_dir = os.path.dirname(image_path)

    # Save the resulting image in the same folder as the original image
    new_image_path = os.path.join(image_dir, 'gridded_image.png')
    new_image.save(new_image_path)
    print(f"The image was saved as: {new_image_path}")

# Ask for the image path from the user
input_image_path = input("Insert image path: ")
draw_grid(input_image_path)