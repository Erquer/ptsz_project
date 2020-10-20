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
size = 50
#duration time parameters
longTaskCount = math.floor(size * 0.20)
mediumTaskCount = math.floor(size * 0.40)
shortTaskCount = math.floor(size * 0.40)

#start time parameters
earlyTasks = math.floor(size * 0.35)
semiTasks = math.floor(size * 0.35)
lateTasks = math.floor(size * 0.30)

#wages parameters
lesserTasks = math.floor(size * 0.40)
importantTasks = math.floor(size * 0.35)
veryImportantTasks = math.floor(size * 0.25)

tasks =[]
def generateTemplate(size):
    global tasks
    for i in range(size):
        tasks.append(Task(0,0,0,0))

def chooseTasksReadyTime():
    #globals
    global tasks, earlyTasks,semiTasks,lateTasks, size
    available = [i for i in range(len(tasks))]
    print(available)
    #choose early tasks
    while earlyTasks > 0:
        #choose new available task index
        randNum = random.randint(0, len(available))
        #assing value r to chosen task
        tasks[available[randNum]].r = random.randint(0,size)
        # remove element with random index
        available.pop(randNum)
        #decrement counter
        earlyTasks -= 1
    while semiTasks > 0:
        randNum = random.randint(0,len(available))
        # assing value r to chosen task
        tasks[available[randNum]].r = random.randint(size, size * 3)
        # remove element with random index
        available.pop(randNum)
        semiTasks -= 1
    while lateTasks > 0 and len(available) > 0:
        randNum = random.randint(0, len(available))
        # assing value r to chosen task
        tasks[available[randNum]].r = random.randint(size*3, size * 6)
        # remove element with random index
        available.pop(randNum)
        lateTasks -= 1



def chooseTasksDuration():
    global tasks
    global longTaskCount,shortTaskCount,mediumTaskCount
    used = []
    #todo: finish every loop
    while longTaskCount > 0:
        randNum = random.randint(0, len(tasks))
        if not used.__contains__(randNum):
            task = tasks[randNum]
            used.append(randNum)
        longTaskCount -= 1



def generateInstance(size):
    generateTemplate(size)
    chooseTasksReadyTime()

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
    print("instance size:", size)

if __name__ == '__main__':
    while  longTaskCount + shortTaskCount + mediumTaskCount != size:
        shortTaskCount += 1
    while  earlyTasks + semiTasks + lateTasks != size:
        earlyTasks += 1
    while lesserTasks + importantTasks + veryImportantTasks != size:
        lesserTasks += 1
    # for i in range(50, 550, 50):
    #     generateTestFile(i)
    #     generateTemplate(i)
    generateInstance(50)
    [print(t) for t in tasks]
