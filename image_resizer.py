from PIL import Image


def resize_image(size1, size2):
    image = Image.open("Baldurs-Gate-3-Dark-Urge-And-Sceleritas-Fel.jpg")

    print(f"Current size: {image.size}")

    resized_image = image.resize((size1, size2))

    resized_image.save("darkurgebackground.jpg")

    print(f"Current size: {resized_image.size}")


size1= int(input("Enter Width: "))
size2 = int(input("Enter Length: "))
resize_image()