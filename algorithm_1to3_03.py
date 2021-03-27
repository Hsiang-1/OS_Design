## update the process of the algorithm
import sys
from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial

# time delay function
def sleep_1():
    loop = QEventLoop()
    QTimer.singleShot(2000, loop.quit)
    loop.exec_()

# FIFO Algorithm
def FIFO(jobNum, jobsArriveTime , jobsCostTime):
    # error input
    if jobNum <= 0 :
        print("error input!")
        return 0
    # to determine the order of the input jobs
    jobOrder = []
    for virtualTime in range(0, max(jobsArriveTime)+sum(jobsCostTime)):
        for j in range(0, jobNum):
            if (jobsArriveTime[j] == virtualTime):
                jobOrder.append(j)
    # caculate the finish time of every job
    print("--------------------")
    print('THE PROCESS:')
    jobsFinishTime = [0 for x in range(0, jobNum)]
    jobsBeginTime = [0 for x in range(0, jobNum)]
    arrived = [0 for x in range(0, jobNum)]
    currentTime = jobsArriveTime[jobOrder[0]]
    for order in jobOrder:
        if currentTime < jobsArriveTime[order]:
            currentTime = jobsArriveTime[order]
        jobsBeginTime[order] = currentTime
        for i in range(0, jobNum):
            if (jobsArriveTime[i] <= currentTime) and (arrived[i] == 0):
                print('Time ' + str(jobsArriveTime[i]) + ': Job ' + str(i) + ' arrived in!')
                arrived[i] = 1
        print('Time ' + str(currentTime) + ': Job ' + str(order) + ' begin to run! ')
        currentTime += jobsCostTime[order]
        for i in range(0, jobNum):
            if (jobsArriveTime[i] <= currentTime) and (arrived[i] == 0):
                print('Time ' + str(jobsArriveTime[i]) + ': Job ' + str(i) + ' arrived in!')
                arrived[i] = 1
        jobsFinishTime[order] = currentTime
        print('Time ' + str(currentTime) + ': Job ' + str(order) + ' has finished! ')
    # caculate the cycling time and the weighted cycling time of every job
    jobsCyclingTime = []
    jobsWeightedCyclingTime = []
    for i in range(0,jobNum):
        cyclingTime = jobsFinishTime[i] - jobsArriveTime[i]
        jobsCyclingTime.append(cyclingTime)
        jobsWeightedCyclingTime.append( cyclingTime / jobsCostTime[i])
    # display the answers
    print("--------------------")
    print("FIFO Algorithm")
    print("arrive time: ", jobsArriveTime)
    print("cost time: ", jobsCostTime)
    print("begin time: ", jobsBeginTime)
    print("finish time: ", jobsFinishTime)
    print("cycling time: ", jobsCyclingTime)
    print("weighted cycling time: ", jobsWeightedCyclingTime)
    print("--------------------")
    return 1

# ShortJobFirst Algorithm
def ShortJobFirst(jobNum, jobsArriveTime , jobsCostTime):
    # error input
    if jobNum <= 0 :
        print("error input!")
        return 0
    # use finished array to mark the finished jobs
    finished = [0 for i in range(0, jobNum)]
    arrived = [0 for i in range(0 ,jobNum)]
    jobsFinishTime = [0 for i in range(0, jobNum)]
    jobsBeginTime = [0 for i in range(0, jobNum)]
    # order and caculate
    currentTime = 0
    for time in range(0, max(jobsArriveTime)+sum(jobsCostTime)):
        thisOrder = -1
        timeMin = 1000
        for job in range(0,jobNum):
            if (currentTime >= jobsArriveTime[job]) and (finished[job] == 0) and (jobsCostTime[job] < timeMin):
                timeMin = jobsCostTime[job]
                thisOrder = job
        if thisOrder != -1:
            for i in range(0, jobNum):
                if (jobsArriveTime[i] <= currentTime) and (arrived[i] == 0):
                    print('Time ' + str(jobsArriveTime[i]) + ': Job ' + str(i) + ' arrived in!')
                    arrived[i] = 1
            jobsBeginTime[thisOrder] = currentTime
            print('Time ' + str(currentTime) + ': Job ' + str(thisOrder) + ' begin to run! ')
            currentTime += timeMin
            jobsFinishTime[thisOrder] = currentTime
            finished[thisOrder] = 1
            for i in range(0, jobNum):
                if (jobsArriveTime[i] <= currentTime) and (arrived[i] == 0):
                    print('Time ' + str(jobsArriveTime[i]) + ': Job ' + str(i) + ' arrived in!')
                    arrived[i] = 1
            print('Time ' + str(currentTime) + ': Job ' + str(thisOrder) + ' has finished! ')
        else:
            currentTime += 1
    # caculate the cycling time and weighted cycling time
    jobsCyclingTime = []
    jobsWeightedCyclingTime = []
    for i in range(0, jobNum):
        cyclingTime = jobsFinishTime[i] - jobsArriveTime[i]
        jobsCyclingTime.append(cyclingTime)
        jobsWeightedCyclingTime.append(cyclingTime/jobsCostTime[i])
    # display the answers
    print("--------------------")
    print("SJF Algorithm")
    print("arrive time: ", jobsArriveTime)
    print("cost time: ", jobsCostTime)
    print("begin time: ", jobsBeginTime)
    print("finish time: ", jobsFinishTime)
    print("cycling time: ", jobsCyclingTime)
    print("weighted cycling time: ", jobsWeightedCyclingTime)
    print("--------------------")
    return 1

