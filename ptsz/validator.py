import sys

from ptsz import Task

instancePath = ""
solutionPath = ""
# array of tasks read from file
tasks = []
solution = 0
orderOfTasks = []

def readInstance():
    file = open(instancePath)
    size = file.readline()
    readLines = file.readlines()
    for line in readLines:
        splitLine = line.split(" ")
        splitLine = splitLine[:4]
        p,r,d,w = splitLine
        task = Task(p, r, d, w)
        tasks.append(task)
    print("Read File")
    # [print(t) for t in tasks]
    file.close()
def readSolution():
    file = open(solutionPath)
    global solution
    solution = int(file.readline())
    global orderOfTasks
    orderOfTasks= [t for t in file.readline().split(" ")]
    orderOfTasks.pop()
    # print(solution)
    print("Read Solution File")
    file.close()


def validate():
    print("Start validating")

def sortTasks():
    global orderOfTasks
    print("Sorting tasks")
    tempTasks = []
    for i in orderOfTasks:
        print(f"Add {i}th task")

        tempTasks.append(tasks[int(i)])
    print("New order of tasks: ")
    [print(t) for t in tempTasks]


def checkRetrasar():
    actualTime = 0
    foundSolution = 0
    for task in tasks:
        newTime = actualTime + task.p
        print(f'Checking {task} with time {newTime}')
        if newTime <= task.d:
            #no retrasar
            print(f'task {task} is good')
        elif newTime > task.d:
            #there is retrasar
            print(f'task {task} is late')
            foundSolution = foundSolution + task.w

        actualTime = newTime
        print(actualTime)
    print(f'all tasks checked; solution found: {foundSolution}')
    return foundSolution


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('bad number of arguments')
        exit(-1)
    instancePath = sys.argv[1]
    o = sys.argv[2]
    solutionPath = sys.argv[3]
    #Read file with problem instance
    readInstance()
    #Read solution File
    readSolution()
    #Sort our instances by solution file
    sortTasks()
    solutionFound = checkRetrasar()
    #print(f'{solution};{solutionFound}')
    if solutionFound == solution:
        print('Validation successful')
    else:
        print('Validation failed')


