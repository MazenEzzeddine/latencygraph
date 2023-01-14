# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import math

import csv

from numpy import double


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



def justoldworkload():
    # https://snapshots.raintank.io/dashboard/snapshot/Jo4ozA2mXuSQl3Lqgsi32ZGs9woFP5N8
    t = []
    lamda = []
    replicas = []

    with open('defaultArrivalRatesm1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            t.append(math.floor(double(row[0])))
            lamda.append(double(row[1]))
            if math.floor(double(row[0])) < 98:
                replicas.append(1)
            elif math.floor(double(row[0])) < 451:
                replicas.append(2)
            elif math.floor(double(row[0])) < 547:
                replicas.append(3)
            elif math.floor(double(row[0])) < 562:
                replicas.append(2)
            # elif math.floor(double(row[0])) < 273:
            #     replicas.append(3)
            # elif math.floor(double(row[0])) < 344:
            #     replicas.append(4)
            # elif math.floor(double(row[0])) < 375:
            #     replicas.append(3)
            # elif math.floor(double(row[0])) < 415:
            #     replicas.append(2)
            # elif math.floor(double(row[0])) < 446:
            #     replicas.append(3)
            # elif math.floor(double(row[0])) < 477:
            #     replicas.append(4)
            # elif math.floor(double(row[0])) < 509:
            #     replicas.append(5)
            # elif math.floor(double(row[0])) < 539:
            #     replicas.append(4)
            # elif math.floor(double(row[0])) < 570:
            #     replicas.append(3)
            else:
                replicas.append(1)

    for r in range(len(replicas)):
        print(replicas[r])
    print(len(replicas))
    print(len(t))
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(t, lamda, color='blue', label='workload')
    ax2.plot(t, replicas, '--r',  label='replicas')

    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('Event Arrivals Rate')
    #ax2.spines['left'].set_color('blue')
    #ax2.spines['right'].set_color('red')

    #ax2.set_ylabel('Consumer replicas')

    plt.title('Workload ')
    ax1.legend()
    ax2.legend(loc=1)
    plt.show()



def justoldworkloadf7():
    # https://snapshots.raintank.io/dashboard/snapshot/Jo4ozA2mXuSQl3Lqgsi32ZGs9woFP5N8
    t = []
    lamda = []
    replicas = []

    with open('defaultArrivalRatesm1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            t.append(math.floor(double(row[0])))
            lamda.append(double(row[1])*0.7)
            if math.floor(double(row[0])) < 274: ##380:
                replicas.append(1)
            elif math.floor(double(row[0])) < 375:
                replicas.append(2)
            elif math.floor(double(row[0])) < 430:
                replicas.append(1)
            elif math.floor(double(row[0])) < 540:
                replicas.append(2)
            # elif math.floor(double(row[0])) < 273:
            #     replicas.append(3)
            # elif math.floor(double(row[0])) < 344:
            #     replicas.append(4)
            # elif math.floor(double(row[0])) < 375:
            #     replicas.append(3)
            # elif math.floor(double(row[0])) < 415:
            #     replicas.append(2)
            # elif math.floor(double(row[0])) < 446:
            #     replicas.append(3)
            # elif math.floor(double(row[0])) < 477:
            #     replicas.append(4)
            # elif math.floor(double(row[0])) < 509:
            #     replicas.append(5)
            # elif math.floor(double(row[0])) < 539:
            #     replicas.append(4)
            # elif math.floor(double(row[0])) < 570:
            #     replicas.append(3)
            else:
                replicas.append(1)

    for r in range(len(replicas)):
        print(replicas[r])
    print(len(replicas))
    print(len(t))
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(t, lamda, color='blue', label='workload')
    ax2.plot(t, replicas, '--r',  label='replicas')

    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('Event Arrivals Rate')
    #ax2.spines['left'].set_color('blue')
    #ax2.spines['right'].set_color('red')

    #ax2.set_ylabel('Consumer replicas')

    plt.title('Workload ')
    ax1.legend()
    ax2.legend(loc=1)




    ##############################################
    lamda15 = []
    s15 = 0
    s5 = 0
    s1 = 0


    ###################################################
    with open('Latency-data-2023-01-14 13_33_52.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            #t.append(math.floor(double(row[0])))
            #t.append(str(row[0]))
            #t15.append(s15)
            s15 +=5
            lamda15.append(double(row[1]))

    ###################################################
    plt.show()



def justoldworkloadf7lag():
    # https://snapshots.raintank.io/dashboard/snapshot/Jo4ozA2mXuSQl3Lqgsi32ZGs9woFP5N8
    t = []
    lamda = []
    replicas = []

    with open('defaultArrivalRatesm1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            t.append(math.floor(double(row[0])))
            lamda.append(double(row[1])*0.7)
            if math.floor(double(row[0])) < 274: ##380:
                replicas.append(1)
            elif math.floor(double(row[0])) < 375:
                replicas.append(2)
            elif math.floor(double(row[0])) < 430:
                replicas.append(1)
            elif math.floor(double(row[0])) < 540:
                replicas.append(2)
            # elif math.floor(double(row[0])) < 273:
            #     replicas.append(3)
            # elif math.floor(double(row[0])) < 344:
            #     replicas.append(4)
            # elif math.floor(double(row[0])) < 375:
            #     replicas.append(3)
            # elif math.floor(double(row[0])) < 415:
            #     replicas.append(2)
            # elif math.floor(double(row[0])) < 446:
            #     replicas.append(3)
            # elif math.floor(double(row[0])) < 477:
            #     replicas.append(4)
            # elif math.floor(double(row[0])) < 509:
            #     replicas.append(5)
            # elif math.floor(double(row[0])) < 539:
            #     replicas.append(4)
            # elif math.floor(double(row[0])) < 570:
            #     replicas.append(3)
            else:
                replicas.append(1)
        ##############################################
    t15=[]
    lamda15 = []
    s15 = 0
    s5 = 0
    s1 = 0

    ###################################################
    with open('Latency-data-2023-01-14 13_33_52.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t15.append(s15)
            s15 += 5
            lamda15.append(double(row[1]))

    for r in range(len(lamda15)):
        print(lamda15[r])
    print(len(lamda15))
   # print(len(t))
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(t, lamda, color='blue', label='workload')
    ax2.plot(t15, lamda15, '--r',  label='latency')

    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('Event Arrivals Rate')


    plt.title('Workload ')
    ax1.legend()
    ax2.legend(loc=1)
    ###################################################
    plt.show()


def justoldworkloadf7lag2():
    # https://snapshots.raintank.io/dashboard/snapshot/Jo4ozA2mXuSQl3Lqgsi32ZGs9woFP5N8
    t = []
    lamda = []
    replicas = []

    with open('defaultArrivalRatesm1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            t.append(math.floor(double(row[0])))
            lamda.append(double(row[1])*0.7)
            if math.floor(double(row[0])) < 264: ##380:
                replicas.append(1*175)
            elif math.floor(double(row[0])) < 375:
                replicas.append(2*175)
            elif math.floor(double(row[0])) < 430:
                replicas.append(1*175)
            elif math.floor(double(row[0])) < 540:
                replicas.append(2*175)
            # elif math.floor(double(row[0])) < 273:
            #     replicas.append(3)
            # elif math.floor(double(row[0])) < 344:
            #     replicas.append(4)
            # elif math.floor(double(row[0])) < 375:
            #     replicas.append(3)
            # elif math.floor(double(row[0])) < 415:
            #     replicas.append(2)
            # elif math.floor(double(row[0])) < 446:
            #     replicas.append(3)
            # elif math.floor(double(row[0])) < 477:
            #     replicas.append(4)
            # elif math.floor(double(row[0])) < 509:
            #     replicas.append(5)
            # elif math.floor(double(row[0])) < 539:
            #     replicas.append(4)
            # elif math.floor(double(row[0])) < 570:
            #     replicas.append(3)
            else:
                replicas.append(1*175)
        ##############################################
    t15=[]
    lamda15 = []
    s15 = 0
    s5 = 0
    s1 = 0

    ###################################################
    with open('Latency-data-2023-01-14 13_33_52.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t15.append(s15)
            s15 += 5
            lamda15.append(double(row[1]))

    for r in range(len(lamda15)):
        print(lamda15[r])
    print(len(lamda15))
   # print(len(t))
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(t, lamda, color='blue', label='workload')
    ax2.plot(t15, lamda15, '--r',  label='latency')

    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('Event Arrivals Rate')


    plt.title('Workload ')
    ax1.plot(t, replicas, '-g', label='replicas')
    ax1.legend()
    ax2.legend(loc=1)
    ###################################################
    plt.show()

if __name__ == '__main__':
    justoldworkload()
    justoldworkloadf7()
    justoldworkloadf7lag()
    justoldworkloadf7lag2()



