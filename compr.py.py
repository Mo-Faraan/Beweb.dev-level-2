from PIL import Image

def comim(input_path, output_path, quality):
    with Image.open(input_path) as img:
        img.save(output_path, format='JPEG', quality=quality)
        print("Image compressed and saved.")


input_image_path = input("Enter the path to the input image: ")
output_image_path = input("Enter the path to save the compressed image: ")
quality = int(input("Enter the compression quality (0 to 100): "))

comim(input_image_path, output_image_path, quality)
