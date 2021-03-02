class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        self.__elements.sort()
        length = len(self.__elements) - 1
        self.maximumDifference = self.__elements[length] - self.__elements[0]

d=Difference([4,3,1])
d.computeDifference()
print(d.maximumDifference)