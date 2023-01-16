import matplotlib.pyplot as plt
import math

import csv

from numpy import double


def graf():
    t5 = []
    t15 = []
    lamda15 = []
    lamda5 = []

    t1 = []
    lamda1 = []

    s15 = 0
    s5 = 0
    s1 = 0
    with open('arrival177.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t15.append(s15)
            s15 += 5
            lamda15.append(double(row[1]))



    with open('replicas177.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t1.append(s1)
            s1 += 5
            lamda1.append(double(row[1]))

    t=0
    lt=[]
    lv=[]
    with open('latency177.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            lt.append(t)
            t += 5
            lv.append(double(row[1]))

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    # ax1.plot(t5, lamda5, color='blue', label='arrival rate')
    # ax1.plot(t15, lamda15, color='red', label='consumption rate')
    # ax1.plot(t1, lamda1, color='black', label='Max consumption rate')
    ##rep = []
    # for r in lamda5:
    #     var = r / 95
    #     rep.append(var)

    ##ax1.plot(t5, lamda5)
    ax1.plot(t15, lamda15, label='Arrival rate')
    ax1.plot(t1, lamda1, label='Maximum consumption rate \n (number of replicas)')

    ax2.plot(lt, lv, 'r', label='latency (ms)')
    #
    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('Event Arrival Rate')
    # #ax2.spines['left'].set_color('blue')
    # #ax2.spines['right'].set_color('red')
    #
    #ax2.set_ylabel('Consumer replicas')
    #
    plt.title('Bin pack autoscaler')
    ax1.legend()
    #ax2.legend(loc=4)
    #
    plt.show()






if __name__ == '__main__':
    graf()