class Team:

    def __init__(self, name):
        self.name = name
        self.score = 0

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setScore(self, score):
        self.score = score

    def getScore(self):
        return self.score

    def addToScore(self,score):
        self.score = self.score + score
