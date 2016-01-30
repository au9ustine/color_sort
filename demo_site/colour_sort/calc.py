from __future__ import print_function
from PIL import Image
import urllib

class CalcRGBAvg:
    def __init__(self, openable_img):
        try:
            self.img_obj = Image.open(openable_img)
        except IOError:
            print("Cannot open ", openable_img)

        self.pixels = self.img_obj.load()
        print(self.img_obj.mode)

    def calculate(self, f_calc):
        eigen = [0,0,0]
        pixels = self.pixels
        x_max, y_max = self.img_obj.size
        total_pixels = x_max * y_max
        for i in range(x_max):
            for j in range(y_max):
                r, g, b = pixels[i, j]
                eigen += f_calc(r, g, b) / total_pixels
        return eigen

def get_luminance_val(r, g, b):
    return (r*0.299 + g*0.587 + b*0.114) % 256

def get_chromatic_val(r, g, b):
    return (r + (g << 8) + (b << 16)) & 0xffffff
