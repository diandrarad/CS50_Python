import os.path
from PIL import Image, ImageOps
from sys import argv, exit

def main():
    # Check number of command-line arguments
    if len(argv) < 3:
        exit("Too few command-line arguments")
    elif len(argv) > 3:
        exit("Too many command-line arguments")

    # Check file extensions
    elif not (argv[1].lower().endswith('.jpg') or
                argv[1].lower().endswith('.jpeg') or
                argv[1].lower().endswith('.png')):
        exit("Invalid input")
    elif not (argv[2].lower().endswith('.jpg') or
                argv[2].lower().endswith('.jpeg') or
                argv[2].lower().endswith('.png')):
        exit("Invalid output")

    # Check if input file exists
    elif not os.path.isfile(argv[1]):
        sys.exit("Input file does not exist")

    # Check if input file extension matches output file extension
    elif os.path.splitext(argv[1])[1] != os.path.splitext(argv[2])[1]:
        exit("Input and output have different extensions")

    # Load input image
    input_image = Image.open(argv[1])

    # Resize and crop input image
    shirt_image = Image.open('shirt.png')
    resized_image = ImageOps.fit(input_image, shirt_image.size)

    # Overlay shirt image onto input image
    resized_image.paste(shirt_image, (0, 0), shirt_image)

    # Save output image
    resized_image.save(argv[2])


if __name__ == "__main__":
    main()