# Priority Algorithm
def Priority(jobNum, jobsArriveTime, jobsCostTime, jobsPriority):
    # error input
    if jobNum <= 0 :
        print("error input!")
        return 0
    # mark the finished jobs and expresse their finish time
    finished = [0 for i in range(0, jobNum)]
    arrived = [0 for i in range(0, jobNum)]
    jobsFinishTime = [0 for i in range(0, jobNum)]
    jobsBeginTime = [0 for i in range(0, jobNum)]
    # order and caculate
    currentTime = 0
    for time in range(0, max(jobsArriveTime)+max(jobsCostTime)):
        thisOrder = -1
        priorityMax = 5
        for job in range(0, jobNum):
            if (finished[job] == 0) and (jobsPriority[job] < priorityMax) and (currentTime >= jobsArriveTime[job]):
                priorityMax = jobsPriority[job]
                thisOrder = job
        if thisOrder != -1:
            for i in range(0, jobNum):
                if (jobsArriveTime[i] <= currentTime) and (arrived[i] == 0):
                    print('Time ' + str(jobsArriveTime[i]) + ': Job ' + str(i) + ' arrived in!')
                    arrived[i] = 1
            jobsBeginTime[thisOrder] = currentTime
            print('Time ' + str(currentTime) + ': Job ' + str(thisOrder) + ' begin to run! ')
            currentTime += jobsCostTime[thisOrder]
            jobsFinishTime[thisOrder] = currentTime
            finished[thisOrder] = 1
            for i in range(0, jobNum):
                if (jobsArriveTime[i] <= currentTime) and (arrived[i] == 0):
                    print('Time ' + str(jobsArriveTime[i]) + ': Job ' + str(i) + ' arrived in!')
                    arrived[i] = 1
            print('Time ' + str(currentTime) + ': Job ' + str(thisOrder) + ' has finished! ')
        else:
            currentTime += 1
    # caculate the cycling time and weighted cycling time
    jobsCyclingTime = []
    jobsWeightedCyclingTime = []
    for i in range(0, jobNum):
        cyclingTime = jobsFinishTime[i] - jobsArriveTime[i]
        jobsCyclingTime.append(cyclingTime)
        jobsWeightedCyclingTime.append(cyclingTime/jobsCostTime[i])
    # display the answers
    print("--------------------")
    print("Priority Algorithm")
    print("priority: ", jobsPriority)
    print("arrive time: ", jobsArriveTime)
    print("cost time: ", jobsCostTime)
    print("begin time: ", jobsBeginTime)
    print("finish time: ", jobsFinishTime)
    print("cycling time: ", jobsCyclingTime)
    print("weighted cycling time: ", jobsWeightedCyclingTime)
    print("--------------------")
    return 1

# user input mode
def UserInputData():
    global jobNum
    global jobsArriveTime
    global jobsCostTime
    while(1):
        jobNum = int(input("input the number of jobs(>=1):"))
        if jobNum >= 1:
            break
        else:
            print("error input")
    jobsArriveTime = []
    jobsCostTime = []
    for i in range(0, jobNum):
        print("input job_", i+1, "'s arrive time:",end = '')
        arriveTime = int(input())
        print("input job_", i+1, "'s cost time:",end='')
        costTime = int(input())
        jobsArriveTime.append(arriveTime)
        jobsCostTime.append(costTime)

## main program
# jobNum = 0
# jobsArriveTime = []
# jobsCostTime = []
# jobsPriority = []
# the test datas
jobNum = 5
jobsArriveTime = [ 0, 4, 7, 2, 15]
jobsCostTime = [ 3, 2, 1, 4, 2]
# priority of jobs, 1 is the highest, 3 is the lowest
jobsPriority = [ 1, 2, 1, 3, 1]
# UserInputData()
FIFO(jobNum, jobsArriveTime , jobsCostTime)
ShortJobFirst(jobNum, jobsArriveTime, jobsCostTime)
Priority(jobNum, jobsArriveTime, jobsCostTime, jobsPriority)