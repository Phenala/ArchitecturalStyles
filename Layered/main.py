from modules.DatabaseLayer import *


class Main:

    def __init__(self):
        self.db = Database()
        self.commands = {
                'showTables':self.showTables,
                'selectTable':self.selectTable,
                'addTable':self.addTable,
                'printTable':self.printTable,
                'addColumn':self.addColumn,
                'addRow':self.addRow,
                'setValue':self.setValue,
            }
        self.table = None
        self.main()


    def main(self):
        while True:
            command = input('=>')
            com = command
            params = ''
            if ' ' in command:
                com = command[:command.find(' ')]
                params = command[command.find(' '):].strip()
            if com in self.commands:
                self.commands[com](params)
            else:
                print(com)
                print(params)
                print('Instruction not recognized')

    def showTables(self, params):
        for i in self.db.getTables():
            print(i)

    def selectTable(self, params):
        if self.confirm(params, 1):
            return
        self.table = self.db.getTable(params.strip())
        print('Selected table ' + self.table.name)

    def printTable(self, params):
        if not self.table:
            print('No table selected')
            return
        for i in self.table.titles:
            print(format(i, '20'), end='')
        print()
        print('-'*(len(self.table.titles)*20))
        for i in self.table.table:
            for j in i:
                print(format(j, '20'), end='')
            print()

    def addTable(self, params):
        if self.confirm(params, 1):
            return
        self.db.makeTable(params)

    def addColumn(self, params):
        if not self.table:
            print('No table selected')
        if self.confirm(params, 1):
            return
        self.table.addColumn(params.strip())

    def addRow(self, params):
        if not self.table:
            print('No table selected')
        if self.confirm(params, len(self.table.titles)):
            return
        self.table.addRow(params.split(' '))

    def setValue(self, params):
        if not self.table:
            print('No table selected')
        if self.confirm(params, 3):
            return
        prlst = params.split(' ')
        if self.confirm(prlst[0], 2, '=>'):
            return
        self.table.setValue(prlst[0].split('=>'), prlst[1], prlst[2])

    def confirm(self, params, num, bound = ' '):
        print(params)
        if not len(params.strip().split(bound)) == num:
            return True


Main()
            
            
