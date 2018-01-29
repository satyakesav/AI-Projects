import sys
import random
import copy
from collections import deque
import Queue
import time
from math import ceil, floor

#Round-off function to support display of time
def float_round(num, places = 0, direction = floor):
    return direction(num * (10**places)) / float(10**places)
start_time = time.time()

global_val = 0

#Heuristic-3 is the best heuristic which can solve problems having a depth of 25 within 200 goal tests
# (works for 7 stacks & 17 blocks within few seconds)
def heuristic3(snode):
    arr = copy.deepcopy(snode.lst)
    hval = 0
    i = 0
    while(i<arr[0].__len__() and arr[0][i]==i):
        i = i+1
    st = -1
    for l in range(0,arr.__len__()):
        for j in range(0,arr[l].__len__()):
            if (arr[l][j]==i):
                st = l
                break
    while(arr[0].__len__() > i):
        l = arr[0].__len__()-1
        ind = -1
        for j in range(1,arr.__len__()):
            if (arr[j].__len__()==0):
                arr[j].append(arr[0][l])
                del arr[0][-1]
                hval = hval+1
                break
            if (st != j and arr[0][l]<arr[j][arr[j].__len__()-1]) or (j == arr.__len__()-1):
                arr[j].append(arr[0][l])
                del arr[0][-1]
                hval = hval+1
                break
    for i in range(1, arr.__len__()):
        min = 31242315234
        ind = -1
        for j in range(0, arr[i].__len__()):
            if (min > arr[i][j]):
                min = arr[i][j]
                ind = j
        if (ind != -1):
            staks = arr.__len__()-2
            for j in range(arr[i].__len__()-1, ind, -1):
                if (arr[i][j]<arr[i][j-1]):
                    if staks==1:
                        hval = hval+3
                    else:
                        hval = hval+2
                        staks = staks-1
                else:
                    staks = arr.__len__()-2
                    hval = hval+2
            hval = hval+1
        for j in range(ind-1, 0, -1):
            if (arr[i][j]>arr[i][j-1]):
                hval = hval+2
            else:
                hval = hval+1
        if (ind!=0 and arr[i].__len__()>0):
            hval = hval+1
    return hval

#Heuristic-2 is the 2nd efficient function among all my heuristics but is computationally better than H-3
def heuristic2(snode):
    arr = snode.lst
    hval = 0
    i = 0
    while(i<arr[0].__len__() and arr[0][i]==i):
        i = i+1
    hval = 2*(arr[0].__len__() - i)
    for i in range(1, arr.__len__()):
        min = 31242315234
        ind = -1
        for j in range(0, arr[i].__len__()):
            if (min > arr[i][j]):
                min = arr[i][j]
                ind = j
        if (ind!=-1):
            hval = hval + 2*(arr[i].__len__()-ind-1)+1
        for j in range(ind-1, 0, -1):
            if (arr[i][j]>arr[i][j-1]):
                hval = hval+2
            else:
                hval = hval+1
        if (ind!=0 and arr[i].__len__()>0):
            hval = hval+1
    return hval

#The basic heuristic derived directly from my intuition (But, it is lot efficient - can solve the 5 stacks and 10 blocks in milli seconds)
def heuristic1(snode):
    arr = snode.lst
    hval = 0
    i = 0
    while(i<arr[0].__len__() and arr[0][i]==i):
        i = i+1
    hval = 2*(arr[0].__len__() - i)
    for i in range(1, arr.__len__()):
        for j in range(arr[i].__len__()-1, 0, -1):
            if (arr[i][j]>arr[i][j-1]):
                hval = hval+2
            else:
                hval = hval+1
        if (arr[i].__len__()>0):
            hval = hval+1
    return hval


def heuristic(snode):
    return 0

#This is the Node class which supports successor generation, Goal test and random start state generation methods
class Node:
    lst = []
    depth = 0
    cost = 0
    num_stacks = 0
    num_blocks = 0
    def __init__(self, num_stacks, num_blocks):
        self.lst = []
        self.father = None
        self.depth = 0
        self.cost = 0
        self.num_blocks = num_blocks
        self.num_stacks = num_stacks
        for x in range(0, self.num_stacks):
            eachstack = []
            self.lst.append(eachstack)  # creating a 2D list of blocks i.e. for each stack a block list

    def getfather(self):
        return self.father

    def GoalNodeCheck(self):
        if (self.lst[0].__len__() != self.num_blocks):
            return False
        for x in range(0, self.num_blocks):
            if self.lst[0][x]!=(x):
                return False
        return True

    def operationNode(self, source, destination):
        if self.lst[source] == []:
            return
        if source==destination:
            return
        if source>self.lst.__len__() or destination>self.lst.__len__():
            print("Error: Source or Destination is beyond the stack size")
        self.lst[destination].append(self.lst[source][-1])
        self.lst[source].pop()

    def GenerateRandomNode(self, max_steps):
        for i in range(0, self.num_blocks):
            self.lst[0].append(i)
        #steps = random.randint(max_steps/2, max_steps)-self.num_blocks/2-2
        steps = max_steps - self.num_blocks/2-2
        for i in range(0, self.num_blocks-1):
            self.operationNode(0, random.randint(1,self.num_stacks-1))
        for i in range(0, steps):
            self.operationNode(random.randint(0,self.num_stacks-1), random.randint(0,self.num_stacks-1))

    def successor(self):
        retlist = []
        for i in range(0,self.num_stacks):
            for j in range(0, self.num_stacks):
                if (i!=j):
                    if (self.lst[i].__len__()==0):
                        continue
                    newnode = Node(self.num_stacks, self.num_blocks)
                    newnode.lst = copy.deepcopy(self.lst)
                    newnode.operationNode(i, j)
                    newnode.father = self
                    newnode.depth = self.depth+1
                    retlist.append(newnode)
        return retlist
    def __cmp__(self, other):
        return cmp(self.cost, other.cost)

