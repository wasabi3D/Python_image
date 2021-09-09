from PIL import Image

img= Image.open("bebe.jpeg")
print("______", end='\n\n\n')

print(img)
print(img.format, img.size, img.mode)

img.show()
