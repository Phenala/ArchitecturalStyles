from modules.FileLayer import *

class EncryptionLayer:

    def __init__(self):
        self.file = FileLayer()

    def open(self, table):
        data = self.file.open(table)
        return self.decrypt(data)

    def save(self, table, data):
        data = self.encrypt(data)
        self.file.save(table, data)

    def decrypt(self, data):
        outdata = ''
        while len(data) > 1:
            outdata += chr(500 - int(data[:3]))
            data = data[3:]
        return outdata

    def encrypt(self, data):
        outdata = ''
        for i in data:
            outdata += str(500 - (ord(i)))
        return outdata

    def recall(self):
        return self.file.recall()
