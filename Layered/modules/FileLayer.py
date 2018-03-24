import os

class FileLayer:

    def __init__(self):
        self.folder = 'data/'

    def open(self, table):
        return open(self.folder + table).read()

    def save(self, table, data):
        file = open(self.folder + table, 'w')
        file.write(data)
        file.close()

    def recall(self):
        dirs = []
        for i in os.scandir(self.folder):
            dirs.append(i.name)
        return dirs

    
