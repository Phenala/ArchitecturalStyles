from modules.EncryptionLayer import *

class Database:

    def __init__(self):
        self.enc = EncryptionLayer()
    
    def getTable(self, name):
        return self.parseTable(name, self.enc.open(name))

    def getTables(self):
        return self.enc.recall()

    def makeTable(self, name):
        t = Table(name, [])
        t.addColumn('id')
        t.save()
        return t

    def parseTable(self, name, string):
        data = string.split('\n')
        num = int(data.pop(0))
        table = []
        for i in range(len(data)//num):
            rw = []
            for j in range(num):
                rw.append(data[i*num + j])
            table.append(rw)
        t = Table(name, table[0])
        if (len(table) > 1):
            t.table = table[1:]
        return t
        

class Table:

    def __init__(self, name, columns):
        self.name = name
        self.titles = columns
        self.enc = EncryptionLayer()
        self.table = []

    def addRow(self, rowData):
        if len(rowData) == len(self.titles):
            self.table.append(rowData)
        self.save()

    def addColumn(self, columnName):
        self.titles.append(columnName)
        for i in self.table:
            i.append('')
        self.save()

    def getValue(self, condition, column):
        cindex = self.titles.index(column)
        self.getRow(condition)[cindex]

    def getRow(self, condition):
        cindex = self.titles.index(condition[0])
        for i in self.table:
            if i[cindex] == condition[1]:
                return i.copy()

    def getSettableRow(self, condition):
        cindex = self.titles.index(condition[0])
        for i in self.table:
            if i[cindex] == condition[1]:
                return i

    def setValue(self, condition, column, value):
        cindex = self.titles.index(column)
        self.getSettableRow(condition)[cindex] = value

    def getColumn(self, column):
        vals = []
        cindex = self.titles.index(column)
        for i in self.table:
            vals.append(i[cindex])

    def encodeTable(self):
        string = ''
        string += str(len(self.titles)) + '\n'
        for i in [self.titles] + self.table:
            for j in i:
                string += j + '\n'
        return string

    def save(self):
        self.enc.save(self.name, self.encodeTable())

        
