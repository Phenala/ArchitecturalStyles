from modules.imagefilter import *

class GrayScale(ImageFilter):

    def filterPixel(self, pixel):
        npixel = ( pixel[0], pixel[0], pixel[0])
        return npixel

class Invert(ImageFilter):

    def filterPixel(self, pixel):
        npixel = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])
        return npixel

class BlueTint(ImageFilter):

    def filterPixel(self, pixel):
        npixel = (pixel[0], pixel[1], min(pixel[2] + 50, 255))
        return npixel

class Modulate(ImageFilter):

    def filterPixel(self, pixel):
        npixel = ((pixel[0]%50)*5, (pixel[1]%50)*5, (pixel[2]%50)*5)
        return npixel

class Vivify(ImageFilter):

    def filterPixel(self, pixel):
        p = pixel
        average = int((p[0] + p[1] + p[2])/3)
        np1 = average + ((p[0] - average) * self.amount)
        np2 = average + ((p[1] - average) * self.amount)
        np3 = average + ((p[2] - average) * self.amount)
        return self.clamp((np1, np2, np3))

class Contrast(ImageFilter):

    def filterPixel(self, pixel):
        p = pixel
        average = int((p[0] + p[1] + p[2])/3)
        np0 = p[0] + (p[0] - 125 * self.amount)
        np1 = p[1] + (p[1] - 125 * self.amount)
        np2 = p[2] + (p[2] - 125 * self.amount)
        return self.clamp((np0, np1, np2))

class Brighten(ImageFilter):

    def filterPixel(self, pixel):
        p = pixel
        np0 = p[0] * self.amount
        np1 = p[1] * self.amount
        np2 = p[2] * self.amount
        return self.clamp((np0, np1, np2))
