import random
from PIL import Image

def change_contrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level)) 
    def contrast(c):
        return 128 + factor * (c - 128) 
    return img.point(contrast)

for k in range (1,9):
    image = change_contrast(Image.open("Bitplane"+str(k)+'.png'), 900) 
    image = image.convert('1')
    o_pixels = image.load()
    outfile1 = Image.new("1", (image.size[0], image.size[1] * 2)) 
    f_pixels = outfile1.load()
    outfile2 = Image.new("1", (image.size[0], image.size[1] * 2)) 
    s_pixels = outfile2.load()
    for i in range(image.size[0]): 
        for j in range(image.size[1]):
            if o_pixels[i,j] == 0:
                if random.randint(0, 1):
                    f_pixels[i,j * 2 ] = 1
                    f_pixels[i,j * 2 + 1] = 0
                    s_pixels[i,j * 2 ] = 0
                    s_pixels[i,j * 2 + 1] = 1 
                else:
                    f_pixels[i,j * 2 ] = 0
                    f_pixels[i,j * 2 + 1] = 1
                    s_pixels[i,j * 2 ] = 1
                    s_pixels[i,j * 2 + 1] = 0
            else:
                if random.randint(0, 1):
                    f_pixels[i,j * 2 ] = 0
                    f_pixels[i,j * 2 + 1] = 1
                    s_pixels[i,j * 2 ] = 0
                    s_pixels[i,j * 2 + 1] = 1 
                else:
                    f_pixels[i,j * 2 ] = 1
                    f_pixels[i,j * 2 + 1] = 0
                    s_pixels[i,j * 2 ] = 1
                    s_pixels[i,j * 2 + 1] = 0
    outfile1.save("Map"+ str(k) + "_share1.png") 
    outfile2.save("Map"+ str(k) + "_share2.png")