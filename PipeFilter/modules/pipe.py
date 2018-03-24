class Pipe:

    def __init__(self):

        self.filters = []

    def addFilter(self, imageFilter):
        self.filters.append(imageFilter)

    def run(self, image):
        for i in self.filters:
            image = i.filterImage(image)
        return image
