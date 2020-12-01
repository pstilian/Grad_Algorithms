import sys
import time
import datetime as dt
import random
import numpy as np

def buildData(size, type):
    #build data array
    arrData = [] * size
    # s for sorted
    if type == 's':
        i = 0
        arrData = np.zeros(size, dtype=int)
        while i < size:
            arrData[i] = i
            i += 1
    # c for constant value zero
    if type == 'c':
        arrData = np.zeros(size, dtype=int)
    # r for random int
    if type == 'r':
        arrData = np.random.randint(1, size, size)

    #print(arrData)
    
    return arrData


def checkCorrect(data):
    flag = False
    i = 1
    while i < len(data):
        if data[i] < data[i - 1]:
            flag = True
        i += 1

    #print(data)
    if flag == True:
        print("Data incorrectly sorted after running algorithm")
    else:
        print("Data correctly sorted after running algorithm")
    

def selectionSort(data):
    # traverse through data
    for i in range(len(data)):
        index = i
        for j in range(i + 1, len(data)):
            if data[index] > data[j]:
                index = j
        # swap values
        data[i], data[index] = data[index], data[i]
    
    return data

def median(d, i, j, k):
    if d[i] < d[j]:
        return i if d[k] < d[i] else k if d[k] < d[j] else j
    else:
        return j if d[k] < d[j] else k if d[k] < d[i] else i
 
def partition(data, left, right):

    pivotIndex = median(data, left, right, (left + right) // 2)
    data[left], data[pivotIndex] = data[pivotIndex], data[left]
    pivotValue = data[left]

    leftMarker = left
    rightMarker = right
    flag = False

    while not flag:
        while leftMarker <= rightMarker and data[leftMarker] <= pivotValue:
            leftMarker += 1

        while data[rightMarker] >= pivotValue and rightMarker >= leftMarker:
            rightMarker -= 1

        if rightMarker <= leftMarker:
            flag = True
        else:
            temp = data[leftMarker]
            data[leftMarker] = data[rightMarker]
            data[rightMarker] = temp
    temp = data[left]
    data[left] = data[rightMarker]
    data[rightMarker] = temp

    return rightMarker
    

def quickSort(data, left, right):

    if left < right:
        pivot = partition(data, left, right)

        quickSort(data, left, pivot - 1)
        quickSort(data, pivot + 1, right)

def insertionSort(data):
    # traverse through data
    for i in range(1, len(data)):
        curData = data[i]
        index = i - 1

        while index >= 0 and curData < data[index]:
            data[index + 1] = data[index]
            index -= 1
        data[index+1] = curData
    
    return data


#---------------------------- MAIN CODE ----------------------------

sType, dSize, dType = sys.argv[1], sys.argv[2], sys.argv[3]

Data = buildData(int(dSize), dType)
startTime = time.time()
time_difference = time.time() - startTime
x = dt.datetime.now()

if sType == 'q':
    quickSort(Data, 0, int(dSize) - 1) 
    print("Quicksort run time expressed in Hours, Minutes, Seconds was...")
    print(time.strftime("%H:%M:%S", time.gmtime(time.time() - startTime)))
    tDiff = (dt.datetime.now() - x)
    milliSec = tDiff.total_seconds() * 1000
    print("Or in milliseconds")
    print(milliSec)

if sType == 'i':
    Data = insertionSort(Data)
    print("Insertion Sort run time expressed in Hours, Minutes, Seconds was...")
    print(time.strftime("%H:%M:%S", time.gmtime(time.time() - startTime)))
    tDiff = (dt.datetime.now() - x)
    milliSec = tDiff.total_seconds() * 1000
    print("Or in milliseconds")
    print(milliSec)

if sType == 's':
    Data = selectionSort(Data)
    print("Selection Sort run time expressed in Hours, Minutes, Seconds was...")
    print(time.strftime("%H:%M:%S", time.gmtime(time.time() - startTime)))
    tDiff = (dt.datetime.now() - x)
    milliSec = tDiff.total_seconds() * 1000
    print("Or in milliseconds")
    print(milliSec)

checkCorrect(Data)