#Prints the state of the graph
def printstack(stacklist):
    for i in range(0, stacklist.__len__()):
        sys.stdout.write("Stack-"+str(i+1)+"    ")
        for j in range(0, stacklist[i].__len__()):
            sys.stdout.write(str(1+stacklist[i][j]) + " ")
        print("")
    print("-----------------------------------------------------------")

#Traceback function to print all the path from the source to goal state
def traceback(parent, dep):
    global global_val
    if (parent.cost == -1):
        global_val = dep
        return
    traceback(parent.father, dep+1)
    print("Next Step:")
    printstack(parent.lst)

#BFS implementation for validating the optimality/admissibility of my heuristic
def BFS(src, num_stacks, num_blocks):
    print("")
    print("******************** Applying BFS Algorithm ********************")
    if (src.GoalNodeCheck()):
        return
    covered_list = []
    goalnode = src
    q = [src]
    src.cost = -1
    q = deque(q)
    global_flag = 0
    maxq = 1
    goal_tests = 1
    while(q.__len__()!=0):
        current = q.popleft()
        covered_list.append(current.lst)
        children = current.successor()
        for i in range(0,children.__len__()):
            flag = 0
            for j in range(0, covered_list.__len__()):
                if (covered_list[j]==children[i].lst):
                    flag=1
                    break
            if (flag!=1):
                q.append(children[i])
                goal_tests = goal_tests + 1
                if (children[i].GoalNodeCheck()):
                    goalnode = children[i]
                    global_flag = 1
                    break
        if (global_flag==1):
            break
        if (maxq<q.__len__()):
            maxq = q.__len__()
    print("The maximum queue size is                                  : "+str(maxq))
    print("The number of goal tests conducted is                      : "+str(goal_tests))
    traceback(goalnode, 0)

#The Astar search algorithm method
def Astar(src, num_stacks, num_blocks, options):
    global global_val
    print("******************** Applying A-star (Heuristic-"+ str(options)+") search Algorithm ********************")
    print("Source Node is ")
    printstack(src.lst)
    if (src.GoalNodeCheck()):
        return
    covered_list = []
    goalnode = src
    q = Queue.PriorityQueue()
    q.put(src)
    src.cost = -1
    global_flag = 0
    maxq = 1
    goal_tests = 1
    hval = 0
    while not q.empty():
        current = q.get()
        goal_tests = goal_tests + 1
        if (current.GoalNodeCheck()):
            goalnode = current
            break
        covered_list.append(current.lst)
        children = current.successor()
        for i in range(0,children.__len__()):
            flag = 0
            if (options == 1):
                hval = heuristic1(children[i])
            elif (options==2):
                hval = heuristic2(children[i])
            elif (options==3):
                hval = heuristic3(children[i])
            else:
                hval = heuristic(children[i])
            children[i].cost = children[i].depth + hval
            for j in range(0, covered_list.__len__()):
                if (covered_list[j]==children[i].lst):
                    flag=1
                    break
            if (flag!=1):
                q.put(children[i])
        if (maxq<q.qsize()):
            maxq = q.qsize()
        if (maxq > 100000):
            print("Queue size is exceeding the limit!!")
            return
    traceback(goalnode, 0)
    print("Summary: ")
    print("The maximum queue depth reached is                                         : "+str(maxq))
    print("The number of goal tests conducted is                                      : "+str(goal_tests))
    print("The number of steps the algorithm has taken to reach the goal state is     : "+str(global_val))

def main():
    global global_val
    print("Welcome to Blocksworld Puzzle! (Author: @Satya)")
    #print("-----------------------------------------------------------")
    num_stacks = 3
    num_blocks = 5
    num_stacks = input("Enter the number of stacks in the puzzle: ")
    num_blocks = input("Enter the number of blocks in the puzzle: ")

    src = Node(num_stacks, num_blocks)
    string_input = str(raw_input("Do you want to enter a custom source state (strictly enter Y for yes and N for no) : "))
    if (string_input == 'Y' or string_input=='y'):
        for i in range(0, num_stacks):
            inp = raw_input("Enter the blocks (separated by spaces, 1-"+str(num_blocks)+ ") in stack-"+str(i+1)+" : ")
            l = []
            l = [(int(n)-1) for n in inp.split()]
            src.lst[i] = l
    else:
        if (num_stacks <= 5 and num_blocks <= 10):
            src.GenerateRandomNode(500)
        else:
            src.GenerateRandomNode(80)

    if (string_input == 'Y' or string_input == 'y'):
        print("I am not making sure that all blocks you have entered are unique. So please verify if you have entered them correctly or not!!")

    for i in range(0, num_stacks):
        for j in range(0, src.lst[i].__len__()):
            if (src.lst[i][j]>=num_blocks or src.lst[i][j]<=-1):
                print("The program might not work properly because you haven't entered the blocks with in the limits")
                print("Please rerun the program and enter the values between 1 to "+str(num_blocks))

    option = input("Choose the heuristic you want to test (1, 2 or 3) (3 works best and it works up to 7 stacks and 20 blocks) : ")
    print("")
    print("Note: If you have entered above 5 stacks or 15 blocks, then please wait for a couple of minutes")
    Astar(src, num_stacks, num_blocks, option)

    #print("The total time taken to execute this program is                            : " + str(float_round(time.time() - start_time, 3, ceil)) + " seconds")

if __name__== "__main__":
  main()