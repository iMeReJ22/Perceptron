import sys

from Iris import Iris
from Perceptron import Perceptron


def getLists(trainSet, testSet, checkSet):
    trainList = list()
    for i in trainSet:
        trainList.append(Iris(i))
    testList = list()
    for i in testSet:
        testList.append(Iris(i))
    checkList = list()
    for i in checkSet:
        checkList.append(Iris(i))

    return trainList, testList, checkList

def getInitialData():
    if len(sys.argv) >= 4:
        a = float(sys.argv[1])
        trainSet = open(sys.argv[2], "r")
        testSet = open(sys.argv[3], "r")
    else:
        a = 0.5
        trainSet = open("Data/trainSet.txt", "r")
        testSet = open("Data/testSet.txt", "r")

    checkSet = open("Data/checkSet.txt", "r")
    trainList, testList, checkList = getLists(trainSet, testSet, checkSet)
    return a, trainList, testList, checkList


def getAccuracy(correct, overall):
    accuracy = correct / overall * 100
    return accuracy

def classificate(answer):
    if answer:
        guess = "Iris-setosa"
    else:
        guess = "Iris-versicolor"
    return guess

def trainPerceptronAndReturnAccuracy(perceptron, trainList):
    correctGuesses = 0
    correctSetosaGuesses = 0
    correctVersicolorGuesses = 0
    for iris in trainList:
        name = iris.name
        answer = perceptron.isActivated(iris.vector)
        guess = classificate(answer)

        if guess == name:
            correctGuesses += 1
            if name == "Iris-setosa":
                correctSetosaGuesses += 1
            else:
                correctVersicolorGuesses += 1
        else:
            perceptron.learn(not answer, answer, iris.vector)
    overallAccuracy = getAccuracy(correctGuesses, len(trainList))
    setosaAccuracy = getAccuracy(correctSetosaGuesses, len(trainList)/2)
    versicolorAccuracy = getAccuracy(correctVersicolorGuesses, len(trainList)/2)
    return overallAccuracy, setosaAccuracy, versicolorAccuracy


def printAccuracies(ovaerall, setosa, versicolor):
    print(f"\nOverall accuracy:\t\t{ovaerall}%")
    print(f"Setosa accuracy:\t\t{setosa}%")
    print(f"Versicolor accuracy:\t{versicolor}%")


def TrainAgainPrompt(perceptron, trainList):
    while True:
        t = trainPerceptronAndReturnAccuracy(perceptron, trainList)
        printAccuracies(t[0], t[1], t[2])
        perceptron.printInfo()
        if t[0] > 99:
            input("")
            break
        con = input("Train again? (n/y): ")
        if con == "n":
            break


def testPerceptronAndPrintAccuracy(perceptron, testList, checkList):
    print("\n\nTestring perceptron on testSet.\n")
    correctGuesses = 0
    correctSetosaGuesses = 0
    correctVersicolorGuesses = 0
    for i in range(len(testList)):
        guess = classificate(perceptron.isActivated(testList[i].vector))

        if guess == checkList[i].name:
            correctGuesses += 1
            if guess == "Iris-setosa":
                correctSetosaGuesses += 1
            else:
                correctVersicolorGuesses += 1

    overallAccuracy = getAccuracy(correctGuesses, len(testList))
    setosaAccuracy = getAccuracy(correctSetosaGuesses, len(testList) / 2)
    versicolorAccuracy = getAccuracy(correctVersicolorGuesses, len(testList) / 2)

    printAccuracies(overallAccuracy, setosaAccuracy, versicolorAccuracy)


def userInputLoop(perceptron):
    while True:
        con = input("\nDo you wan to test your own Iris? (y/n): ")
        if con == "n":
            break
        else:
            vector = list()
            print("Please put in your attributes: ")
            for i in range(len(perceptron.weights)):
                vector.append(float(input(f"{i + 1}. ")))

            guess = classificate(perceptron.isActivated(vector))
            print(f"My gouess: {guess}")


# Main code here!!!!!
a, trainList, testList, checkList = getInitialData()

perceptron = Perceptron(trainList[0].getVectorLength(), a, 1, "Iris", 1)

TrainAgainPrompt(perceptron, trainList)

testPerceptronAndPrintAccuracy(perceptron, testList, checkList)

userInputLoop(perceptron)
