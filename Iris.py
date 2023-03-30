class Iris:
    def __init__(self, line):
        self.name, self.vector = self._initNameAndVector(line)

    def _initNameAndVector(self, line):
        name = "TBD"
        vector = list()
        line = line.replace("\n", "")
        parts = line.split(",")
        for i in range(len(parts)):
            try:
                vector.append(float(parts[i]))
            except ValueError:
                name = parts[i]
        return name, vector

    def __str__(self):
        line = self.vector.__str__() + "\tName: " + self.name
        return line

    def getVectorLength(self):
        return len(self.vector)
