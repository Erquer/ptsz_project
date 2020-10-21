# n - rozmiar instancji problemu
# p-czas trwania
# r - moment gotowości
# d - deadline
# w - waga zadania
# postać pliku:
# n
# p r d w
import random
import math
from ptsz import Task
#duration time parameters
longTaskCount = 0
mediumTaskCount = 0
shortTaskCount = 0

#start time parameters
earlyTasks = 0
semiTasks = 0
lateTasks = 0

tasks =[]
def setParameters(size):
    global longTaskCount,mediumTaskCount,shortTaskCount,earlyTasks,semiTasks,lateTasks
    # duration time parameters
    longTaskCount = math.floor(size * 0.20)
    mediumTaskCount = math.floor(size * 0.40)
    shortTaskCount = math.floor(size * 0.40)

    # start time parameters
    earlyTasks = math.floor(size * 0.35)
    semiTasks = math.floor(size * 0.35)
    lateTasks = math.floor(size * 0.30)


def generateTemplate(size):
    global tasks
    for i in range(size):
        tasks.append(Task(0,0,0,0))
def chooseTasksReadyTime(size):
    #globals
    global tasks, earlyTasks,semiTasks,lateTasks
    actualTasks = tasks
    available = [i for i in range(len(tasks))]

    print(available, len(actualTasks))
    #TODO: make loops as a function
    #choose early tasks
    while earlyTasks > 0:
        #choose new available task index
        randNum = random.randint(0, len(available)-1)

        #assing value r to chosen task
        actualTasks[available[randNum]].r = random.randint(0,size)
        # remove element with random index
        available.pop(randNum)
        #decrement counter
        earlyTasks -= 1
    while semiTasks > 0:
        randNum = random.randint(0,len(available)-1)
        # assing value r to chosen task
        actualTasks[available[randNum]].r = random.randint(size, size * 3)
        # remove element with random index
        available.pop(randNum)
        semiTasks -= 1
    while lateTasks > 0:
        randNum = random.randint(0, len(available)-1)
        # assing value r to chosen task
        actualTasks[available[randNum]].r = random.randint(size*2, size * 5)
        # remove element with random index
        available.pop(randNum)
        lateTasks -= 1
    tasks = actualTasks

def chooseTasksDuration(size):
    global tasks
    global longTaskCount,shortTaskCount,mediumTaskCount
    available = [i for i in range(len(tasks))]
    acTasks = tasks
    #TODO: make it as function with parameters
    while longTaskCount > 0:
        randNum = random.randint(0, len(available)-1)
        duration = random.randint(round(size), round(size * 1.3))
        acTasks[available[randNum]].p = duration
        acTasks[available[randNum]].d = acTasks[available[randNum]].r + random.randint(duration + 1, round(duration * 1.8))
        available.pop(randNum)
        longTaskCount -= 1
    while shortTaskCount > 0:
        randNum = random.randint(0, len(available) - 1)
        duration = random.randint(1, round(size/2))
        acTasks[available[randNum]].p = duration
        acTasks[available[randNum]].d = acTasks[available[randNum]].r + random.randint(duration + 1, round(duration * 1.8))
        available.pop(randNum)
        shortTaskCount -= 1
    while mediumTaskCount > 0:
        randNum = random.randint(0, len(available) - 1)
        duration = random.randint(round(size / 2), size)
        acTasks[available[randNum]].p = duration
        acTasks[available[randNum]].d = acTasks[available[randNum]].r + random.randint(duration + 1,
                                                                                       round(duration * 1.8))
        available.pop(randNum)
        mediumTaskCount -= 1
    tasks = acTasks

def chooseWages(size):
    global tasks
    for i in range(len(tasks)):
        tasks[i].w = random.randint(1,size)

def generateInstance(size):
    generateTemplate(size)
    chooseTasksReadyTime(size)
    chooseTasksDuration(size)
    chooseWages(size)

#generate test instances with perfect matching
def generateTestFile(n):
    file = open("instances/testRevertedInstance{0}".format(n),"w")
    for i in range(n+1):
        if(i == 0):
            file.write('{0}\n'.format(n))
        else:
            file.write('{0} {1} {2} {3} \n'.format(1,50-i,50-i+1,1))
    file.close()
    print("Generated TestInstance")

def generate(n):
    global tasks
    generateInstance(n)
    file = open("instances/126828_{0}.in".format(n),"w")
    for i in range(n+1):

        if i == 0:
            file.write(f'{n}\n')
        else:
            file.write(f'{tasks[i-1]}\n')

if __name__ == '__main__':
    for i in range(50,501,50):
        setParameters(i)
        while longTaskCount + shortTaskCount + mediumTaskCount != i:
            shortTaskCount += 1
        while earlyTasks + semiTasks + lateTasks != i:
            earlyTasks += 1
        generate(i)
        tasks.clear()
