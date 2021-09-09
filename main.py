from PIL import Image


def ex2():
    img = Image.open("bebe.jpeg")
    print("______", end='\n\n\n')

    print(img)
    print(img.format, img.size, img.mode)

    img.show()


def ex3():
    # (a)
    img = Image.open("bebe.jpeg")
    morceau = img.crop((1050, 650, 1300, 800))
    morceau.show()

    # (b)
    morceau.save("image_partielle.jpg")

    # (c)
    img.paste(morceau, (1000, 500, 1250, 650))
    img.show()


def ex4():
    img = Image.open("bebe.jpeg")
    r, v, b = img.split()
    # r.show()
    # v.show()
    # b.show()

    r = r.point(lambda i: i * 1.5)
    imr_r = Image.merge(img.mode, (r, v, b))
    imr_r.show()

    img_lum = img.point(lambda i : i * 0.05)
    img_lum.show()


def ex6():
    img = Image.open("bebe.jpeg")

    img1 = img.copy()
    for i in range(800):
        img.putpixel((i, 150), (255, 0, 0))
    img.show()

    for i in range(800):
        img1.putpixel((150, i), (0, 255, 0))
    img1.show()

    for i in range(100):
        for o in range(200):
            img1.putpixel((50 + i, 100 + o), (0, 0, 255))
    img1.show()

    pixels = img.getpixel((56,161))
    print(pixels)


def main():
    ex6()


if __name__ == "__main__":
    main()
