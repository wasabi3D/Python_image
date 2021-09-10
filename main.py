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


def ex7():
    img = Image.open("bebe.jpeg")
    img2 = img.convert('L')
    img3 = img.convert('1')
    img2.show()
    img3.show()


def ex8():
    img = Image.open("bebe.jpeg")
    largeur, hauteur = img.size

    WHITE_THRESHOLD = 50

    for x in range(largeur):
        for y in range(hauteur):
            r, v, b = img.getpixel((x, y))
            if r > WHITE_THRESHOLD and v > WHITE_THRESHOLD and b > WHITE_THRESHOLD:
                img.putpixel((x, y), (0, 0, 0))
    img.show()


def ex9():
    img = Image.open("bebe.jpeg")

    def niv_de_gris(image):
        largeur, hauteur = image.size
        for x in range(largeur):
            for y in range(hauteur):
                r, v, b = image.getpixel((x, y))
                g = int(0.125 * r + 0.7154 * v + 0.0721 * b)  # int((r + v + b) / 3)
                image.putpixel((x, y), (g, g, g))
        return image

    niv_de_gris(img).show()


def ex9_c():

    def noir_et_blanc(image, seuil: int):
        width, height = image.size
        for x in range(width):
            for y in range(height):
                r, v, b = image.getpixel((x, y))
                image.putpixel((x, y), (255, 255, 255) if int(0.125 * r + 0.7154 * v + 0.0721 * b) < seuil else (0, 0, 0))
        return image

    img = Image.open("bebe.jpeg")
    noir_et_blanc(img, 175).show()


def ex10():

    def img_en_neg(image):
        width, height = image.size
        for x in range(width):
            for y in range(height):
                r, v, b = image.getpixel((x, y))
                image.putpixel((x, y), (255 - r, 255 - v, 255 - b))
        return image

    img = Image.open("bebe.jpeg")
    img_en_neg(img).show()


def ex11():

    def filtre_rouge_noir(image):
        width, height = image.size
        for x in range(width):
            for y in range(height):
                r, v, b = image.getpixel((x, y))
                if v < r > b:
                    image.putpixel((x, y), (0, 0, 0))
        return image

    filtre_rouge_noir(Image.open("bebe.jpeg")).show()


def ex12_a():
    img = Image.open("bebe.jpeg")
    for i in range(50, 101):
        for j in range(150, 301):
            if (i - j) // 10 % 2 == 0:
                img.putpixel((i, j), (0, 0, 255))
            else:
                img.putpixel((i, j), (255, 0, 255))

    img.show()


def main():
    ex12_a()


if __name__ == "__main__":
    main()
