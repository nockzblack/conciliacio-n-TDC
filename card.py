class Card:
    def __init__(self, alias, ending):
        self.alias = alias
        self.ending = ending

    def getData(self):
        return (self.alias, self.ending)
