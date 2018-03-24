
class ImageFilter:

    def __init__(self, amount = 1):
        self.amount = amount

    def filterImage(self, image):
        newImage = image.copy()
        for i in range(image.width()):
            for j in range(image.height()):
                newImage.put(self.parseColor(self.filterPixel(image.get(i,j))), to=(i,j))
        return newImage

    def filterPixel(self, pixel):
        pass

    def clamp(self, color):
        return (int(max(0,min(255,color[0]))), int(max(0,min(255,color[1]))), int(max(0,min(255,color[2]))))

    def parseColor(self, color):
        return ('#' + format(color[0], '2x') + format(color[1], '2x') + format(color[2], '2x')).replace(' ','0')

