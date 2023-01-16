
import matplotlib.pyplot as plt
import math

import csv

from numpy import double



def justoldworkloadf7lag2():
    # https://snapshots.raintank.io/dashboard/snapshot/Jo4ozA2mXuSQl3Lqgsi32ZGs9woFP5N8
    t = []
    lamda = []
    replicas = []

    with open('defaultArrivalRatesm1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            t.append(math.floor(double(row[0])))
            lamda.append(double(row[1])*0.8*0.6)
            replicas.append(1*175)
            # if math.floor(double(row[0])) < 264: ##380:
            #     replicas.append(1*175)
            # elif math.floor(double(row[0])) < 375:
            #     replicas.append(2*175)
            # elif math.floor(double(row[0])) < 430:
            #     replicas.append(1*175)
            # elif math.floor(double(row[0])) < 540:
            #     replicas.append(2*175)
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
            # else:
            #     replicas.append(1*175)
        ##############################################
    t15=[]
    lamda15 = []
    s15 = 0
    s5 = 0
    s1 = 0

    ###################################################
    with open('186.txt', 'r') as csvfile:
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
    ax1.plot(t, lamda, color='blue', label='issuer workload')
    ax2.plot(t15, lamda15, '--r',  label='end to end latency')

    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('Event Arrivals Rate')


    ##plt.title('Workload ')
    ax1.plot(t, replicas, '-g', label='max consumption rate')
    ax1.legend()
    ax2.legend(loc=1)
    ax2.set_ylabel('Latency (ms)')
    ###################################################
    plt.show()



def security():
    # https://snapshots.raintank.io/dashboard/snapshot/Jo4ozA2mXuSQl3Lqgsi32ZGs9woFP5N8
    t = []
    lamda = []
    replicas = []

    with open('defaultArrivalRatesm1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            t.append(math.floor(double(row[0])))
            lamda.append(double(row[1]))

            if math.floor(double(row[0])) < 97: ##380:
                replicas.append(1*175)
            elif math.floor(double(row[0])) < 449:
               replicas.append(2*175)
            elif math.floor(double(row[0])) < 547:
               replicas.append(3*175)
            elif math.floor(double(row[0])) < 566:
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
    # with open('186.txt', 'r') as csvfile:
    #     plots = csv.reader(csvfile, delimiter=',')
    #     for row in plots:
    #         # t.append(math.floor(double(row[0])))
    #         # t.append(str(row[0]))
    #         t15.append(s15)
    #         s15 += 5
    #         lamda15.append(double(row[1]))

   ##################################################################*


   # print(len(t))
    fig, ax1 = plt.subplots()

    ax1.plot(t, lamda, color='blue', label='Security workload')

    #ax2 = ax1.twinx()
    ##ax2.plot(t15, lamda15, '--r',  label='end to end latency')

    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('Event Arrivals Rate')


    ##plt.title('Workload ')
    ax1.plot(t, replicas, '-g', label='max consumption rate')
    ax1.legend()
    #ax2.legend(loc=1)
    #ax2.set_ylabel('Latency (ms)')
    ###################################################
    plt.show()


def acquirer():
    # https://snapshots.raintank.io/dashboard/snapshot/Jo4ozA2mXuSQl3Lqgsi32ZGs9woFP5N8
    t = []
    lamda = []
    replicas = []

    with open('defaultArrivalRatesm1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            t.append(math.floor(double(row[0])))
            lamda.append(double(row[1])*0.8)

            if math.floor(double(row[0])) < 264: ##380:
                replicas.append(1*175)
            elif math.floor(double(row[0])) < 555:
               replicas.append(2*175)
            # elif math.floor(double(row[0])) < 547:
            #    replicas.append(3*175)
            # elif math.floor(double(row[0])) < 566:
            #      replicas.append(2*175)
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
    # with open('186.txt', 'r') as csvfile:
    #     plots = csv.reader(csvfile, delimiter=',')
    #     for row in plots:
    #         # t.append(math.floor(double(row[0])))
    #         # t.append(str(row[0]))
    #         t15.append(s15)
    #         s15 += 5
    #         lamda15.append(double(row[1]))

   ##################################################################*


   # print(len(t))
    fig, ax1 = plt.subplots()

    ax1.plot(t, lamda, color='blue', label='Acquirer workload')

    #ax2 = ax1.twinx()
    ##ax2.plot(t15, lamda15, '--r',  label='end to end latency')

    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('Event Arrivals Rate')


    ##plt.title('Workload ')
    ax1.plot(t, replicas, '-g', label='max consumption rate')
    ax1.legend()
    #ax2.legend(loc=1)
    #ax2.set_ylabel('Latency (ms)')
    ###################################################
    plt.show()



if __name__ == '__main__':
    justoldworkloadf7lag2()
    security()
    acquirer()